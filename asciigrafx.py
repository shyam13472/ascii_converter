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



def main():
    
    if len(sys.argv) < 2:
        print('Usage: python3 asciigrafx.py <path-to-videofile>')
    else:
        video_file = sys.argv[1]

        print('Welcome to ASCIIGRAFX Converter\nSHEG Enterprises Inc., All rights reserved\nUses ffmpeg ver. 5.1.2.\n')
        print(f'Videofile path: {video_file}')

        print('Extracting configfile...', end = '')
        conf = ASCIIGRAFXConfigFile('config')
        params = conf.getConfiguration()
        print('done')

        texturepackIndex = DEFAULT_TEXTUREPACK_INDEX if params['texturepack-index'] == 'def' else int(params['texturepack-index'])
        extractionFPS = DEFAULT_EXTRACTION_FPS if params['extraction-fps'] == 'def' else int(params['extraction-fps'])
        asciiCharHeight = DEFAULT_ASCII_CHAR_HEIGHT if params['ascii-pixel-char-height'] == 'def' else int(params['ascii-pixel-char-height'])
        print('Conversion parameters:')
        print('Video extraction FPS: %s\nASCII char height: %s\nTexturepack index of textures.txt %s' % (extractionFPS, asciiCharHeight, texturepackIndex))

        print('Extracting texturepack from textures.txt...', end='')
        with open('textures.txt' , 'r', encoding='utf8') as fitextures:
            texturepack = fitextures.readlines()[texturepackIndex]
        print('done')

        print(f'Loaded texturepack: {texturepack}')

        print('Beginning the conversion!')

        carver(video_file, extractionFPS)
        conventers(asciiCharHeight, texturepack)
        subprocess.check_output(["C:\\Users\\EgrZver\\Documents\\ffmpeg-5.1.2-full_build\\bin\\ffmpeg.exe", "-framerate", str(extractionFPS), "-i", f"{os.getcwd()}/processed/%07d.jpg", f"{video_file}-{extractionFPS}fps-{asciiCharHeight}h-processed.mp4"])
        shutil.rmtree("not_processed/")
        shutil.rmtree('processed/')

        print(f'Done! Output file is {video_file}-{extractionFPS}fps-{asciiCharHeight}h-processed.mp4')
    
    


if __name__ == "__main__":
    main()
