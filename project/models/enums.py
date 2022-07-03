from enum import Enum


class LoanRiskGrade(Enum):
    A = 'Grade A - Lowest'
    B = 'Grade B'
    C = 'Grade C'
    D = 'Grade D'
    E = 'Grade E'
    F = 'Grade F'
    G = 'Grade G - Highest'


class LoanPurpose(Enum):
    CAR = 'Car'
    CREDIT_CARD = 'Credit Card'
    DEBT_CONSOLIDATION = 'Debt Consolidation'
    HOME_IMPROVEMENT = 'Home Improvement'
    HOUSE = 'House'
    MAJOR_PURCHASE = 'Major Purchase'
    MEDICAL = 'Medical'
    MOVING = 'Moving'
    OTHER = 'Other'
    RENEWABLE_ENERGY = 'Renewable Energy'
    SMALL_BUSINESS = 'Small Business'
    VACATION = 'Vacation'
    WEDDING = 'Wedding'


class LoanStatus(Enum):
    CHARGED_OFF = 0
    FULLY_PAID = 1


class LoanTerm(Enum):
    _36_MONTHS = '36-month term'
    _60_MONTHS = '60-month term'


class PredictionModel(Enum):
    RANDOM_FOREST = 'Random Forest'
