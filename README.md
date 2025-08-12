# 📥 Manan Downloader

A Termux-based video downloader for TikTok, Facebook, and YouTube Shorts with a password-protected menu and rainbow banner.

## 📌 Features
- Rainbow-style banner & menu
- Password protection (`contanct for paswrd ( +92 03250758526`)
- Saves videos to `/storage/emulated/0/MananDownloads`
- Supports TikTok, Facebook, YouTube Shorts

## 🚀 How to Install in Termux

termux-setup-storage && \
pkg update -y && pkg upgrade -y && \
pkg install python -y git -y && \
pip install yt-dlp termcolor pyfiglet && \
rm -rf manan-automation && \
git clone https://github.com/Hasni2130289/manan-automation.git && \
cd manan-automation && \
python3 manan_downloader.py
