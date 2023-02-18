#rom app.admin import admin
from app.public import public
from app import app, db

app.register_blueprint(public.public)
#app.register_blueprint(admin.admin, url_prefix='/admin')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555)
