import enum


class UserType(str, enum.Enum):
    ADMIN = "admin"
    STUDENT = "student"
    INSTRUCTOR = "instructor"
