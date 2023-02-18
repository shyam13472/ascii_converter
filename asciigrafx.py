from core.scripts.carver import carver
from core.scripts.handler import conventers
from core.configfile import ASCIIGRAFXConfigFile
import os, sys, subprocess, shutil, argparse
from sty import fg, rs
#import sty

DEFAULT_EXTRACTION_FPS = 30
DEFAULT_ASCII_CHAR_HEIGHT = 5
DEFAULT_TEXTUREPACK_INDEX = 0

class ConfigVerificationError(Exception): ...

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():

    os.system('') #! DO NOT DELETE!
    
    cls()

    infoMsg = fg.li_cyan + '[INFO]' + rs.fg
    appArgs = argparse.ArgumentParser(
        description='ASCIIGRAFX graphic converter. SHEG Enterprises Incorporated. All rights reserved.\nProcesses a video in a video in ASCII graphics.'
    )
    appArgs.add_argument('videoToProcess', type=str, help='A videofile to process into ASCII graphics')

    args = appArgs.parse_args()
    #if len(sys.argv) < 2:
    #    print('Usage: python3 asciigrafx.py <path-to-videofile>')
    #else:
    video_file = args.videoToProcess

    print('Welcome to ASCIIGRAFX Converter\nSHEG Enterprises Inc., All rights reserved\nUses ffmpeg (3rd-party software)\n')
    print(infoMsg + ' Running on ' + ('Windows' if os.name == 'nt' else 'Linux-like OS'))
    print(infoMsg + f' Videofile path: {video_file}')

    print(infoMsg + ' Extracting configfile...', end = '')
    conf = ASCIIGRAFXConfigFile('config')
    params = conf.getConfiguration()
    print('done')

    print(infoMsg + ' Verifying congifuration parameters...', end = '')
    for key in params.keys():
        if params[key] == '': 
            raise ConfigVerificationError('%s in the config file is null, value required' % (key))
    print('done')

    texturepackIndex = DEFAULT_TEXTUREPACK_INDEX if params['texturepack-index'] == 'def' else int(params['texturepack-index'])
    extractionFPS = DEFAULT_EXTRACTION_FPS if params['extraction-fps'] == 'def' else int(params['extraction-fps'])
    asciiCharHeight = DEFAULT_ASCII_CHAR_HEIGHT if params['ascii-pixel-char-height'] == 'def' else int(params['ascii-pixel-char-height'])
    ffmpegPath = params['ffmpeg-path']

    print(infoMsg + ' Conversion parameters:')
    print('%s Video extraction FPS: %s\n%s ASCII char height: %s\n%s Texturepack index in textures.txt: %s' % (infoMsg, extractionFPS, infoMsg, asciiCharHeight, infoMsg, texturepackIndex))
    print(infoMsg + f' FFMpeg location is at {ffmpegPath}')

    print(infoMsg + ' Extracting texturepack from textures.txt...', end='')
    with open('textures.txt' , 'r', encoding='utf8') as fitextures:
        texturepack = fitextures.readlines()[texturepackIndex]
    print('done')
    #out = 
    print(infoMsg + f' Loaded texturepack: {texturepack}')

    print('Beginning the conversion!')

    carver(video_file, extractionFPS)
    conventers(asciiCharHeight, texturepack)
    subprocess.check_output([ffmpegPath, "-framerate", str(extractionFPS), "-i", f"{os.getcwd()}/processed/%07d.jpg", f"{video_file}-{extractionFPS}fps-{asciiCharHeight}h-processed.mp4"])
    shutil.rmtree("not_processed/")
    shutil.rmtree('processed/')

    print(fg.li_green + 'Done!' + rs.fg + f' Output file is {video_file}-{extractionFPS}fps-{asciiCharHeight}h-processed.mp4')
    
    


if __name__ == "__main__":
    main()
