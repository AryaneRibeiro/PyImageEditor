import cv2

class Historico:

    def __init__(self):
        self.historico = []

    def addHistorico(self, imagem):
        return self.historico.append(imagem)

    def removerHistorico(self):
        if len(self.historico) > 0:
            self.historico.pop()
        else:
            print("Vc não editou a imagem")

    def imgAtual(self):
        cv2.imshow("imagem", self.historico[-1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def qntDeModificacao(self):
        return len(self.historico) - 1