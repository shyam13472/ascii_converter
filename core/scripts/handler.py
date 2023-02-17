import os
import re
from progress.bar import IncrementalBar
from core.scripts.ascii import conventer


def conventers(compression, texturepack):
    images = [img for img in os.listdir('not_processed') if img.endswith(".jpg")]
    images.sort(key=lambda f: int(re.sub('\D', '', f)))
    bars = IncrementalBar('Processing frames into ASCII', max=len(images) )
    for index, filename in enumerate(images):
        f = os.path.join(os.getcwd(), 'not_processed', filename)
        if os.path.isfile(f):

            conventer(f, index, texturepack, compression)
            bars.next()
    bars.finish()