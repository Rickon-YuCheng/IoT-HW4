"""### 3. 用 Gradio 打造 Web App

我們先來安裝 `openai` 套件, 還有快速打造 Web App 的 `gradio`。
"""


import os

import gradio as gr
import requests

try:
    # 嘗試讀取同目錄的 .env，但沒有安裝 python-dotenv 也不會中斷
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
except Exception:
    # 若 .env 讀取有例外，保持靜默，避免影響主流程
    pass

system="""
請用台灣習慣的中文來寫這段 po 文：
請用員瑛式思考, 也就是什麼都正向思維任何使用者寫的事情,
用我的第一人稱、社群媒體 po 文的口吻說一次,
說為什麼這是一件超幸運的事, 並且以「完全是 Lucky Vicky 呀!」結尾。
可以適度的加上 emoji。
"""

"""設定你要的模型。"""

# provider = "openai"
# model = "gpt-4o"

provider="groq"
model="llama-3.3-70b-versatile"

# provider = "groq"
# model = "gemma2-9b-it"

# provider = "groq"
# model = "openai/gpt-oss-120b"

if provider == "groq" and not os.getenv("GROQ_API_KEY"):
    raise RuntimeError("缺少 GROQ_API_KEY，請在環境變數或 .env 中設定你的 Groq 金鑰後再執行。")

GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"

def reply(system: str, prompt: str, provider: str, model: str) -> str:
    if provider != "groq":
        raise ValueError("目前僅支援 provider=='groq'。")

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("缺少 GROQ_API_KEY，請在環境變數或 .env 中設定你的 Groq 金鑰後再執行。")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = requests.post(GROQ_CHAT_URL, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

def lucky_post(prompt):
    response = reply(system=system,
                     prompt=prompt,
                     provider = provider,
                     model = model
                    )
    return response

with gr.Blocks(title="員瑛式思考產生器") as demo:
    gr.Markdown("### ꒰*ˊᵕˋ꒱ 員瑛式思考產生器 Lucky Vicky 🌈")
    gr.Markdown("請輸入一件你覺得超小事，甚至有點倒楣的事，讓我幫你用員瑛式思考，超正向的方式重新詮釋！")

    with gr.Row():
        user_input = gr.Textbox(label="今天發生的事情是…", placeholder="例如：今天出門就下大雨, 可是忘了帶傘...")

    submit_btn = gr.Button("Lucky Vicky 魔法!")
    output = gr.Textbox(label="📣 員瑛式貼文", lines=10)

    submit_btn.click(fn=lucky_post, inputs=user_input, outputs=output)

demo.launch(share=True, debug=True)
