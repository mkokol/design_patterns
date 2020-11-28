from src.prototype import ConcretePrototypeDeepCopy, ConcretePrototypeShallowCopy


class App:
    @classmethod
    def run(cls):
        cls.run_shallow_copy()
        cls.run_deep_copy()

    @classmethod
    def run_shallow_copy(cls):
        concrete_prototype_shallow_copy_1 = ConcretePrototypeShallowCopy(
            1,
            'Obj Shallow Copy 1',
            [1, 2, 3],
            {'a': 1, 'b': 2, 'c': 3}
        )

        concrete_prototype_shallow_copy_2 = concrete_prototype_shallow_copy_1.clone()

        concrete_prototype_shallow_copy_1.list_val.append(4)
        concrete_prototype_shallow_copy_2.str_val = 'Obj Shallow Copy 2'

        print(concrete_prototype_shallow_copy_1)
        print(concrete_prototype_shallow_copy_2)

    @classmethod
    def run_deep_copy(cls):
        concrete_prototype_deep_copy_1 = ConcretePrototypeDeepCopy(
            1,
            'Obj A 1',
            [1, 2, 3],
            {'a': 1, 'b': 2, 'c': 3}
        )

        concrete_prototype_deep_copy_2 = concrete_prototype_deep_copy_1.clone()

        concrete_prototype_deep_copy_1.list_val.append(4)
        concrete_prototype_deep_copy_2.str_val = 'Obj A 2'

        print(concrete_prototype_deep_copy_1)
        print(concrete_prototype_deep_copy_2)


if __name__ == '__main__':
    app = App()
    app.run()
