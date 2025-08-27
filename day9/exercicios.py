'''
Programa de Avaliação

Você tem acesso a um banco de dados de student_scores no formato de um dicionário. As chaves em student_scores são os nomes dos alunos e os valores são suas notas nas provas.
Escreva um programa que converta suas notas em conceitos.
Ao final do seu programa, você deverá ter um novo dicionário chamado student_grades, que deverá conter os nomes dos alunos como chaves e suas notas avaliadas como valores.
A versão final do dicionário student_grades será verificada.
**NÃO** modifique as linhas 1 a 7 para alterar o dicionário student_scores existente.
Este é o critério de pontuação:

- Notas 91 - 100: Nota = "Excelente"
- Notas 81 - 90: Nota = "Excede as Expectativas"
- Notas 71 - 80: Nota = "Aceitável"
- Notas 70 ou menos: Nota = "Reprovado"
'''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for aluno in student_scores:
    nota = student_scores[aluno]
    if nota > 90:
        student_grades[aluno] = "Outstanding"
    elif nota > 80:
        student_grades[aluno] = "Exceeds Expectations"
    elif nota > 70:
        student_grades[aluno] = "Acceptable"
    else:
        student_grades[aluno] = "Fail"

print(student_grades)
