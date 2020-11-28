from src.adapter import AdapterComposition, AdapterInheritance


class App:
    @classmethod
    def run(cls):
        adapter_inheritance: AdapterInheritance = AdapterInheritance(
            'Inheritance Title',
            'Inheritance Body'
        )
        print(adapter_inheritance.get_text())

        adapter_composition: AdapterComposition = AdapterComposition(
            'Composition Title',
            'Composition Body'
        )
        print(adapter_composition.get_text())


if __name__ == '__main__':
    app = App()
    app.run()
