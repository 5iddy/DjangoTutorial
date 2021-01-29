from django.db import models
import os
from youtube_dl import YoutubeDL
# Create your models here.
BASE_FILE_DIR = os.getcwd()



class YtVid(models.Model):
    video_id = models.CharField(max_length=20,null=False, primary_key=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        url = f"https://www.youtube.com/watch?v={self.video_id}"

    @staticmethod


    def download_vid(self, format_code):
        ydl_opts = {
            'format': format_code,
            'outtmpl': 'static/downloads/%(id)/%(format_id).%(ext)'
        }
        if os.path.exists(f'static/downloads/{self.video_id}'):
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
        else:
            os.mkdir(f'static/downloads/{self.video_id}')
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])