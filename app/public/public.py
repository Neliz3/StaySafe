from flask import Blueprint, render_template

public = Blueprint("public", __name__, static_folder="static", template_folder="templates")

@public.route("/")
@public.route("/home")
def home():
    return render_template("public/index.html")
