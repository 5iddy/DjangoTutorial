from django.shortcuts import render
from . import models
from youtube_dl import YoutubeDL
import os


# Create your views here.
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

def home_view(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        info = models.YoutubeVideo.fetch_info(url)
        context['formats'] = info['formats']

    return render(request, 'home/index.html', context)

def download(request, video_id, format_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    base_dir = os.getcwd()
    download_dir = os.path.join(base_dir, f'static/media/downloads/{video_id}')

    ydl_opts = {
        'format': format_id,
        'outtmpl': 'static/media/%(id)s_%(format_id)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    context = {
        'video_id':video_id,
        'format_id':format_id,
        'download_url': f'media/{video_id}_{format_id}.webm',
    }
    return render(request, 'download/index.html', context)