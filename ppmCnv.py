import numpy as np
import cv2

class ppm:
    def __init__(self, filepath=''):
        self.file_path = str(filepath)
        self.stat = 'ok'
        self.STAT_OK = 'ok'
        self.STAT_FFE = 'ffe'
        self.STAT_FSE = 'fse'
        self.STAT_MCNE = 'mcne'
        self.file_format = ''
        self.file_text_size = ''
        self.file_width = -1
        self.file_height = -1
        self.file_max_color_size = -1
        self.headers_readed = False

    def readHeaders(self):
        with open(self.file_path, 'r') as file:
            self.file_format = file.readline()
            if self.file_format != 'P6\n':
                self.stat = self.STAT_FFE
                raise TypeError(f'File format: {self.file_format[:2]} is not allowed.')

            self.file_text_size = file.readline()
            try:
                width, height = self.file_text_size.split(sep=' ')
                self.file_width = int(width)
                self.file_height = int(height)
            except:
                self.stat = self.STAT_FSE
                raise TypeError('File size reading error.')

            self.max_color_size = file.readline()
            if self.max_color_size != '255\n':
                self.stat = self.STAT_MCNE
                raise TypeError(f'File max color number: {self.max_color_size[:-1]} is not allowed.')
            self.headers_readed = True

    def readFile(self):
        if not self.headers_readed:
            raise Warning('File headers not found! Try: <object>.readHeaders()')
        with open(self.file_path, 'rb') as file_data:
            for i in range(3):
                file_data.readline()
            data = file_data.read()

            img = np.zeros(self.file_width * self.file_height * 3, dtype='float32')
            for i in range(len(data) - 1):
                img[i] = data[i]
            img = img.reshape(self.file_height, self.file_width, 3)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return img

    def openImg(self, filepath=''):
        if filepath != '':
            self.file_path = filepath
        self.readHeaders()
        return self.readFile()
