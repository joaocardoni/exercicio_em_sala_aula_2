# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
# Em seguida, exiba apenas o nome do aluno

aluno={
    "nome": "Fulano",
    "idade": 12,
    "curso": "ESW"
}

print(aluno["nome"])

# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
# Depois, remova a chave "idade".

aluno.update({"nota":9.5})

aluno.pop("idade")

# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço:
# produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

for chave,valor in produtos.items():
    print(f"O produto {chave} custa {valor}")


# 4. Dado o dicionário aluno, verifique se existe a chave "curso".

if "curso" in aluno:
    print("Sim, existe a chave curso")
else:
    print("Não, não existe a chave curso")

# 5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome
# e nota.
# Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.

turma = {
    "Aluno1": 10,
    "Aluno2":9
}

chaves = list(turma.keys())
valores = list(turma.values())

print(f" O primeiro aluno se chama {chaves[0]} e a nota do segundo aluno foi {valores[1]}")


# 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
# a. Adicione ao dicionário do carro a chave 'cor'.
# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como
# valor).
# c. Acesse a nota de um dos alunos e exiba.
# d. Remova um aluno do dicionário de notas.


carro = { 
    "marca": "fiat",
    "modelo": "siena",
    "ano":2005,
}
carro.update({"cor":"branco"})

notas ={
    "aluno1" : 10,
    "aluno2" : 8,
    "aluno3" : 9
}
print(f"A nota do aluno1 foi {notas["aluno1"]}")

notas.pop("aluno2")