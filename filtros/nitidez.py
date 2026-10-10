import cv2
import numpy as np

class Nitidez:

    def aplicar(self, imagem):
        ''' kernel = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
        ])'''
        kernel = np.array([
        [-1, 0, -1],
        [0,  5, 0],
        [-1, 0, -1]
        ])

        # Aplica o filtro de convolução
        nitidez = cv2.filter2D(imagem, -1, kernel)

        return nitidez