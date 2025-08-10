# 📥 Manan Downloader

A Termux-based video downloader for TikTok, Facebook, and YouTube Shorts with a password-protected menu and rainbow banner.

## 📌 Features
- Rainbow-style banner & menu
- Password protection (`manan`)
- Saves videos to `/storage/emulated/0/MananDownloads`
- Supports TikTok, Facebook, YouTube Shorts

## 🚀 How to Install in Termux

pkg update && pkg upgrade -y
pkg install python -y
pip install yt-dlp termcolor pyfiglet
pkg install git -y
git clone https://github.com/Hasni2130289/manan-automation
cd manan-automation
python manan_downloader.py
