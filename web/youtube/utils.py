from youtube_dl import YoutubeDL

def download_vid(url, format_code):
    ydl_opts = {
        'format': format_code,
        'outtmpl': 'static/downloads/%(id)_%(format_id).%(ext)'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def fetch_info(url):
    with YoutubeDL() as ytinfo:
        try:
            info = ytinfo.extract_info(url, ie_key=None,
                                       process=True, download=False,
                                       force_generic_extractor=False,
                                       extra_info={})
            ytinfo.list_formats(info)
            return info
        except Exception:
            print('Unable to fetch info')
            return None

info = fetch_info('https://www.youtube.com/watch?v=ZaijNcRuzsQ')
print(info)
# print(info['formats'][0]['format_id'])

# download_vid('https://www.youtube.com/watch?v=ZaijNcRuzsQ', '137+251')
