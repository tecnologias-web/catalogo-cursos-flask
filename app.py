import os
from flask import Flask
from database.carregador import carregar_dados


app = Flask(__name__)


from controllers import *


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
