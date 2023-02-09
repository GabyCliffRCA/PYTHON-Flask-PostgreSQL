from flask import Flask, render_template
from config import config

#ROUTES IMPORTS
from routes import Book
from routes import User

app=Flask(__name__)


def error_not_found_404(error):
    return "<h1>ERROR 404 - Page Not Found</h1>", 404


if __name__=='__main__':
    #APP BLUEPRINTS
    app.register_blueprint(Book.main, url_prefix='/api/books')
    app.register_blueprint(User.main, url_prefix='/api/users')
    
    #APP ERROR HANDLER
    app.register_error_handler(404, error_not_found_404)

    #APP RUN
    app.config.from_object(config['development'])
    app.run(port=4000)