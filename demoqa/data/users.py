import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


@dataclasses.dataclass
class User2:
    full_name: str
    email: str
    current_address: str
    permanent_address: str
