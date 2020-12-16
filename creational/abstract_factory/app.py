import argparse

from src.client import Client


class App():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--type', '-t',
            required=True,
            help='1 and 2 product type are available.',
            choices=['1', '2']
        )
        args = parser.parse_args()
        self.client = Client(int(args.type))

    def run(self):
        print(self.client.get_name())
        print(self.client.get_content())


if __name__ == '__main__':
    app = App()
    app.run()
