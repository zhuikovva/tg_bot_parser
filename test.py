from dataclasses import dataclass

@dataclass
class Person:

    name: str
    age: int
    e_mail: str


def get_user_info(person: Person) -> str:
    return f'Name: {person.name}, age: {person.age}, e-mail: {person.e_mail}'


print(get_user_info(Person('Max', 25, 'max@ya.ru')))
