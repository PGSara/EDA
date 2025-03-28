#________________________________________________________________________
#__ENUNCIADO__

'''Exercício 02

O problema que usaremos é bem conhecido e bastante simples. Queremos resolver uma equação de segundo grau, ou seja, dada a equação : 𝒂𝒙𝟐 + 𝒃𝒙 + 𝒄, queremos saber quais são as suas raízes reais, se elas existirem. Desta forma, resolva a função 2𝑥ˆ2 + 2𝑥 − 6.'''

#________________________________________________________________________
#__INÍCIO___

#Inportações:
import numpy as np
import matplotlib.pyplot as plt
import re

#Função para extrair a, b e c :
def extrair_coeficiente(equacao):
    # Remover espaços
    equacao = equacao.replace(" ", "")

    # Expressão regular para encontrar os coeficientes
    padrao = re.match(r"([+-]?\d*)x\^2([+-]\d*)x([+-]\d+)", equacao)

    if padrao:
        a = int(padrao.group(1)) if padrao.group(1) not in ["", "+", "-"] else int(padrao.group(1) + "1")
        b = int(padrao.group(2))
        c = int(padrao.group(3))
        return float(a), float(b), float(c)
    
    return None


# Função para calcular as raízes usando Bhaskara:
def calcular(a, b, c):
    delta = b**2 - 4 * a * c

    if delta < 0:
        return "Não há raízes reais"
    
    raiz = np.sqrt(delta)
    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)

    return x1, x2


# Definição da equação:
equacao = "2x^2 + 2x - 6"
a, b, c = extrair_coeficiente(equacao)
x1, x2 = calcular(a, b, c)


# Ajustar intervalo de x para incluir as raízes:
x_min = min(x1, x2) - 5 if x1 is not None and x2 is not None else -10
x_max = max(x1, x2) + 5 if x1 is not None and x2 is not None else 10
x = np.linspace(x_min, x_max, 400)
y = a * x**2 + b * x + c


# Criar o gráfico:
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'{equacao}', color='blue')
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)


# Mostrar raízes se existirem:
if x1 is not None and x2 is not None:
    plt.scatter([x1, x2], [0, 0], color='red', zorder=3, label='Raízes')
    plt.text(x1, 0, f'  x1={x1:.2f}', verticalalignment='bottom', color='red')
    plt.text(x2, 0, f'  x2={x2:.2f}', verticalalignment='bottom', color='red')

#Ajustando o grafíco: 
plt.xlabel("x")  
plt.ylabel("y")  
plt.legend()  
plt.grid(True)  
plt.title("Gráfico da Equação Quadrática") 
plt.show()

#__FIM!__
