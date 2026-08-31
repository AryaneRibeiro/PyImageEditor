import cv2

class Historico:
    def __init__(self, imagem):
        self.historico = []
        self.historico.append(imagem.copy())

    @property
    def atual(self):
        return self.historico[-1]

    def alterar(self, imagemProcessada):
        self.historico.append(imagemProcessada)

    def modificacoesFeitas(self):
        print(f'Total de modficações feitas: {len(self.historico) - 1}')

    def desfazer(self):
        if len(self.historico) > 1:
            self.historico.pop()
            print("Ação realizada")
        else:
            print("Não há modificações para realizar")