"""
____ENUNCIADO:

    Encontrando um ponto dentro de uma Função

    Como engenheiro de software voce recebeu a missão de encontrar o valor aproximado de \( x \) que faz com que uma determinada função \( f(x) \) seja igual a zero.

    Para isso, como explicado nas aulas anteriores você sabe que o valor deverá ser investigado dentro de um intervalo \([a, b]\), onde:

    - \( f(a) \) e \( f(b) \) possuem sinais opostos (um é positivo e o outro é negativo).

    O seu objetivo é criar um algoritmo que, a cada etapa, reduza esse intervalo até obter um valor de \( x \) com um erro aceitável.

    ## **Passos:**
    1. Escolha um ponto médio \( m \) entre \( a \) e \( b \).
    2. Avalie \( f(m) \).
    3. Se \( f(m) \) for suficientemente próximo de zero, pare. Caso contrário:
    - Se \( f(m) \) e \( f(a) \) tiverem sinais opostos, então a raiz está entre \( a \) e \( m \), e você deve descartar \( b \).
"""
#_________________________________________________________________________________________________________________

#EXPLICAÇÃO
"""
____MÉTODO DA BISSEÇÃO:

    O método da bisseção é um dos algoritmos mais simples e confiáveis para encontrar raízes de funções. Ele é baseado no Teorema do Valor Intermediário, que afirma que se uma função contínua 𝑓(𝑥) tem sinais opostos em dois pontos 𝑎 e 𝑏 
    f(a)⋅f(b)<0), então existe pelo menos uma raiz dentro desse intervalo.
"""

"""
____PASSOS DO MÉTODO DA BISSEÇÃO:
    
    Escolher um intervalo inicial [a,b][a, b][a,b] onde f(a) e f(b) tenham sinais opostos.

    Calcular o ponto médio:
    M = (a + 2) / (2)
    Avaliar f(m):

    Se f(m) for suficientemente próximo de zero ((m)∣< tolerância), então m é a raiz aproximada.
    Se f(m) e f(a) tiverem sinais opostos, a raiz está entre a e m → Atualiza b para m.

    Caso contrário, a raiz está entre m e b → Atualizaa para m.


    Repetir o processo até que o intervalo seja pequeno o suficiente ou o número máximo de iterações seja atingido.

"""
#_________________________________________________________________________________________________________________
"""
____EXPLICAÇÃO DA FUNÇÃO DO MÉTODO(CÓDIGO):

    Encontra uma raiz da função f(x) no intervalo [a, b] usando o método da bisseção.
    
    Parâmetros:
    f : função - A função para a qual queremos encontrar a raiz.
    a, b : float - Os extremos do intervalo inicial, onde f(a) * f(b) < 0.
    tol : float - Tolerância para considerar que encontramos a raiz.
    max_iter : int - Número máximo de iterações.
    
    Retorna:
    float - A raiz aproximada da função f(x).

"""
#________________________________________________________________________________________________________________
# CÓDIGO:

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
   
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
    
    for _ in range(max_iter):
        m = (a + b) / 2  # Ponto médio
        f_m = f(m)
        
        if abs(f_m) < tol:
            return m  # Encontramos a raiz aproximada
        
        if f(a) * f_m < 0:
            b = m  # A raiz está entre a e m
        else:
            a = m  # A raiz está entre m e b
    
    return (a + b) / 2  # Retorna a melhor estimativa após max_iter iterações

# Exemplo de uso
def f(x):
    return x**3 - 5*x - 7 

raiz = bisection_method(f, 2, 3)
print(f"Raiz encontrada: {raiz:.2f}")