alunos = dict()

alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['nota'] = float(input('Digite a media do aluno: '))

if alunos['nota'] < 7:
    alunos['situacao'] = 'REPROVADO'
else:
    alunos['situacao'] = 'APROVADO'

print(f'A média de {alunos["nome"]} foi {alunos["nota"]} e ele está: {alunos["situacao"]} !!')