from django.db import models
import os
from youtube_dl import YoutubeDL
# Create your models here.
BASE_FILE_DIR = os.getcwd()

class DownloadOptions(models.Model):
    format_id = models.IntegerField(primary_key=True)
    extension = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    filesize = models.CharField(max_length=50)

class YtVid(models.Model):
    download_links = models.ForeignKey(DownloadOptions, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        video_id = models.CharField(null=False, primary_key=True)
        video_file = models.FilePathField(path=self.gen_file_path)
        url = f"https://www.youtube.com/watch?v={self.video_id}"

    def gen_file_path(self):
        return os.path.join(BASE_FILE_DIR, f'static/downloads/{self.video_id}')

    @staticmethod
    def fetch_info(url):
        with YoutubeDL() as ytinfo:
            try:
                info = ytinfo.extract_info(url, ie_key=None,
                                           process=True, download=False,
                                           force_generic_extractor=False,
                                           extra_info={})
                return info
            except Exception:
                return None

    def download_vid(self, format_code):
        ydl_opts = {
            'format': format_code,
            'outtmpl': 'static/downloads/%(id)/%(format_id).%(ext)'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
