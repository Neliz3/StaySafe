from app.admin import admin
from app.public import form, public, payment
from app import app, db

app.register_blueprint(form.form)
app.register_blueprint(public.public)
app.register_blueprint(admin.admin, url_prefix='/admin')
app.register_blueprint(payment.payment, url_prefix='/payment')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5557)
