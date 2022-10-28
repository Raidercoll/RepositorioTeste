import matplotlib.pyplot as plt
from random import *


notas_aluno = []
for i in range(8):
    notas_aluno.append(randrange(0,11))

x = list(range(1,9))

plt.plot(notas_aluno, x)