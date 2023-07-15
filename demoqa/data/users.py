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
