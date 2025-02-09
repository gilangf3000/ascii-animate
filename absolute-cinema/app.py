import sys
import time
import os
import re

def Animasi():
    folder = "frame"
    if not os.path.exists(folder):
        print(f"Folder '{folder}' tidak ditemukan!")
        return

    files = sorted(
        [f for f in os.listdir(folder) if f.endswith(".txt")],
        key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0
    )

    total_frames = len(files)

    if total_frames == 0:
        print("Tidak ada file .txt di dalam folder frame!")
        return

    print(f"Total frame ditemukan: {total_frames}")

    # **Membaca semua frame terlebih dahulu ke dalam memori**
    frames = []
    for f in files:
        frame_path = os.path.join(folder, f)
        with open(frame_path, "r") as file:
            frames.append(file.read())

    frame_time = 1 / 30  # **30 FPS**
    
    while True:
        start_time = time.perf_counter()  # **Gunakan perf_counter untuk akurasi lebih tinggi**
        for content in frames:
            sys.stdout.write("\033[H")  # **Lebih cepat daripada "\033c"**
            sys.stdout.write(content)
            sys.stdout.flush()

            elapsed_time = time.perf_counter() - start_time
            sleep_time = frame_time - elapsed_time
            if sleep_time > 0:
                time.sleep(sleep_time)

            start_time = time.perf_counter()  # **Reset waktu untuk frame berikutnya**

Animasi()