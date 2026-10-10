from editor.editor import Editor

imagem = Editor("images/entrada/imagem.png")

imagem.addFiltro()
# imagem.mostrarImagem()
print(f'Modificações: {imagem.modicacoes()}')

imagem.salvarImagem()