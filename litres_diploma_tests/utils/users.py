import dataclasses


@dataclasses.dataclass
class User:
    email: str
    password: str


def __init__(self, email, password):
    self.email = email
    self.password = password
