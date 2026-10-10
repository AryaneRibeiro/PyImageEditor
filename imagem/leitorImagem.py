import cv2

class LeitorImagem:

    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho)

        if self.imagem is None:
            raise ValueError("Erro ao enviar imagem")

        print("Imagem carregada com sucesso!")
