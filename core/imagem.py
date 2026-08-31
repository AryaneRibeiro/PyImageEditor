import cv2

from .historico import Historico
from .salvarImagem import SalvarImagem

class Imagem:
    def __init__(self, imagem):
        self.imagem = cv2.imread(imagem)

        if self.imagem is None:
            raise ValueError(f"Erro ao tentar encontrar imagem no caminho: {imagem}")

        self._historico = Historico(self.imagem)
        self._salvar = SalvarImagem()

    @property
    def imgAtual(self):
        return self._historico.atual

    def aplicarAlteracoes(self, imagemProcessada):
        self._historico.alterar(imagemProcessada)

    def desfazer(self):
        self._historico.desfazer()

    def informacoesImagens(self):
        x,y = self._historico.atual.shape[:2]
        print(f'Altura: {x}\nLargura: {y}')

    def salvarImagem(self, nomePasta):
        self._salvar.salvarImagem(self.imgAtual, nomePasta)

    def modificacoesFeitas(self):
        self._historico.modificacoesFeitas()
                
    '''def exibirImagem(self):
        cv2.imshow("Imagem original x Imagem modificada", self.historico[-1])
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''
