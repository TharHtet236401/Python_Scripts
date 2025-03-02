import yt_dlp
import os

def download_video(url, output_path='./downloads'):
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Add path here
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
            print(f"Saved to: {os.path.abspath(output_path)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    custom_path = "C:/Users/Thar_Htet/Downloads/Video"
    download_video(url, custom_path)