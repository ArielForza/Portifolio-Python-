# lista 
nomes = ["Ariel", "Duda", "Ana"]  # como criar

numeros = [20, 10, 12, 15]

primeiro = nomes[0]  # como pegar primeiro item (sempre começa em Zero)
print(primeiro)

nomes.append("Rafael")
print(nomes)


# Dicionarios
# pessoa = {"chave": "valor"}
pessoa = {"nome": "Ariel","idade": "31","peso": "80","cidade": "BH",}
peso = pessoa["peso"]
print(peso)

# como usar a estrutura. E deixar inteligente

lista_mensagens = []  # criando a lista

# mensagem1 = {"quem enviou": "user", "conteudo": "Mensagem"}
# mensagem2 = {"quem enviou": "assistant", "conteudo": "Resposta IA"}

mensagem1 = {"role": "user", "content": "Mensagem"}
mensagem2 = {"role": "assistant", "content": "Resposta IA"}

lista_mensagens.append(mensagem1)
lista_mensagens.append(mensagem2)

print(lista_mensagens)