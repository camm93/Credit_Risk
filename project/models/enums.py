from enum import Enum


class LoanGrade(Enum):
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


class LoanTerm(Enum):
    _36_MONTHS = '36-month term'
    _60_MONTHS = '60-month term'


class PredictionModel(Enum):
    LOGISTIC_REGRESSION = 'Logistic Regression'
    NEURAL_NETWORK = 'Neural Network'
    RANDOM_FOREST = 'Random Forest'
