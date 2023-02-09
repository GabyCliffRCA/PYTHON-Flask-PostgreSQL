class Book():

    def __init__(self, id, author, genre, image, isbn, pages, publisher, subtitle, title, year):
        self.id = id
        self.author = author
        self.genre = genre
        self.image = image
        self.isbn = isbn
        self.pages = pages
        self.publisher = publisher
        self.subtitle = subtitle
        self.title = title
        self.year = year

    
    def to_JSON(self):
        return {
            'id' : self.id,
            'author' : self.author,
            'genre' : self.genre,
            'image' : self.image,
            'isbn' : self.isbn,
            'pages' : self.pages,
            'publisher' : self.publisher,
            'subtitle' : self.subtitle,
            'title' : self.title,
            'year' : self.year
        }