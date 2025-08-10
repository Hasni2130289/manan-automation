import os
import sys
import time
import yt_dlp
from termcolor import colored
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ---------- Gradient Text Function ----------
def gradient_text(text, colors):
    """Apply gradient colors to ASCII art text."""
    result = ""
    for i, char in enumerate(text):
        result += colors[i % len(colors)] + char
    return result + Style.RESET_ALL

# ---------- Banner with White Border ----------
def banner():
    os.system("clear")

    # Gradient color patterns
    colors1 = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    colors2 = [Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.RED]

    # Create ASCII art
    manan_text = pyfiglet.figlet_format("MANAN", font="banner3-D")
    automation_text = pyfiglet.figlet_format("AUTOMATION", font="banner3-D")

    # Combine both texts
    combined_text = gradient_text(manan_text, colors1) + gradient_text(automation_text, colors2)
    lines = combined_text.split("\n")

    # Calculate max width for border
    max_width = max(len(line) for line in lines)

    # Print top border
    print(Fore.WHITE + "╔" + "═" * max_width + "╗")

    # Print each line inside border
    for line in lines:
        print(Fore.WHITE + "║" + line.ljust(max_width) + Fore.WHITE + "║")

    # Print bottom border
    print(Fore.WHITE + "╚" + "═" * max_width + "╝\n")

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
        print(Fore.GREEN + "[1] TikTok Download")
        print(Fore.BLUE + "[2] Facebook Download")
        print(Fore.RED + "[3] YouTube Shorts Download")
        print(Fore.YELLOW + "[4] Exit" + Style.RESET_ALL)

        choice = input(colored("Choose an option [1-4]: ", "cyan"))

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
            print(colored("👋 Goodbye!", "red"))
            sys.exit()
        else:
            print(colored("❌ Invalid choice!", "red"))
            time.sleep(1)

# ---------- Main ----------
if __name__ == "__main__":
    banner()
    password_check()
    menu()
