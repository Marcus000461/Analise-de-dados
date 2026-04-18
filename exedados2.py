def Calcular_Amplitude(A):
    vmax = max (A)
    vmin = min (A)
    amplitude = vmax - vmin
    return amplitude
alturas = []
while True:
    entrada = input("Digite as alturas dos alunos?: ")
    if entrada.lower() == 's':
        break
    try:
        altura = float(entrada)
        alturas.append(altura)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido ou 's' para parar.")
if len(alturas) > 0:
    amplitude = Calcular_Amplitude(alturas)
    print(f"A amplitude das alturas é: {amplitude}")
    print(f"A altura máxima é: {max(alturas)}")
    print(f"A altura mínima é: {min(alturas)}")
else:
    print("\nNenhuma altura foi inserida para o cálculo da amplitude.")
        