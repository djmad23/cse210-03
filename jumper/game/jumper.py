
class Jumper:
    """The paratrooper who jumped out of a perfectly good plane!  
    
    The responsibility of jumper is to keep track of the jumper text art and number of guesses left. 
    
    Attributes:
        _guesses (int): The number of guesses left
        _jumper (str): The text art representation of the paratrooper at different stages of parachute failer.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._guesses = 0
        self._jumper = ""
    
    