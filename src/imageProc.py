from PIL import Image
import pytesseract
import os
class ImageProc:
    _DATA_DIR_NAME = r"data"
    _WORKING_DIR = os.getcwd()
    _IMG_PATH = ''
    pytesseract.pytesseract.tesseract_cmd = r'D:\programs\Tesseract-OCR\tesseract.exe'
    def __init__(self, working_dir):
        if working_dir is not None:
            self._DATA_DIR_NAME = working_dir

    def readImg(self, fileName):
        if fileName is None:
            print(f"Error: please provide a image name.")
            exit()
        else:
            self._IMG_PATH = os.path.join(self._WORKING_DIR,"..",  self._DATA_DIR_NAME, fileName)
        img = ''
        try:
            img = Image.open(self._IMG_PATH)
            return pytesseract.image_to_string(img)
        except FileNotFoundError:
            print(f"Error: {img} not found. Please provide a valid image file.")
            exit()

