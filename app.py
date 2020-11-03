import os
from admin.controllers import admin_bp
from flask import Flask
from database.carregador import carregar_dados
from website.controllers import website_bp


app = Flask(__name__)

app.register_blueprint(website_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')


if __name__ == '__main__':
    carregar_dados(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            'database'
        )
    )
    app.run(
        debug=True
    )
