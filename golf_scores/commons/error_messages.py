from enum import Enum

class ErrorMessage(Enum):
    PASSWORDS_DONT_MATCH = "Passwords don't match"
    USERNAME_ALREADY_EXISTS = "Username already exists"
    EMAIL_ALREADY_EXISTS = "E-mail already exists"
    USERNAME_OR_PASSWORD_INCORRECT = "Username or password is incorrect"
    COURSE_ALREADY_EXISTS = "Course already exists"
    