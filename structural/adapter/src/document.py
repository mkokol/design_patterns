class Document:
    def __init__(self):
        self.title = ''
        self.body = ''

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    def __str__(self):
        return 'Title: {}\nBody: {}\n'.format(
            self.title,
            self.body
        )
