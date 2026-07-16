class DatabaseException(Exception):
    pass


class RecordNotFoundException(DatabaseException):
    pass


class DatabaseSaveException(DatabaseException):
    pass