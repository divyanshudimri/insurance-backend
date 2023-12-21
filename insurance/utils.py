from datetime import date
from enum import Enum

from users.models import User


class PolicyTypes(Enum):
    PERSONAL_ACCIDENT = 'personal_accident'
    HEALTH = 'health'
    MOTOR_VEHICLE = 'motor_vehicle'

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


class PolicyStates(Enum):
    NEW = 'new'
    QUOTED = 'quoted'
    ACTIVE = 'active'

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]


def calculate_age(born: date) -> int:
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class PremiumCalculator:
    def __init__(self, customer: User, policy_type: PolicyTypes) -> None:
        self.customer = customer
        self.age = calculate_age(customer.date_of_birth)
        self.policy_type = policy_type

    def calculate_premium_and_cover(self) -> tuple[int, int]:
        """
        This method calculates premium and cover, using customer details and policy type
        return type: (premium, cover)
        Note: not using self.policy_type for now
        """
        if 20 <= self.age <= 30:
            return (10, 500000)
        if 30 <= self.age <= 40:
            return (20, 500000)
        if 40 <= self.age <= 50:
            return (30, 500000)
        if 50 <= self.age <= 60:
            return (40, 500000)
