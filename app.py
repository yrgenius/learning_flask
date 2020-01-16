from flask import Flask
from config import Configurauion

from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Configurauion)

app.register_blueprint(posts, url_prefix='/blog')

#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
