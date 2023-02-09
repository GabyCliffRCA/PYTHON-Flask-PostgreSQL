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

    
    @classmethod
    def get_Book(self, id):
        try:
            connection = get_connection()
            book = None

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, author, genre, image, isbn, pages, publisher, subtitle, title, year FROM book WHERE id=%s", (id,))
                row = cursor.fetchone()

                if row != None:
                    bookResult = Book(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    book = (bookResult.to_JSON())
            
            connection.close()
            return book

        except Exception as ex:
            raise Exception(ex)

    
    @classmethod
    def create_Book(self, newBook):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO book (author, genre, image, isbn, pages, publisher, subtitle, title, year) 
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (newBook.author,newBook.genre,newBook.image,newBook.isbn,newBook.pages,newBook.publisher,newBook.subtitle,newBook.title,newBook.year))
                affected_rows = cursor.rowcount
                print(affected_rows)
                connection.commit()
            
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update_Book(self, id, book):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE book SET author=%s, genre=%s, image=%s, isbn=%s, pages=%s, publisher=%s, subtitle=%s, title=%s, year=%s 
                    WHERE id = %s""", (book.author,book.genre,book.image,book.isbn,book.pages,book.publisher,book.subtitle,book.title,book.year, id))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete_Book(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM book WHERE id=%s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)