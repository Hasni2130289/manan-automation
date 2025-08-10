import os
import sys
import time
import yt_dlp
from termcolor import colored

# ---------- Banner ----------
def banner():
    os.system("clear")
    print(colored("       MANAN", "cyan", attrs=["bold"]))
    print(colored("   AUTOMATION", "cyan", attrs=["bold"]))
    print()

# ---------- Password Check ----------
def password_check():
    correct_password = "manan"
    pwd = input(colored("[?] Enter Password: ", "yellow", attrs=["bold"]))
    if pwd != correct_password:
        print(colored("❌ Wrong password! Exiting...", "red", attrs=["bold"]))
        sys.exit()
    print(colored("✅ Password Accepted!", "green", attrs=["bold"]))
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
        print(colored("✅ Download Complete!", "green", attrs=["bold"]))
    except Exception as e:
        print(colored(f"❌ Error: {e}", "red", attrs=["bold"]))

# ---------- Menu ----------
def menu():
    while True:
        banner()
        print(colored("[1] Download TikTok Video", "yellow", attrs=["bold"]))
        print(colored("[2] Download Facebook Video", "yellow", attrs=["bold"]))
        print(colored("[3] Download YouTube Shorts", "yellow", attrs=["bold"]))
        print(colored("[4] Exit", "yellow", attrs=["bold"]))
        print(colored("=" * 40, "cyan"))

        choice = input(colored("Select option: ", "cyan", attrs=["bold"]))

        if choice == "1":
            url = input(colored("Enter TikTok URL: ", "yellow", attrs=["bold"]))
            download_video(url)
            input(colored("Press Enter to return to menu...", "cyan"))
        elif choice == "2":
            url = input(colored("Enter Facebook URL: ", "yellow", attrs=["bold"]))
            download_video(url)
            input(colored("Press Enter to return to menu...", "cyan"))
        elif choice == "3":
            url = input(colored("Enter YouTube Shorts URL: ", "yellow", attrs=["bold"]))
            download_video(url)
            input(colored("Press Enter to return to menu...", "cyan"))
        elif choice == "4":
            print(colored("👋 Exiting...", "red", attrs=["bold"]))
            sys.exit()
        else:
            print(colored("❌ Invalid choice!", "red", attrs=["bold"]))
            time.sleep(1)

# ---------- Main ----------
if __name__ == "__main__":
    banner()
    password_check()
    menu()
