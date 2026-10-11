import cv2

class RepositorioImagem:

    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho)

        if self.imagem is None:
            raise ValueError("Erro ao enviar imagem")

        print("Imagem carregada com sucesso!")

    @classmethod
    def salvarImagem(cls, imagem):
        salvar = cv2.imwrite("images/resultados/img_01.jpg", imagem)

        if salvar:
            print("Imagem salva com sucesso!")
        else:
            print("Falhar ao salvar")
    
