import cv2

class RepositorioImagem:

    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho)

        if self.imagem is None:
            raise ValueError("Erro ao enviar imagem")

        print("Imagem carregada com sucesso!")

    @classmethod
    def salvarImagem(self, imagem):
        salvar = cv2.imwrite("images/resultados/imagem.png", imagem)

        if salvar:
            print("Imagem salva com sucesso!")
        else:
            print("Falhar ao salvar")
    
