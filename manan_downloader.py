import os
import sys
import time
import yt_dlp
from termcolor import colored

# ---------- Rainbow Text Function ----------
def rainbow(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    result = ""
    for i, char in enumerate(text):
        result += colored(char, colors[i % len(colors)])
    return result

# ---------- Banner ----------
def banner():
    os.system("clear")
    print(rainbow("=" * 50))
    print(rainbow("      📥 MANAN DOWNLOADER 📥"))
    print(rainbow("=" * 50))
    print()

# ---------- Password Check ----------
def password_check():
    correct_password = "manan"
    pwd = input(colored("[?] Enter Password: ", "yellow"))
    if pwd != correct_password:
        print(colored("❌ Wrong password! Exiting...", "red"))
        sys.exit()
    print(colored("✅ Password Accepted!", "green"))
    time.sleep(1)

# ---------- Create Download Folder ----------
download_path = "/storage/emulated/0/MananDownloads"
if not os.path.exists(download_path):
    os.makedirs(download_path)

# ---------- Download Function ----------
def download_video(url):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(colored("✅ Download Complete!", "green"))
    except Exception as e:
        print(colored(f"❌ Error: {e}", "red"))

# ---------- Menu ----------
def menu():
    while True:
        banner()
        print(rainbow("[1] Download TikTok Video"))
        print(rainbow("[2] Download Facebook Video"))
        print(rainbow("[3] Download YouTube Shorts"))
        print(rainbow("[4] Exit"))
        print(rainbow("=" * 50))

        choice = input(colored("Select option: ", "cyan"))

        if choice == "1":
            url = input(colored("Enter TikTok URL: ", "yellow"))
            download_video(url)
            input(colored("Press Enter to return to menu...", "cyan"))
        elif choice == "2":
            url = input(colored("Enter Facebook URL: ", "yellow"))
            download_video(url)
            input(colored("Press Enter to return to menu...", "cyan"))
        elif choice == "3":
            url = input(colored("Enter YouTube Shorts URL: ", "yellow"))
            download_video(url)
            input(colored("Press Enter to return to menu...", "cyan"))
        elif choice == "4":
            print(colored("👋 Exiting...", "red"))
            sys.exit()
        else:
            print(colored("❌ Invalid choice!", "red"))
            time.sleep(1)

# ---------- Main ----------
if __name__ == "__main__":
    banner()
    password_check()
    menu()
