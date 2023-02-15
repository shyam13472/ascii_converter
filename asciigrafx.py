from core.scripts.carver import carver
from core.scripts.handler import conventers
from core.configfile import ASCIIGRAFXConfigFile
import os
import sys
import subprocess
import shutil

DEFAULT_EXTRACTION_FPS = 30
DEFAULT_ASCII_CHAR_HEIGHT = 5
DEFAULT_TEXTUREPACK_INDEX = 0

#SAVING_FRAMES_PER_SECOND = 30
#COMPRESSION = 5


def main():
    conf = ASCIIGRAFXConfigFile('config')
    params = conf.getConfiguration()
    #print(conf.getConfiguration())
    if len(sys.argv) < 2:
        print('Usage: python3 asciigrafx.py <path-to-videofile>')
    else:
        video_file = sys.argv[1]
        #video_compression = int(sys.argv[2])
        #video_out_fps = int(sys.argv[3])
        #texturepackIndex = 
        texturepackIndex = DEFAULT_TEXTUREPACK_INDEX if params['texturepack-index'] == 'def' else int(params['texturepack-index'])
        extractionFPS = DEFAULT_EXTRACTION_FPS if params['extraction-fps'] == 'def' else int(params['extraction-fps'])
        asciiCharHeight = DEFAULT_ASCII_CHAR_HEIGHT if params['ascii-pixel-char-height'] == 'def' else int(params['ascii-pixel-char-height'])
        with open('textures.txt' , 'r', encoding='utf8') as fitextures:
            texturepack = fitextures.readlines()[texturepackIndex]
        print(texturepack)
        print(params)
        carver(video_file, extractionFPS)
        conventers(asciiCharHeight, texturepack)
        subprocess.check_output(["C:\\Users\\EgrZver\\Documents\\ffmpeg-5.1.2-full_build\\bin\\ffmpeg.exe", "-framerate", str(extractionFPS), "-i", f"{os.getcwd()}/processed/%07d.jpg", f"{video_file}-{extractionFPS}fps-{asciiCharHeight}h-processed.mp4"])
        shutil.rmtree("not_processed/")
        shutil.rmtree('processed/')
    
    


if __name__ == "__main__":
    main()
