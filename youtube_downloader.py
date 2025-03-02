import yt_dlp

def download_video(url):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': True,
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"\nDownloaded: {info['title']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_video(url)