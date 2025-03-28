#_____________________________________________________________
#__ENUNCIADO__

''' Exercício 01

Desenvolva um algoritmo que seja capaz de resolver um sistema de equações lineares abaixo 

$$
\ begin{cases}
y = 0.5x + 0.5 
y = -x + 2
\end{cases}
$$

Como resultado, sua saída devera apresentar o resultado do sistema de equações e plotar as equações, o ponto x,y '''

#_____________________________________________________________
#__INÍCIO___

# Importações:
import matplotlib.pyplot as plt
import numpy as np 
from  sympy import symbols, Eq, solve

# Definição de variaveis:
x, y = symbols('x y')


# Definições de equações:
eq1 = Eq(0.5*x + 0.5, y)
eq2 = Eq(-x +2, y)
 

# Resolução:
solucao = solve((eq1, eq2), (x, y))
x_intersecao = float(solucao[x])
y_intersecao = float(solucao[y])


# Gerar valores para eixo x:
x_vals = np.linspace(-10, 10, 70)

# Calcula os valores de Y para cada equação:
y1_vals = 0.5 * x_vals + 0.5
y2_vals = -x_vals + 2

plt.figure(figsize=(8,6))

# Plota as equações
plt.plot(x_vals, y1_vals, label="y = 0.5x + 0.5", color="blue")
plt.plot(x_vals, y2_vals, label="y = -x + 2", color="green")


# Plota o ponto de interseção
plt.scatter(x_intersecao, y_intersecao, color="black", zorder=3, label="Interseção")


# Adiciona linhas do eixo X e Y
plt.axhline(0, color="black", linewidth=1) 
plt.axvline(0, color="black", linewidth=1) 


# Rótulos e legenda
plt.xlabel("x")  
plt.ylabel("y")  
plt.legend()  
plt.grid(True)  
plt.title("Gráfico das Equações")  


# Mostra o gráfico
plt.show()

#FIM.__________________________________________________________________