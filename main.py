from core.scripts.carver import carver
from core.scripts.handler import conventers
import os
import sys
import subprocess
import shutil

SAVING_FRAMES_PER_SECOND = 30
COMPRESSION = 5


def main():
    if len(sys.argv) < 2:
        print('Usage:python main.py <in-video> <compression> <framerate> <textures>')
    else:
        video_file = sys.argv[1]
        video_compression = int(sys.argv[2])
        video_out_fps = int(sys.argv[3])
        texturepack = ''
        with open(sys.argv[4], 'r', encoding='utf8') as fitextures:
            texturepack = fitextures.readlines()[0]
        print(texturepack)
        carver(video_file, video_out_fps)
        conventers(video_compression, texturepack)
        subprocess.check_output(["C:\\Users\\EgrZver\\Documents\\ffmpeg-5.1.2-full_build\\bin\\ffmpeg.exe", "-framerate", str(SAVING_FRAMES_PER_SECOND), "-i", f"{os.getcwd()}/processed/%07d.jpg", f"{video_file}-processed.mp4"])
        shutil.rmtree("not_processed/")
        shutil.rmtree('processed/')
    
    


if __name__ == "__main__":
    main()
