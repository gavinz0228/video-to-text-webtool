from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import uvicorn
import whisper
from tiktok_downloader.tiktok_downloader import TikTokDownloader
downloader = TikTokDownloader()


app = FastAPI()
templates = Jinja2Templates(directory="templates")
model = whisper.load_model("turbo")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.get("/stt/tiktok/")
async def stt_tiktok(request: Request):
    url = request.query_params.get("url")
    output_path = downloader.download_video(url)
    result = model.transcribe(output_path)
    print(result["text"])
    return {"text": result["text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
