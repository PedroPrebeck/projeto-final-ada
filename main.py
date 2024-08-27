import os
from pet import coletar_nome_pet, coletar_idade_pet, coletar_peso_pet, exibir_informacoes_pet

def main():
    if os.isatty(0):
        print("Por favor, insira as informações sobre seu pet.")
        nome = coletar_nome_pet()
        idade = coletar_idade_pet()
        peso = coletar_peso_pet()
    else:
        print("Running in non-interactive mode. Using default values.")
        nome = "DefaultPet"
        idade = 1
        peso = 5.0
    
    exibir_informacoes_pet(nome, idade, peso)

if __name__ == "__main__":
    main()
