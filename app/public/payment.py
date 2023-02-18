from flask import Blueprint, render_template, request, redirect, url_for
from app.models import CreateWidget

payment = Blueprint("payment", __name__, static_folder="static", template_folder="templates")

"""
@payment.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        pass
    else:
        query_params = request.args
        bank = query_params.get('bank') or 'default'
        return render_template("public/payment.html", bank=bank)

@payment.route('/payment', methods=['POST'])
def payment():
        return redirect(url_for('public.home'))
"""
