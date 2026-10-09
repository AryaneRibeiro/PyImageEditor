import cv2
import numpy as np

class Nitidez:

    def aplicarNitidez(self, imagem):
        kernel = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
        ])

        # Aplica o filtro de convolução
        nitidez = cv2.filter2D(imagem, -1, kernel)

        return nitidez