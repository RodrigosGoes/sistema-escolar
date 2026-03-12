import datetime

# TUPLA (imutável) 
CONFIG = ("Sistema Escolar", "1.0")

# FUNÇÃO 
def calcular_media(notas): 
    return sum(notas) / len(notas)

# CLASSE (orientação a objetos)
class Aluno: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 
        self.notas = [] 

    def adicionar_nota(self, nota): 
        self.notas.append(nota)

    def media(self): 
        if len(self.notas) == 0: 
            return 0 
        return calcular_media(self.notas)
     
# DICIONÁRIO 
alunos = {} 

# SET (evitar nomes repetidos) 
nomes_unicos = set()

# Salvar arquivos
def salvar_arquivo(): 
    with open("alunos.txt", "w") as arquivo: 
        for nome, aluno in alunos.items(): 
            linha = f"{aluno.nome},{aluno.idade},{aluno.notas}\n" 
            arquivo.write(linha) 
    print("Arquivo salvo com sucesso!") 

# Carregar arquivos
def carregar_arquivo(): 
    try: 
        with open("alunos.txt", "r") as arquivo: 
            for linha in arquivo: 
                nome, idade, notas = linha.strip().split(",", 2) 
                aluno = Aluno(nome, int(idade))
                aluno.notas = eval(notas) 
                alunos[nome] = aluno 
                nomes_unicos.add(nome)
            print("Arquivo carregado!") 

    except: 
        print("Arquivo ainda não existe.")
    

print(CONFIG[0], "versão", CONFIG[1]) 
print("Data:", datetime.datetime.now())

carregar_arquivo() 
    
while True: 
    print("\n===== MENU =====") 
    print("1 - Cadastrar aluno") 
    print("2 - Listar alunos") 
    print("3 - Buscar aluno") 
    print("4 - Salvar dados") 
    print("5 - Sair") 
    opcao = input("Escolha: ") 
    if opcao == "1": 
        nome = input("Nome: ")

        if nome in nomes_unicos: 
            print("Aluno já cadastrado!") 
            continue 

        try: 
            idade = int(input("Idade: ")) 
        except: 
            print("Idade inválida") 
            continue 

        aluno = Aluno(nome, idade)

        for i in range(3):
            while True:

                try: 
                    nota = float(input(f"Nota {i+1}: ")) 
                except: 
                    print("Digite número válido") 
                    continue 
                if nota < 0 or nota > 10: 
                    print("Nota inválida") 
                    continue 
                aluno.adicionar_nota(nota) 
                break

        alunos[nome] = aluno 
        nomes_unicos.add(nome) 

        print("Aluno cadastrado!")

    elif opcao == "2":
        if len(alunos) == 0: 
            print("Nenhum aluno cadastrado") 
            continue

        for nome, aluno in alunos.items(): 
            print("\nNome:", aluno.nome) 
            print("Idade:", aluno.idade) 
            print("Notas:", aluno.notas) 
            print("Média:", aluno.media()) 

    elif opcao == "3":
        busca = input("Digite o nome do aluno: ") 
        if busca in alunos: 
            aluno = alunos[busca] 
            print("Nome:", aluno.nome) 
            print("Idade:", aluno.idade) 
            print("Notas:", aluno.notas) 
            print("Média:", aluno.media())
        else: print("Aluno não encontrado!")

    elif opcao == "4": 
        salvar_arquivo()

    elif opcao == "5":
        print("Encerrando sistema...") 
        break
    else: print("Opção inválida")
    