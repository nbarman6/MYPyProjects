"""Simple Facebook video downloader using yt-dlp.

This script downloads a public Facebook video (or reel) given its URL.
It uses yt-dlp under the hood. If yt-dlp is not installed the script will
explain how to install it.

Usage examples:
    - Interactive: python download.py
    - CLI: python download.py "https://www.facebook.com/..." --output C:\\Downloads
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Optional

try:
    import yt_dlp
except Exception as e:  # pragma: no cover - helpful runtime message
    print(
        "yt-dlp is required but not installed. Install with: python -m pip install yt-dlp",
        file=sys.stderr,
    )
    raise


def download_facebook_video(url: str, output_path: str = ".") -> Optional[str]:
    """Download a public Facebook video using yt-dlp.

    Args:
        url: The public Facebook video or reel URL.
        output_path: Directory to save the downloaded file.

    Returns:
        The path to the downloaded file if available, otherwise None.
    """
    if not url or not isinstance(url, str):
        raise ValueError("A valid URL string must be provided")

    # Normalize and create output directory if needed
    output_path = os.path.abspath(os.path.expanduser(output_path))
    os.makedirs(output_path, exist_ok=True)

    outtmpl = os.path.join(output_path, "%(title)s.%(ext)s")

    ydl_opts = {
        # prefer to merge best video+audio into a single file when possible
        "format": "bestvideo+bestaudio/best",
        "outtmpl": outtmpl,
        "noplaylist": True,
        # be a bit verbose so users see progress/errors; callers can silence
        # by adjusting logging in yt-dlp if needed
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            # yt-dlp returns info dict; if a filename is available, construct it
            if info:
                filename = ydl.prepare_filename(info)
                # prepare_filename may return a name with an extension yt-dlp didn't merge into,
                # so return the path as-is (it should exist after download)
                return os.path.abspath(filename)
    except yt_dlp.utils.DownloadError as de:
        print(f"Download error: {de}", file=sys.stderr)
        return None
    except Exception as exc:
        print(f"Unexpected error while downloading: {exc}", file=sys.stderr)
        return None


def _parse_args(argv) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download public Facebook videos (using yt-dlp)")
    p.add_argument("url", nargs="?", help="Facebook video or reel URL")
    p.add_argument("-o", "--output", default=".", help="Output directory (default: current dir)")
    return p.parse_args(argv)


def main(argv=None) -> int:
    args = _parse_args(argv or sys.argv[1:])

    url = args.url
    if not url:
        # fall back to interactive prompt to preserve previous behavior
        try:
            url = input("Enter the Facebook video URL: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("No URL provided, exiting.")
            return 1

    if not url:
        print("No URL provided, exiting.")
        return 1

    print(f"Downloading from: {url}\nSaving to: {os.path.abspath(args.output)}")
    result = download_facebook_video(url, args.output)

    if result:
        print(f"✅ Download complete: {result}")
        return 0
    else:
        print("❌ Download failed. See messages above.")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
