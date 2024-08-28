import sqlite3

def create_connection():
  conn = sqlite3.connect('pets.db', check_same_thread=False)
  return conn

def create_table(conn):
  try:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pets
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, peso REAL)''')
    conn.commit()
  except sqlite3.Error as e:
    print(f"Error creating table: {e}")
    
def insert_pet(conn, nome, idade, peso):
  try:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pets (nome, idade, peso) VALUES (?, ?, ?)", (nome, idade, peso))
    conn.commit()
  except sqlite3.Error as e:
    print(f"Error inserting pet: {e}")
    
def fetch_all_pets(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pets")
        pets = cursor.fetchall()
        return pets
    except sqlite3.Error as e:
        print(f"Error fetching pets: {e}")
        return []

def coletar_nome_pet():
  nome = input("Nome do pet: ")
  return nome

def coletar_idade_pet():
  while True:
    try:
      idade = int(input("Idade do pet (em anos): "))
      if idade < 0:
        print("A idade não pode ser negativa. Tente novamente.")
      else:
        return idade
    except ValueError:
      print("Por favor, insira um número válido para a idade.")
      
def coletar_peso_pet():
  while True:
    try:
      peso = float(input("Peso do pet (em kg): "))
      if peso < 0:
        print("O peso não pode ser negativo. Tente novamente.")
      else:
        return peso
    except ValueError:
      print("Por favor, insira um número válido para o peso.")
      
def exibir_informacoes_pet(nome, idade, peso):
  print("\nInformações do pet:")
  print(f"Nome: {nome}")
  print(f"Idade: {idade} anos")
  print(f"Peso: {peso} kg")