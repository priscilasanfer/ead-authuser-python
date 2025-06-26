import enum


class UserStatus(str, enum.Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
