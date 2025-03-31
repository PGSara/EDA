'''
    4. Repita o processo até atingir a precisão desejada.

    Aplique esse método para encontrar este ponto na função:
    \[
    f(x) = x^3 - x - 2
    \]
    no intervalo \([1, 2]\) com uma precisão de \( 10^{-4} \).
'''

"""
    Encontra uma raiz da função f(x) no intervalo [a, b] usando o método da bisseção.
    
    Parâmetros:
    f : função - A função para a qual queremos encontrar a raiz.
    a, b : float - Os extremos do intervalo inicial, onde f(a) * f(b) < 0.
    tol : float - Tolerância para considerar que encontramos a raiz.
    max_iter : int - Número máximo de iterações.
    
    Retorna:
    float - A raiz aproximada da função f(x).
    
"""
#__________________________________________________________________________

#CÓDIGO:

# mesmo código do exercicio 3, so muda a precisão que agora é de -4 e o intervalo que agora está (1-2)
def bisection_method(f, a, b, tol=1e-4, max_iter=100):
    
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
    return x**3 - x - 2


raiz = bisection_method(f, 1, 2,)
print(f"Raiz encontrada: {raiz:.3f}")
