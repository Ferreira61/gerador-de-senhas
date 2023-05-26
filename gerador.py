import random
import string

def gerar_senha(comprimento=8, incluir_letras=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ""
    
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
        
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def obter_preferencias():
    incluir_letras = input("Incluir letras na senha? (S/N): ").lower() == "s"
    incluir_numeros = input("Incluir números na senha? (S/N): ").lower() == "s"
    incluir_simbolos = input("Incluir símbolos na senha? (S/N): ").lower() == "s"
    
    return incluir_letras, incluir_numeros, incluir_simbolos

def solicitar_comprimento():
    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha: "))
            if comprimento <= 0:
                raise ValueError
            break
        except ValueError:
            print("Digite um valor válido (número inteiro positivo).")
    
    return comprimento

def main():
    comprimento = solicitar_comprimento()
    incluir_letras, incluir_numeros, incluir_simbolos = obter_preferencias()
    
    senha = gerar_senha(comprimento, incluir_letras, incluir_numeros, incluir_simbolos)
    
    print("Senha gerada:", senha)

if __name__ == "__main__":
    main()
