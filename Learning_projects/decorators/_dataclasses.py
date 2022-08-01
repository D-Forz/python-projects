from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Deliver:
    street: str
    num: int = 0

@dataclass(eq=True, frozen=True)
class User:
    deliver: Deliver
    name: str
    last_name: str = None
    count: ClassVar[int] = 0

    def __post_init__(self):
        if not self.name:
            raise ValueError(f"Name cannot be empty: {self.name}")



deliver_one = Deliver("CL 50", 15)
user_one = User(deliver_one, "Juan", "Perez")
print(f"{user_one!r}")
print(f"Class Var: {User.count}")
print(f"instance variables: {user_one.__dict__}")
user_two = User(Deliver("CL 60", 10), "Juan", "Perez")
print(f"Equal objects? {user_one == user_two}")
collection = {user_one, user_two}