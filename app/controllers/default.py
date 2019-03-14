import datetime
from app import app, resp,db
from flask import render_template,flash,redirect,url_for
from app.models.forms import Contact
import app.models.tables as tbs

gradeChoices = [        ('1º Ano','1º Ano'),
                        ('2º Ano','2º Ano'),
                        ('3º Ano','3º Ano'),
                        ('4º Ano','4º Ano'),
                        ('5º Ano','5º Ano'),
                        ('6º Ano','6º Ano'),
                        ('7º Ano','7º Ano'),
                        ('8º Ano','8º Ano'),
                        ('9º Ano','9º Ano'),
                        ('1º Ensino Med.','1º Ensino Med.'),
                        ('2º Ensino Med.','2º Ensino Med.'),
                        ('3º Ensino Med.','3º Ensino Med.')]



@app.route("/home", methods=["GET","POST"])
def home():
    cnt = Contact()
    cnt.grade.choices = gradeChoices
    contactValidate(cnt)
    return render_template("index.html", notActive = True, form = cnt)

@app.route("/boas-praticas", methods=["GET","POST"])
def praticas():
    cnt = Contact()
    cnt.grade.choices = gradeChoices
    contactValidate(cnt)
    return render_template("praticas.html", notActive = True, form = cnt)

@app.route("/ferramentas-consumo", methods=["GET","POST"])
def consumo():
    cnt = Contact()
    cnt.grade.choices = gradeChoices
    contactValidate(cnt)
    return render_template("consumo.html", notActive = True, form = cnt)

@app.route("/ferramentas-criacao", methods=["GET","POST"])
def criacao():
    cnt = Contact()
    cnt.grade.choices = gradeChoices
    contactValidate(cnt)
    return render_template("criacao.html", notActive = True, form = cnt)

def contactValidate(cnt):
    if cnt.validate_on_submit():
        contact = tbs.Contact(email=cnt.email.data,
                    name=cnt.name.data,
                    age = cnt.age.data,
                    grade = cnt.grade.data,
                    message = cnt.message.data,
                    source = cnt.source.data)
        db.session.add(contact)
        db.session.commit()
        print("Added")
    else:
        print("Not added")
