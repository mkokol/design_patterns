from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Dict, List, Optional


class AbstractPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class ConcretePrototypeShallowCopy(AbstractPrototype):
    def __init__(
            self,
            int_val: int = 0,
            str_val: str = '',
            list_val: Optional[List] = None,
            dict_val: Optional[Dict] = None
    ):
        if list_val is None:
            list_val = []

        if dict_val is None:
            dict_val = {}

        self.int_val = int_val
        self.str_val = str_val
        self.list_val = list_val

        self.dict_val = dict_val

    def clone(self):
        return type(self)(
            self.int_val,
            self.str_val,
            self.list_val.copy(),
            self.dict_val.copy()
        )

    def __str__(self):
        return f'{id(self)}\t' \
               + f'int_val={self.int_val}\t' \
               + f'str_val={self.str_val}\t' \
               + f'list_val={self.list_val}\t' \
               + f'dict_val={self.dict_val}'


class ConcretePrototypeDeepCopy(AbstractPrototype):
    def __init__(
            self,
            int_val: int = 0,
            str_val: str = '',
            list_val: Optional[List] = None,
            dict_val: Optional[Dict] = None
    ):
        if list_val is None:
            list_val = []

        if dict_val is None:
            dict_val = {}

        self.int_val = int_val
        self.str_val = str_val
        self.list_val = list_val

        self.dict_val = dict_val

    def clone(self):
        return type(self)(
            self.int_val,
            self.str_val,
            deepcopy(self.list_val),
            deepcopy(self.dict_val)
        )

    def __str__(self):
        return f'{id(self)}\t' \
               + f'int_val={self.int_val}\t' \
               + f'str_val={self.str_val}\t' \
               + f'list_val={self.list_val}\t' \
               + f'dict_val={self.dict_val}'
