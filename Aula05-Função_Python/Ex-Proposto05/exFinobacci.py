def fibonacci(n): # escreve a serie de Fibonacci ate n
 """Print a Fibonacci series up to n"""
 a, b = 0, 1
 
 while b < n:
    print(b)
    a, b = b, a+b

# Agora invoca a funçao que acabamos de definir
fibonacci(2000)
