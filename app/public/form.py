from flask import Blueprint, render_template, request, session, flash
from app.models import GetInfo
from app import db

form = Blueprint("form", __name__, static_folder="static", template_folder="templates")

@form.route("/form", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        text = request.form["text"]

        info = GetInfo(name, phone, email, text)
        db.session.add(info)
        db.session.commit()

        session.permanent = True
        session["name"] = name
        session["phone"] = phone
        session["email"] = email
        flash("Your message has been sent successfully")
        return render_template("public/forms.html", name=name, phone=phone, email=email)
    else:
        if "email" in session:
            name = session["name"]
            phone = session["phone"]
            email = session["email"]
            return render_template("public/forms.html", name=name, phone=phone, email=email)
        return render_template("public/forms.html")
