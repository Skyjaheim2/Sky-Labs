class ExpressionFormatError(Exception):
    def __init__(self, expression):
        self.expression = expression
        self.message = f"{expression} is not formatted properly"
        super().__init__(self.message)