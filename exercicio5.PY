"""Enunciado: Árvore Genealógica

Imagine que você recebeu a tarefa de criar uma árvore genealógica para uma família. A árvore deve ser capaz de armazenar informações sobre várias gerações de uma família e suas relações.

Requisitos:

Modelo de Dados:

Cada membro da família deve ser representado como um dicionário contendo: nome, idade, sexo e uma lista de filhos.
A lista de filhos de cada membro da família deve conter dicionários representando cada filho.
Funções a serem implementadas:

adicionar_membro(nome, idade, sexo, pai=None): Adiciona um membro à árvore genealógica. Se o pai for especificado, o membro é adicionado como filho desse pai.
buscar_membro(nome): Retorna o dicionário representando o membro da família com o nome especificado.
descendentes(nome): Retorna uma lista de todos os descendentes do membro com o nome especificado. Esta função deve ser implementada de forma recursiva.
Exemplo de Uso:

Adicione um membro chamado "João" com 70 anos.
Adicione um filho para "João" chamado "Carlos" com 50 anos.
Adicione um filho para "Carlos" chamado "Pedro" com 30 anos.
Adicione um filho para "Pedro" chamado "Lucas" com 10 anos.
Ao chamar a função descendentes("João"), ela deve retornar uma lista contendo "Carlos", "Pedro" e "Lucas".
Desafio Extra:

Implemente uma função antepassados(nome) que, dado o nome de um membro, retorna uma lista de todos os seus antepassados diretos (pai, avô, bisavô, etc.). Esta função também deve ser implementada de forma recursiva.
Este enunciado exige que o aluno utilize listas para armazenar os filhos de cada membro, dicionários para armazenar informações sobre cada membro e recursividade para buscar descendentes e antepassados.

"""

class ArvoreGenealogica:
    def __init__(self):
        self.membros = {}

    def adicionar_membro(self, nome, idade, sexo, pai=None):
        membro = {"nome": nome, "idade": idade, "sexo": sexo, "filhos": []}
        self.membros[nome] = membro

        if pai and pai in self.membros:
            self.membros[pai]["filhos"].append(membro)

    def buscar_membro(self, nome):
        return self.membros.get(nome, None)

    def listar_membros(self):
        return list(self.membros.keys())
    
    def descendentes(self, nome):
        membro = self.buscar_membro(nome)
        if not membro:
            return []
        lista_descendentes = []
        for filho in membro["filhos"]:
            lista_descendentes.append(filho["nome"])
            lista_descendentes.extend(self.descendentes(filho["nome"]))
        return lista_descendentes
    
    def antepassados(self, nome, lista_antepassados=None):
        if lista_antepassados is None:
            lista_antepassados = []
        for pai, membro in self.membros.items():
            if any(filho["nome"] == nome for filho in membro["filhos"]):
                lista_antepassados.append(pai)
                self.antepassados(pai, lista_antepassados)
        return lista_antepassados


#PROGRAMA:
arvore = ArvoreGenealogica()

print("Bem-vindo ao sistema de árvore genealógica")

while True:
    consulta = input("Você deseja cadastrar parentes ou consultar? (digite 'sair' para encerrar) ").strip().lower()
    
    if consulta == "sair":
        break
    
    elif consulta == "cadastrar":
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        sexo = input("Digite seu sexo: ")
        pai = input("Digite o nome do seu pai (ou deixe em branco se não houver): ").strip()
        
        arvore.adicionar_membro(nome, idade, sexo, pai if pai else None)
        print("Parente cadastrado com sucesso.")
        
        adicionar_filhos = input("Deseja cadastrar filhos para este membro? (sim/não) ").strip().lower()
        if adicionar_filhos == "sim":
            while True:
                nome_filho = input("Digite o nome do filho (ou 'sair' para parar): ").strip()
                if nome_filho.lower() == "sair":
                    break
                idade_filho = input(f"Digite a idade de {nome_filho}: ")
                sexo_filho = input(f"Digite o sexo de {nome_filho}: ")
                arvore.adicionar_membro(nome_filho, idade_filho, sexo_filho, nome)
                print(f"Filho {nome_filho} cadastrado com sucesso.")
    
    elif consulta == "consultar":
        print("Lista de membros cadastrados:")
        for membro in arvore.listar_membros():
            print(membro)
        
        nome = input("Digite o nome da pessoa que deseja consultar: ")
        print("Descendentes de", nome, ":", arvore.descendentes(nome))
        print("Antepassados de", nome, ":", arvore.antepassados(nome))
    
    else:
        print("Opção inválida! Digite 'cadastrar', 'consultar' ou 'sair'.")
