from typing import Optional


class Title:
    def __init__(self, title: str = ''):
        self.title = title

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    def __str__(self) -> str:
        return self.title


class Description:
    def __init__(self, description: str = ''):
        self.description = description

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = description

    def __str__(self) -> str:
        return self.description


class Text:
    def __init__(self, text: str = ''):
        self.text = text

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text

    def __str__(self) -> str:
        return self.text


class Document:
    def __init__(self):
        self.title: Optional[Title] = None
        self.description: Optional[Description] = None
        self.text: Optional[Text] = None

    @property
    def title(self) -> Title:
        return self.__title

    @title.setter
    def title(self, title: Title) -> None:
        self.__title = title

    @property
    def description(self) -> Description:
        return self.__description

    @description.setter
    def description(self, description: Description) -> None:
        self.__description = description

    @property
    def text(self) -> Text:
        return self.__text

    @text.setter
    def text(self, text: Text) -> None:
        self.__text = text

    def __str__(self):
        doc_str = []

        if self.title:
            doc_str.append(str(self.title))

        if self.description:
            doc_str.append(str(self.description))

        if self.text:
            doc_str.append(str(self.text))

        return '\n'.join(doc_str)
