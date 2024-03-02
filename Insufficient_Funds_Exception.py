class InsufficientFundsException(BaseException):
    def _init_(self, message):
        super().__init__(message)
