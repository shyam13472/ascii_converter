class InvalidFileFormat(Exception): ...

class ASCIIGRAFXConfigFile:
    '''
    This class represents a config file for ASCIIGRAFX Converter
    The 1st string of it MUST BE config-file
    The config file contains these fields:
    extraction-fps
    ascii-pixel-char-height
    texturepack-index
    If a value is def then will be used a default value
    '''
    def __init__(self, pathToFile):

        self.__conf = {}

        with open(pathToFile, 'r', encoding='utf8') as inconf:
            lines = inconf.readlines()
            if lines[0][:-1] != 'config-file':
                raise InvalidFileFormat('The given file is not a config file. Extraction has been stopped')
            for i in range(1, 4):
                splitLine = lines[i].split(':')
                self.__conf[splitLine[0]] = splitLine[1][:-1] if splitLine[1][-1] == '\n' else splitLine[1]
    
    def getConfiguration(self):
        return self.__conf


