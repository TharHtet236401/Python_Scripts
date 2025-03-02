import yt_dlp
import os

def download_media(url, output_path='./downloads', media_type='video'):
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_path, f'%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': True,
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        },
        'postprocessors': []
    }

    if media_type == 'video':
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        ydl_opts['merge_output_format'] = 'mp4'
        ydl_opts['postprocessors'].append({
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        })
    elif media_type == 'audio':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'].append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"\nDownloaded: {info['title']}")
            print(f"Saved to: {os.path.abspath(output_path)}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    media_type = input("Choose type (video/audio): ").lower().strip()
    custom_path = "C:/Users/Thar_Htet/Downloads/Video"
    
    download_media(
        url,
        output_path=custom_path if custom_path else None,
        media_type='video' if media_type.startswith('v') else 'audio'
    )