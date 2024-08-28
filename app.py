from flask import Flask, render_template, request, redirect, flash
from pet import create_connection, create_table, insert_pet, fetch_all_pets

app = Flask(__name__)
app.secret_key = "supersecretkey"

conn = create_connection()
create_table(conn)


@app.route("/")
def index():
    pets = fetch_all_pets(conn)
    return render_template("index.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip().capitalize()
        idade = request.form.get("idade", "").strip()
        peso = request.form.get("peso", "").strip()

        if not nome:
            flash("Nome do pet é obrigatório.", "danger")
            return redirect("/add")

        try:
            idade = int(idade)
            if idade < 0:
                flash("Idade não pode ser negativa.", "danger")
                return redirect("/add")
        except ValueError:
            flash("Idade deve ser um número inteiro.", "danger")
            return redirect("/add")

        try:
            peso = float(peso)
            if peso < 0:
                flash("Peso não pode ser negativo.", "danger")
                return redirect("/add")
        except ValueError:
            flash("Peso deve ser um número decimal.", "danger")
            return redirect("/add")

        insert_pet(conn, nome, idade, peso)
        return redirect("/")

    return render_template("add_pet.html")


if __name__ == "__main__":
    app.run(debug=True)
