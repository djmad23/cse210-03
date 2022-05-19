
class SecretWord:
    """The random secret word. 
    
    The responsibility of the SecretWord is to get a random secret word, and keep track of the letters guessed correctly and the letters guessed incorrectly. 
    
    Attributes:
        secret_word (str): The secret word (randomly generated from a text file?)
        
    """

    def __init__(self):
        """Constructs a new SecretWord

        Args:
            secret_word (str): The secret word (randomly generated from a text file?)
        """
        self._secret_word = ""
        