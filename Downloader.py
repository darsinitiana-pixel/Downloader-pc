import os
print("=========================================")
print("  TOOL DOWNLOAD YOUTUBE AUTOMATIC MP4  ")
print("=========================================")
url = input("Masukkan Link Channel/Video: ").strip()
user_profile = os.environ.get('USERPROFILE', 'C:\\Users\\Default')
out = f"{user_profile}\\Downloads"
print(f"\n[INFO] Video akan langsung disimpan ke folder Downloads PC.")
command = f'yt-dlp --sleep-interval 3 -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]" --merge-output-format mp4 -o "{out}\\%(title)s.%(ext)s" "{url}"'
os.system(command)
input("\nTekan Enter untuk keluar...")
