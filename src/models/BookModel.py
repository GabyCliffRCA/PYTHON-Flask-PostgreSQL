from database.db import get_connection
from .entities.BookEntity import Book

class BookModel():

    @classmethod
    def get_Books(self):
        try:
            connection = get_connection()
            books = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, author, genre, image, isbn, pages, publisher, subtitle, title, year FROM book ORDER BY year ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    bookResult = Book(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    books.append(bookResult.to_JSON())
            
            connection.close()
            return books

        except Exception as ex:
            raise Exception(ex)