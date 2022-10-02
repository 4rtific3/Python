from typing_extensions import Self


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer