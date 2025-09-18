from PIL import Image
import pytesseract
import os
class ImageProc:
    _DATA_DIR_NAME = r"data/images"
    _WORKING_DIR = os.getcwd()
    _IMG_PATH = ''
    _IMG_FULLPATH = ''
    pytesseract.pytesseract.tesseract_cmd = r'D:\programs\Tesseract-OCR\tesseract.exe'
    def __init__(self, working_dir):
        if working_dir is not None:
            self._IMG_PATH = working_dir
        else:
            self._IMG_PATH = os.path.join(self._WORKING_DIR,"..",  self._DATA_DIR_NAME)

    def readImg(self, fileName):
        if fileName is None:
            print(f"Error: please provide a image name.")
            exit()
        else:
            self._IMG_FULLPATH = os.path.join(self._IMG_PATH, fileName)
        img = ''
        try:
            img = Image.open(self._IMG_FULLPATH)
            return pytesseract.image_to_string(img)
        except FileNotFoundError:
            print(f"Error: {img} not found. Please provide a valid image file.")
            exit()

    def readMultiImgs(self):
        all_entries = os.listdir(self._IMG_PATH)
        for entry in all_entries:
            full_path = os.path.join(self._IMG_PATH, entry)
            if os.path.isfile(full_path):
                text = self.readImg(entry)
                print(f"Content of {entry}:\n{text}\n")