from src.flyweight import FlyweightFactory, LetterFlyweight


class App:
    def __init__(self):
        self.text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' \
                    + ' Aenean commodo augue id sodales tristique.' \
                    + ' Vestibulum vel condimentum mauris.' \
                    + ' Praesent condimentum nulla sed felis auctor dictum.' \
                    + ' Integer maximus purus suscipit, lacinia nunc ornare, hendrerit turpis.' \
                    + ' Sed vehicula mi id nunc dictum, a feugiat tortor aliquet.'

    def run(self):
        flyweight_factory = FlyweightFactory()

        for letter in self.text:
            letter_flyweight: LetterFlyweight = flyweight_factory.get_letter(letter)
            letter_flyweight.render_letter()

        print('\n')
        print('Total letters count: {}'.format(len(self.text)))
        print('Total objects count: {}'.format(flyweight_factory.get_cache_size()))


if __name__ == '__main__':
    app = App()
    app.run()
