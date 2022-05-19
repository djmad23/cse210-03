from game.terminal_service import TerminalService
from game.secret_word import SecretWord
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's Jumper. ie: "paratrooper".
        is_playing (boolean): Whether or not to keep playing.
        secret_word (SecretWord): The game's secret word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._secret_word = SecretWord()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets a ramdom secret word. Gets players letter guess

        Args:
            self (Director): An instance of Director.
        """
        
        
    def _do_updates(self):
        """Updates the secret word

        Args:
            self (Director): An instance of Director.
        """
        
        
    def _do_outputs(self):
        """desplayes secret word.  Displays jumper text art

        Args:
            self (Director): An instance of Director.
        """
        