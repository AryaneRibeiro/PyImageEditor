import cv2

class Historico:

    def __init__(self):
        self.historico = []

    def adicionarImagem(self, imagem):
        self.historico.append(imagem)

    def desfazerAlteracao(self):
        if len(self.historico) > 0:
            self.historico.pop()
        else:
            print("Vc não editou a imagem")

    def obterImagemAtual(self):
        return self.historico[-1]

    def numeroModicacoes(self):
        return len(self.historico) - 1