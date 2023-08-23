#Rotas do meu site
from flask import render_template, url_for, redirect
from shared import app, database, bcrypt
from shared.models import Usuario, Post
from flask_login import login_required, login_user, logout_user
from shared.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)


@app.route("/criar-conta", methods=["GET", "POST"])
def criaconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data, senha=senha, email=formcriarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", usuario=usuario.username))
    return render_template("criarconta.html", form=formcriarconta)


@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
