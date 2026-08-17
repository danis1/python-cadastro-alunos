#Daniela Feitoza Alves
#DSM - Vespertino 3° Ciclo
#Fatec Praia Grande

#Desenvolvimento de Software 3 - Exercício em Python - Lista, Tupla e Coleções


# Cadastrar alunos


print("=====* Bem Vindo ao cadastro de alunos *=====")

#variáveis do aluno
listaAluno = []
dicionarioAluno = {}
listaDisciplina = set()
listaNotaAluno = []

#variáveis da turma
tuplaTurma = ("Administração", 2026, "3a1")

while 1:
    menu = int(input("\nSelecione a opção desejada: \n 1 - Cadastrar aluno, disciplinas e notas \n 2 - Listar dados da Turma \n 3 - Sair\n\n"))

    if menu == 1:
        # Solicitar nome, idade e cidade.
        # Armazenar os dados de cada aluno.
        nome = str(input("\nDigite o nome do aluno(a): "))
        idade = int(input("Digite a idade do aluno(a): "))
        cidade = str(input("Digite a cidade do aluno(a): "))


        print("\n=== Cadastrar Disciplinas e Notas do aluno =====\n")
        # Registrar notas
        # Permitir adicionar uma ou mais notas para cada aluno.
        # Armazenar as notas em uma lista.
        # Registrar disciplinas
        # Criar uma coleção para armazenar as disciplinas disponíveis.
        # Utilizar um conjunto (set), garantindo que uma mesma disciplina não seja cadastrada mais de uma vez.

        listaNotaAluno = []
        continuarDisciplinaNota = 1
        while continuarDisciplinaNota == 1:
            disciplina = str(input("Digite a disciplina que deseja cadastrar: "))
            listaDisciplina.add(disciplina)

            nota = float(input("Digite a nota que deseja cadastrar: "))
            listaNotaAluno.append(nota)

            continuarNota = int(input("\n===== Continuar adicionando?:  \n 1 - Sim \n 2 - Não\n\n"))
            if continuarNota == 2:
                break

        # Calcular a média
        soma = 0
        media = 0.0
        resultado = " "

        if len(listaNotaAluno) <= 0:
            print("Não é possível dividir por zero")
        else:
            for nota in listaNotaAluno:
                soma += nota
            media = soma / len(listaNotaAluno)
            if media < 5:
                resultado = "Reprovado"
            else:
                 resultado = "Aprovado"

        # Informar se o aluno está aprovado ou reprovado.
        # Utilizar um dicionário para organizar os dados de cada aluno.
        # Utilizar uma lista para armazenar os alunos.
        # Exibir dados do aluno cadastrado
        print("\n======== Dicionario do Aluno Cadastrado =========\n")
        dicionarioAluno = {
            "Nome": nome,
            "Idade": idade,
            "Cidade": cidade,
            "Disciplinas": listaDisciplina,
            "Notas": listaNotaAluno,
            "Media": media,
            "Resultado": resultado
        }
        listaAluno.append(dicionarioAluno)

        for chave, valor in dicionarioAluno.items():
            print(chave, ":", valor) 

    elif menu == 2:
        print("\n===== 2 - Dados da Turma (tupla) =====\n")
        # Listar dados da turma
        # Armazenar informações fixas da turma, como nome do curso e ano.
        # Utilizar uma tupla, demonstrando uma situação em que os dados não precisam ser alterados.
        # Informar dados da turma
        print("Informações da Turma: \n")
        print(tuplaTurma)

        # Listar disciplinas
        print("\nTodas as disciplinas: \n")
        print(listaDisciplina)

        # Listar alunos
        # Exibir todos os alunos cadastrados e suas informações.
        print("\n==== Lista de Alunos Cadastrados ====\n")
        somaMediasTurma = 0
        totalAvaliados = 0

        for aluno in listaAluno:
            for chave, valor in aluno.items():
                print(chave, ":", valor)
            print("\n--------\n")  


        # Calcular a média geral da turma
        print("\n===== Média Geral da Turma =====\n")
        if len(listaAluno) <= 0:
            print("Não é possível dividir por zero (nenhum aluno cadastrado)")
        else:
            somaMediasTurma = 0
            for aluno in listaAluno:
                somaMediasTurma += aluno["Media"]
            mediaTurma = somaMediasTurma / len(listaAluno)
            print("Média da Turma:", mediaTurma)

    elif menu == 3:
        print("\n============ FIM ========== ")
        break

    else:
        print("Inválido\n")
