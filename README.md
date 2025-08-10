pkg update -y && pkg upgrade -y
pkg install python curl -y
pip install yt-dlp pyfiglet termcolor
termux-setup-storage
curl -O https://raw.githubusercontent.com/Hasni2130289/manan-automation/main/manan_downloader.py
python manan_downloader.py

# Password system
PASSWORD = "manan"
