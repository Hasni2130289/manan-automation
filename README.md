# 📥 Manan Downloader

A Termux-based video downloader for TikTok, Facebook, and YouTube Shorts with a password-protected menu and rainbow banner.

## 📌 Features
- Rainbow-style banner & menu
- Password protection (`manan`)
- Saves videos to `/storage/emulated/0/MananDownloads`
- Supports TikTok, Facebook, YouTube Shorts

## 🚀 How to Install in Termux

```bash
pkg update && pkg upgrade
pkg install python ffmpeg -y
pip install yt-dlp termcolor

# Grant Storage Permission
termux-setup-storage

# Download Script
wget https://raw.githubusercontent.com/Hasni2130289/manan_downloader.py/main/manan_downloader.py

# Run Script
python manan_downloader.py

PASSWORD = "manan"
