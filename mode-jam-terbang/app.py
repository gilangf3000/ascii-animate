import sys
import time
import os

def Animasi():
    folder = "frame"
    if not os.path.exists(folder):
        print(f"folder '{folder}' mboten ditemukan!")
        return

    frames = [
        {"jeneng_file": "1.txt", "wektu": 0.1},
        {"jeneng_file": "2.txt", "wektu": 0.1},
        {"jeneng_file": "3.txt", "wektu": 0.1},
        {"jeneng_file": "4.txt", "wektu": 0.1},
        {"jeneng_file": "5.txt", "wektu": 0.1},
        {"jeneng_file": "4.txt", "wektu": 0.1},
        {"jeneng_file": "3.txt", "wektu": 0.1},
        {"jeneng_file": "2.txt", "wektu": 0.1},
    ]

    while True:
        for frame in frames:
            frame_path = os.path.join(folder, frame["jeneng_file"])
            if os.path.exists(frame_path):
                with open(frame_path, "r") as f:
                    content = f.read()
                sys.stdout.write("\033c")  
                sys.stdout.write(content)
                sys.stdout.flush()
                time.sleep(frame["wektu"])

Animasi()