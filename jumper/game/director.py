from game.terminal_service import TerminalService
from game.word import Word
from game.jumper import Jumper
import os

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's Jumper. ie: "paratrooper".
        is_playing (boolean): Whether or not to keep playing.
        secret_word (SecretWord): The game's secret word.
        terminal_service: For getting and displaying information on the terminal.

        guess (str): User's letter guess
        updated_secret_word (str): The hidden word. IF the word is SECRET an eanample could be as follows..' EXAMPLE:  S _ C R _ T     
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._secret_word = Word()
        self._terminal_service = TerminalService()

        self._guess = " "
        self._updated_secret_word = ""

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

        first_guess = self._secret_word.get_first_guess() # first guess booleon switch.

        if first_guess == False:
            hidden_word= self._secret_word.get_hidden_word()
            start_message = self._jumper.get_intro_message(hidden_word)  # get intro message 
            self._terminal_service.write_text(start_message) # display into message
        
        
        self._guess = self._terminal_service.read_text("\nGuess a Capital letter [A-Z]: ")

    def _do_updates(self):
        """Updates the secret word

        Args:
            self (Director): An instance of Director.
        """
        
        self._updated_hidden_word = self._secret_word.update_hidden_word(self._guess)
        
         
    def _do_outputs(self):
        """desplayes secret word.  Displays jumper text art

        Args:
            self (Director): An instance of Director.
        """
       
 
        word = self._secret_word.get_word()
        missed_letters = self._secret_word.get_missed_letters()
        guess_right_wrong = self._secret_word.get_guessed_bool()
        won_lost = self._secret_word.get_won_bool()
        
        #print(F"\nThe hidden word is {word}  displayed for testing")
            
        self._terminal_service.write_text(f"\nThe wrong letters you have used so far are: {missed_letters}")

        already_guessed = self._secret_word.get_already_guessed_bool()
        if already_guessed == True:
            self._terminal_service.write_text(f"You already guessed that letter. Please try again. ")

        if already_guessed == False:
            guess = self._guess.upper() # make guess uppercase incase user typed lowercase
            message = self._jumper.get_messages(guess_right_wrong, won_lost, self._updated_hidden_word, guess, word)
            self._terminal_service.write_text(message)


        # Ending the game logic
        if won_lost == True:
            restart = self._terminal_service.read_text("\nDo you want to play again?  y/n ")
            if restart.upper() == "N": 
                self._is_playing = False
            if restart.upper() == "Y":
                os.system("python cse210-03/jumper/__main__.py")
                exit()
            else:
                self._is_playing = False

        guesses = self._jumper.get_guesses()
        if guesses == 0:
            restart = self._terminal_service.read_text("\nDo you want to play again?  y/n ")
            if restart.upper() == "N": 
                self._is_playing = False
            if restart.upper() == "Y":
                os.system("python cse210-03/jumper/__main__.py")
                exit()
            else:
                self._is_playing = False
