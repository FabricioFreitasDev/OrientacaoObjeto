from FFBank import ContaCorrente, CartaoCredito

#programa
cliente_fabricio = ContaCorrente('Fabricio', '544.877.132-54', 1234, 54321)

cartao_fabricio = CartaoCredito('Fabricio', cliente_fabricio)

cartao_fabricio.senha = '12'
print(cartao_fabricio.senha)

print(cliente_fabricio.__dict__) #dict = dicionari, pega todas as informações.
print(cartao_fabricio.__dict__)