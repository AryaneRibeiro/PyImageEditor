from core.imagem import Imagem
from filtro.filtros import Filtros

# Carrega a imagem
img = Imagem("/home/aryane/Documentos/programacao/python/editorImagens/images/entrada/parque.jpeg")  # coloque uma imagem existente
img.informacoesImagens()

# Aplica filtros
filtro = Filtros(img)
filtro.tonsCinza()
filtro.desfoque()

# Verifica e desfaz
img.modificacoesFeitas()
img.desfazer()
img.modificacoesFeitas()

# Salva
img.salvarImagem("minha_imagem_editada")