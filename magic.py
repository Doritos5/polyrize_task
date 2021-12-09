from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class MagicList(object):
    def __init__(self, cls_type: callable):
        self._cls_type = cls_type
        self._inner_list = list()
        self._list_len = len(self._inner_list)

    def __setitem__(self, key: int, value) -> None:
        if key > self._list_len:
            raise IndexError("Can't add non sequential numbers")

        elif key < self._list_len:  # Exists in list
            self._inner_list[key] = self._cls_type(value)
            return

        # Not exists in list but sequential
        self._inner_list.append(self._cls_type(value))
        self._list_len += 1

    def __repr__(self) -> str:
        return str(self._inner_list)

    def __getitem__(self, item: int) -> str:
        return self._inner_list[item]


a = MagicList(cls_type=Person)
a[0] = 5
a[1] = 7
a[2] = 7
a[3] = 7
a[2] = 9
print(a)
print(a[0])

# Output:
# [Person(age=5), Person(age=7), Person(age=9), Person(age=7)]
# Person(age=5)
