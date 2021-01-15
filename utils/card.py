
class Symbol:
    """

    This class contains the colors (which are strings)
    and the icons (out of the list[♥, ♦, ♣, ♠]) of all the cards.

    """


    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def __str__(self):
        return f"a {self.color} card with a {self.icon} icon."

class Card(Symbol):

    """

    This subclass of Symbol contains the values
    (within ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'])
    of the different cards.

    """



    def __init__(self, icon, value):
        super().__init__(self, icon)
        self.value = value

    def __str__(self):
        return f'The {self.value} of {self.icon}.'



