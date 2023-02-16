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
            for i in range(1, len(lines)):
                line = lines[i]
                splitLine = (line[:line.find(':')], line[line.find(':') + 1:]) 
                self.__conf[splitLine[0]] = splitLine[1].rstrip()
    def getConfiguration(self):
        return self.__conf


