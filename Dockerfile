FROM pytorch/pytorch

RUN mkdir /app
WORKDIR /app
COPY *.py /app
COPY templates /app/templates
COPY tiktok_downloader/tik-tok-downloader.py /app/tiktok_downloader/tiktok_downloader.py
COPY tiktok_downloader/requirements.txt /app/tiktok_downloader/requirements.txt
COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r tiktok_downloader/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["uvicorn", "server:app","--host","0.0.0.0","--port","8080","--workers","4"]