from flask import Blueprint, render_template, request
from app.models import CreateWidget

public = Blueprint("public", __name__, static_folder="static", template_folder="templates")


@public.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        pass
    else:
        return render_template("public/index.html", values=CreateWidget.query.all())
