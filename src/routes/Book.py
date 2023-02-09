from flask import Blueprint, jsonify, request
import uuid

#MODELS
from models.BookModel import BookModel
#ENTITY
from models.entities.BookEntity import Book

main = Blueprint("book_blueprint", __name__)

@main.route('/', methods = ['GET'])
def getBooks():
    try:
        books = BookModel.get_Books()
        return jsonify(books)
    except Exception as ex:
        return jsonify({"message": str(ex)}),500


@main.route('/<id>', methods = ['GET'])
def getBook(id):
    try:
        book = BookModel.get_Book(id)

        if book != None:
            return jsonify(book)
        else:
            return jsonify({"message": "Book not found"}),404
        
    except Exception as ex:
        return jsonify({"message": str(ex)}),500


@main.route('/create', methods = ['POST'])
def creatBook():
    try:
        author = request.json['author']
        genre = request.json['genre']
        image = request.json['image']
        isbn = request.json['isbn']
        pages = int(request.json['pages'])
        publisher = request.json['publisher']
        subtitle = request.json['subtitle']
        title = request.json['title']
        year = request.json['year']
        print(request.json)

        newBook = Book(None,author,genre,image,isbn,pages,publisher,subtitle,title,year)
        affected_rows = BookModel.create_Book(newBook)

        if affected_rows == 1:
            return jsonify({"message":"Book created successfully"}),201
        else:
            return jsonify({"message":"Error in Book create operation"}),500
    
    except Exception as ex:
        return jsonify({"message": str(ex)}),500


@main.route('/update/<id>', methods = ['PUT'])
def updateBook(id):
    try:
        author = request.json['author']
        genre = request.json['genre']
        image = request.json['image']
        isbn = request.json['isbn']
        pages = int(request.json['pages'])
        publisher = request.json['publisher']
        subtitle = request.json['subtitle']
        title = request.json['title']
        year = request.json['year']
        print(request.json)

        book = Book(None,author,genre,image,isbn,pages,publisher,subtitle,title,year)
        affected_rows = BookModel.update_Book(id, book)

        if affected_rows == 1:
            return jsonify({"message":"Book updated successfully"}),201
        else:
            return jsonify({"message":"Error in Book update opration"}),500
    
    except Exception as ex:
        return jsonify({"message": str(ex)}),500


@main.route('/delete/<id>', methods = ['DELETE'])
def deleteBook(id):
    try:
        affected_rows = BookModel.delete_Book(id)

        if affected_rows == 1:
            return jsonify({"message":"Book deleted successfully"}),200
        else:
            return jsonify({"message":"Error in Book delete operation"}),500

    except Exception as ex:
        return jsonify({"message": str(ex)}),500       