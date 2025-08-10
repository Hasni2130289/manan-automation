import os
import pyfiglet
from termcolor import colored
import subprocess

# Password system
PASSWORD = "manan"

# Banner
banner = pyfiglet.figlet_format("Manan Downloader")
print(colored(banner, "cyan"))

# Password prompt
while True:
    user_pass = input(colored("Enter password: ", "yellow"))
    if user_pass == PASSWORD:
        print(colored("✅ Access Granted!", "green"))
        break
    else:
        print(colored("❌ Wrong password! Try again.", "red"))

# Profile link input
profile_url = input(colored("Enter profile link: ", "yellow"))

# Save location
save_path = "/sdcard/Download"
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Download using yt-dlp
print(colored(f"📥 Downloading from: {profile_url}", "cyan"))
try:
    subprocess.run(["yt-dlp", "-o", f"{save_path}/%(title)s.%(ext)s", profile_url])
    print(colored(f"✅ Download completed! Files saved in {save_path}", "green"))
except Exception as e:
    print(colored(f"❌ Error: {str(e)}", "red"))# manan-automation
