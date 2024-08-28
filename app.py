from flask import Flask, render_template, request, redirect
from pet import create_connection, create_table, insert_pet, fetch_all_pets

app = Flask(__name__)

conn = create_connection()
create_table(conn)

@app.route('/')
def index():
  pets = fetch_all_pets(conn)
  return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
  if request.method == 'POST':
    nome = request.form['nome']
    idade = int(request.form['idade'])
    peso = float(request.form['peso'])
    insert_pet(conn, nome, idade, peso)
    return redirect('/')
  return render_template('add_pet.html')

if __name__ == '__main__':
  app.run(debug=True)