from enum import Enum


class TreatmentEnum(Enum):
    B = "Basic"
    H = "Hospital"


class StatusEnum(Enum):
    P = "Pending"
    A = "Approved"
    R = "Rejected"
