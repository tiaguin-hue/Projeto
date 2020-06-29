#Como não sabemos como funciona o touch decidimos botar uma escolhas escritas para testar o código
import uuid
from datetime import date
hj = date.today()
data = hj.weekday()
if data == 0:
    dia = "Segunda\n"
if data == 1:
    dia = "Terça\n"
if data == 2:
    dia = "Quarta\n"
if data == 3:
    dia = "Quinta\n"
if data == 4:
    dia = "Sexta\n"
if data == 5:
    dia = "Sabado\n"
if data == 6:
    dia = "Domingo\n"
professores = open("professores.txt", "r", encoding="utf8")
posicoes = professores.readlines()
professores.close()
opcao_0 = ""
notificacao = 0
notificacao_prof = 0
notificacao_alu = 0
codigo_0 = 0
presenca = 0
b = 0
d = 0
a = 0
c = 0
n = 0
f = 0
presentes = 0
codigo_aleatorio = ""
pessoa = ""
mensagem_prof = ""
chamadas = 0
mensagem_alu = ""
horario_p = []
horario_p_em_and = []
e = []
alunos_presentes = []
alunos_presenca = []
print("LOGIN")
email = input("Digite seu e-mail: \n")  # E-mail que a cesar disponibilizará para os alunos e professores
senha = input("Digite a sua senha: \n")  # A senha é o CPF do aluno e do professor
email_verificacao = email + "\n"
senha_verificacao = senha + "\n"
if email_verificacao in posicoes:
  for i in posicoes:
    if c == 2:
      if senha_verificacao == i:
        pessoa = "Professor Verificado"
      c += 1
    if c == 1:
      c += 1
      nome = i
    if email_verificacao == i:
      c += 1
if pessoa == "Professor Verificado":
  while b == 0:
    for i in posicoes:
        if i == nome:
            f += 1
        if f == 1:
            if 1 <= d < 5:
                horario_p.append(i)
                d += 1
            if i == dia:
                d += 1
    nome_p = nome.rstrip()
    print("\n\nOlá,", nome_p , "!\n\n")
    print("Chamadas em andamento:\n")
    for i in horario_p_em_and:
      print(i)
    print("Para hoje:\n")
    for i in horario_p:
      print(i)
    print("HISTÓRICO   AVISOS   HOME   MENSAGENS   PERFIL")
    opcao = input("")
    opcao_1 = opcao.title()
    opcao_01 = opcao_1.rstrip()
    a = 0
    if opcao_01 in horario_p:
        print("Você tem certeza de que quer fazer a chamada dessa turma?")
        print("\n\n")
        print("HISTÓRICO   AVISOS   HOME   MENSAGENS   PERFIL")
        opcao = input("")
        opcao_02 = opcao.upper()
        if opcao_02 == "HOME":
            break
        horario = input("Qual o horário a chamada será automaticamente encerrada:")
        def my_random_string(string_length=10):
            random = str(uuid.uuid4())
            random = random.upper()
            random = random.replace("-", "")
            return random[0:string_length]


        codigo_aleatorio = my_random_string(6)
        texto = opcao_01 + "\n" + codigo_aleatorio
        cod = open("codigo.txt", "a", encoding="utf8")
        cod.write(texto)
        cod.close()
        print("Seu código é:", codigo_aleatorio)
        # Como não sabiamos como colocar geolocalização, decidimos fazer apenas o código por enquanto
        horario_p_em_and.append(opcao_01)
        horario_p.remove(opcao_01)
        chamadas = chamadas + 1
        a = a + 1
    elif opcao_01 in horario_p_em_and:
        for i in alunos_presentes:
            print(i)
