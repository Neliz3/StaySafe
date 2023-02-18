from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import CreateWidget
from app import db

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        name = request.form["name"]
        url = request.form["url"]
        text = request.form["text"]
        number = request.form["number"]
        mono = request.form["mono"]
        privat = request.form["privat"]

        new_widget = CreateWidget(name, url, text, number, mono, privat)
        db.session.add(new_widget)
        db.session.commit()

        flash("Widget was created successfully")
        return redirect(url_for("public.home"))
    else:
        return render_template("admin/admin.html")
