class Question:
    def __init__(self, name: str, message: str = None, valid_answers: list[str] = None):
        self.name = name
        self.message = message
        self.valid_answers = valid_answers
