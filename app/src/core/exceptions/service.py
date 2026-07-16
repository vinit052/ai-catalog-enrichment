class ServiceException(Exception):
    pass


class ImportProcessingException(ServiceException):
    pass


class ItemProcessingException(ServiceException):
    pass