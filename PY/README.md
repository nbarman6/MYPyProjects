# Facebook video downloader (yt-dlp)

A small Python script to download public Facebook videos (or reels) using `yt-dlp`.

Requirements
- Python 3.7+
- Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Usage
- Interactive mode (prompts for URL):

```powershell
python download.py
```

- CLI mode:

```powershell
python download.py "https://www.facebook.com/..." --output C:\Downloads
```

Notes
- Private or age-restricted videos may require cookies or authentication; this script assumes public URLs.
- For advanced options (cookies, headers, rate limits) see the `yt-dlp` documentation.
