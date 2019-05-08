from enum import Enum


class DoctorSpecialties(Enum):
    IM = "Immunologist"
    CA = "Cardiologist"
    DE = "Dermatologist"
    GE = "Gastroenterologist"


class Gender(Enum):
    M = "Male"
    F = "Female"
