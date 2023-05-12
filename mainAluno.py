from aluno import Aluno
a1 = Aluno("Bia", 19, 9, 0)  # obj da classe aluno
print(a1.name, a1.idade)
a2 = Aluno("Caio", 22, 4, 0)
print(a1.name, a1.idade)
a2.nota = 10.0
print(a2.nota)
