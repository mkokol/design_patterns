from src.builder import AbstractBuilder


class Director:
    def __init__(self, builder: AbstractBuilder):
        self._builder = builder

    def construct(self):
        return self._builder \
            .set_title('Title') \
            .set_description('Description') \
            .set_text('Text') \
            .build()
