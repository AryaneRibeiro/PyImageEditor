class Historico:

    def __init__(self):
        self.historico = []

    def addHistorico(self, imagem):
        self.historico.append(imagem)

    def removerHistorico(self):
        if len(self.historico) > 0:
            self.historico.pop()
        else:
            print("Vc não editou a imagem")

    def imgAtual(self):
        return self.historico[-1]