from src.document import Page, Paragraph, Sentence


class App:
    def __init__(self):
        paragraph1 = Paragraph()
        paragraph1.add(Sentence('Lorem ipsum dolor sit amet, consectetur adipiscing elit.'))
        paragraph1.add(Sentence('Aenean commodo augue id sodales tristique.'))
        paragraph1.add(Sentence('Vestibulum vel condimentum mauris.'))
        paragraph1.add(Sentence('Praesent condimentum nulla sed felis auctor dictum.'))
        paragraph1.add(Sentence('Integer maximus purus suscipit, lacinia nunc ornare, hendrerit turpis.'))
        paragraph1.add(Sentence('Sed vehicula mi id nunc dictum, a feugiat tortor aliquet.'))

        paragraph2 = Paragraph()
        paragraph2.add(Sentence('In bibendum, purus ut dictum lacinia, felis sapien eleifend ligula.'))
        paragraph2.add(Sentence('Nunc lorem nulla, rutrum quis elit nec, tristique accumsan ligula.'))
        paragraph2.add(Sentence('Pellentesque commodo finibus lectus.'))
        paragraph2.add(Sentence('Ut viverra odio in convallis porta. Nunc tincidunt justo vitae erat lacinia cursus.'))
        paragraph2.add(Sentence('Donec et nunc sit amet magna dictum efficitur at at diam.'))

        self.page: Page = Page()
        self.page.add(Sentence('Lorem Ipsum.'))
        self.page.add(paragraph1)
        self.page.add(paragraph2)

    def run(self):
        self.page.print_content()
        self.page.print_size()


if __name__ == '__main__':
    app = App()
    app.run()
