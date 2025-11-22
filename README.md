# 客觀的人工智慧隨身教授 (Gradio / Streamlit)

使用 Groq LLM，提供「理工科指導教授」風格的 AI/ML 咨詢。提供 Gradio 與 Streamlit 兩種介面。

## 線上體驗
- Streamlit 部署網址：`<填入你的 Streamlit 網址>`  （部署後記得更新此欄位）

## 安裝與執行
1) 建立虛擬環境並安裝套件：
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2) 新增 `.env` 並填入你的 Groq API 金鑰：
```bash
GROQ_API_KEY=your_groq_key
```
### Gradio 介面
```bash
python IOT-hw4.py
```
終端機會顯示本機與公開分享 (share) 連結，可直接點擊使用。

### Streamlit 介面
```bash
streamlit run streamlit_app.py
```
預設在本機 `http://localhost:8501`，部署到 Streamlit Cloud 時請把專案加上環境變數 `GROQ_API_KEY`。

## 專案結構
- `IOT-hw4.py`：主程式，定義系統提示與 Gradio 介面。
- `streamlit_app.py`：同一個 AI 教授角色的 Streamlit 版本。
- `requirements.txt`：所需套件列表。
- `.gitignore`：忽略 `.env`、`.venv/`、`.gradio/`、`.streamlit/`、快取檔等不必要內容。

## 備註
- 請勿將個人 API 金鑰加入版本控制。
- share 連結由 Gradio 生成，僅在啟動期間有效；如需關閉公開通道，移除 `demo.launch` 的 `share=True` 參數即可。
