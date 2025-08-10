import os
import sys
import time
import yt_dlp
from termcolor import colored
import shutil

# ---------- Center Text Function ----------
def center_text(text):
    width = shutil.get_terminal_size().columns
    return text.center(width)

# ---------- Banner ----------
def banner():
    os.system("clear")
    print(colored(center_text("MANAN"), "white", attrs=["bold"]))
    print(colored(center_text("AUTOMATION"), "white", attrs=["bold"]))
    print()

# ---------- Password Check ----------
def password_check():
    correct_password = "manan"
    pwd = input(colored("[?] Enter Password: ", "white", attrs=["bold"]))
    if pwd != correct_password:
        print(colored("❌ Wrong password! Exiting...", "white", attrs=["bold"]))
        sys.exit()
    print(colored("✅ Password Accepted!", "white", attrs=["bold"]))
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
        print(colored("✅ Download Complete!", "white", attrs=["bold"]))
    except Exception as e:
        print(colored(f"❌ Error: {e}", "white", attrs=["bold"]))

# ---------- Menu ----------
def menu():
    while True:
        banner()
        print(colored(center_text("[1] Download TikTok Video"), "white", attrs=["bold"]))
        print(colored(center_text("[2] Download Facebook Video"), "white", attrs=["bold"]))
        print(colored(center_text("[3] Download YouTube Shorts"), "white", attrs=["bold"]))
        print(colored(center_text("[4] Exit"), "white", attrs=["bold"]))
        print(colored(center_text("=" * 40), "white", attrs=["bold"]))

        choice = input(colored(center_text("Select option: "), "white", attrs=["bold"]))

        if choice == "1":
            url = input(colored("Enter TikTok URL: ", "white", attrs=["bold"]))
            download_video(url)
            input(colored("Press Enter to return to menu...", "white"))
        elif choice == "2":
            url = input(colored("Enter Facebook URL: ", "white", attrs=["bold"]))
            download_video(url)
            input(colored("Press Enter to return to menu...", "white"))
        elif choice == "3":
            url = input(colored("Enter YouTube Shorts URL: ", "white", attrs=["bold"]))
            download_video(url)
            input(colored("Press Enter to return to menu...", "white"))
        elif choice == "4":
            print(colored("👋 Exiting...", "white", attrs=["bold"]))
            sys.exit()
        else:
            print(colored("❌ Invalid choice!", "white", attrs=["bold"]))
            time.sleep(1)

# ---------- Main ----------
if __name__ == "__main__":
    banner()
    password_check()
    menu()
