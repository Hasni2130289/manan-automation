# Manan Downloader

A simple Termux-based media downloader using `yt-dlp` with password protection.

## 📌 Features
- Password protection (`manan`)
- Downloads videos directly to `/sdcard/Download`
- Simple and fast

---

## ⚙️ Installation & Usage

```bash
pkg update -y && pkg upgrade -y
pkg install python curl -y
pip install yt-dlp pyfiglet termcolor
termux-setup-storage
curl -O https://raw.githubusercontent.com/Hasni2130289/manan_downloader.py/main/manan_downloader.py
python manan_downloader.py
# Password system
PASSWORD = "manan"
