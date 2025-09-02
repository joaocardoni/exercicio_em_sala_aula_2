produtos = [
    {"nome": "Arroz", "preco": 25.90, "estoque": 100},
    {"nome": "Feijão", "preco": 8.75, "estoque": 200},
    {"nome": "Macarrão", "preco": 4.20, "estoque": 150}
]

for i in produtos:
    print(f"{i['nome']} - R${i['preco']} - Estoque: {i['estoque']}")