class Greeter:
    def __init__(self, greeting_text="Привет мир"):
        self.__greeting_text = str(greeting_text)
    def greet(self):
        return "Привет, мир!"
