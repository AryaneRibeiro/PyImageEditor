from editor.editor import Editor

imagem = Editor()
imagem.lerImagem("images/entrada/img_02.jpg")

imagem.addFiltro()
print(f'Modificações: {imagem.nModificacoes()}')
imagem.visualizarImagem()
imagem.salvarImagem()
