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
                        ('3º Ensino Med.','3º Ensino Med.')][::-1]


@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    return contactValidateRender(template_name_or_list = "index.html", sideBarActive = False)


@app.route("/boas-praticas", methods=["GET","POST"])
def praticas():
    return contactValidateRender(template_name_or_list = "praticas.html", sideBarActive = True)
    

@app.route("/ferramentas-consumo", methods=["GET","POST"])
def consumo():
    return contactValidateRender(template_name_or_list = "consumo.html", sideBarActive = True)

@app.route("/ferramentas-criacao", methods=["GET","POST"])
def criacao():
    return contactValidateRender(template_name_or_list = "criacao.html", sideBarActive = True)

def contactValidateRender(**kwargs):
    cnt = Contact()
    cnt.grade.choices = gradeChoices
    kwargs["form"] = cnt
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
        return redirect("home")
    else:
        print("Not added")
        return render_template(**kwargs)
