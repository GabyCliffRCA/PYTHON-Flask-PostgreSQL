from flask import Blueprint, jsonify

#DATABASE
from models.BookModel import BookModel

main = Blueprint("book_blueprint", __name__)

@main.route('/')
def getBooks():
    try:
        books = BookModel.get_Books()
        return jsonify(books)
    except Exception as ex:
        return jsonify({"message": str(ex)}),500