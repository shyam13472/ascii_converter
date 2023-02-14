from core.scripts.carver import carver
from core.scripts.handler import conventers
import os
import sys
import subprocess
import shutil

SAVING_FRAMES_PER_SECOND = 20
COMPRESSION = 5


def main():
    video_file = sys.argv[1]
    carver(video_file, SAVING_FRAMES_PER_SECOND)
    conventers(COMPRESSION)
    subprocess.check_output(["/usr/bin/ffmpeg", "-framerate", str(SAVING_FRAMES_PER_SECOND), "-pattern_type", "glob", "-i", f"{os.getcwd()}/processed/*.jpg", "out.mp4"])
    shutil.rmtree("not_processed/")
    shutil.rmtree('processed/')
    
    


if __name__ == "__main__":
    main()
