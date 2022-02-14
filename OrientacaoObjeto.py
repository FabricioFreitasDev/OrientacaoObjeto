
class tv:
    
    cor = 'preta'

    def __init__(self, tamanho):
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print('Canal Alterado para: {}'.format(novo_canal))

tv_sala = tv(tamanho=65)
tv_quarto = tv(tamanho=40)

tv_sala.mudar_canal('Yuotube')
tv_quarto.mudar_canal('Globo')

print(tv_sala.canal)
print(tv_quarto.canal)