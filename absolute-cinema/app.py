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

    frames = [{"jeneng_file": f, "wektu": 1/30} for f in files]

    while True:
        start_time = time.time()
        for frame in frames:
            frame_path = os.path.join(folder, frame["jeneng_file"])
            if os.path.exists(frame_path):
                with open(frame_path, "r") as f:
                    content = f.read()
                sys.stdout.write("\033c")
                sys.stdout.write(content)
                sys.stdout.flush()

            elapsed_time = time.time() - start_time
            sleep_time = frame["wektu"] - elapsed_time if frame["wektu"] > elapsed_time else 0
            time.sleep(sleep_time)

            start_time = time.time()

Animasi()