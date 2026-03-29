import yt_dlp

async def downloadVideo(url: str) -> str:
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': 'downloads/%(title)s.%(ext)s.%(epoch)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url)
    return ydl.prepare_filename(info)