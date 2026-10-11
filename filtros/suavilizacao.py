from filtros.filtro import Filtro

import cv2

class Suavalizacao(Filtro):

    def aplicar(self, imagem):
        suavizada = cv2.blur(imagem, (5, 5))
        return suavizada
    