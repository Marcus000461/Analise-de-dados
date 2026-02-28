def CalcularAmplitude(A):
    vmax = max (A)
    vmin = min (A)
    amplitude = vmax - vmin
    return amplitude
while True:
    alturas_usuario = float(input("Digite as alturas que você deseja: "))
    alturas = [160,165,180,195,200]
    resposta = input("Você quer adicionar mais alturas? (s/n): ")
    print("Nota adicionada:", resposta)
    amplitudetotal = CalcularAmplitude(alturas)
    print(f"Amplitude total das alturas é de {amplitudetotal} cm.  ")
    
