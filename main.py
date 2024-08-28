import os
from pet import coletar_nome_pet, coletar_idade_pet, coletar_peso_pet, exibir_informacoes_pet, create_connection, create_table, insert_pet

def main():
    conn = create_connection()
    create_table(conn)
    
    if os.isatty(0):
        print("Por favor, insira as informações sobre seu pet.")
        nome = coletar_nome_pet()
        idade = coletar_idade_pet()
        peso = coletar_peso_pet()
        insert_pet(conn, nome, idade, peso)
    else:
        print("Running in non-interactive mode. Using default values.")
        nome = "DefaultPet"
        idade = 1
        peso = 5.0
        insert_pet(conn, nome, idade, peso)
    
    exibir_informacoes_pet(nome, idade, peso)

if __name__ == "__main__":
    main()
