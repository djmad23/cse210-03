class Jumper:
    """The paratrooper who jumped out of a perfectly good plane!  
    
    The responsibility of jumper is to keep track of the jumper text art and number of guesses left. 
    
    Attributes:
        _guesses (int): The number of guesses left
        _message (str): The text art representation of the paratrooper at different stages of parachute failer along with message.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._guesses = 5
        self._message = ""

    def get_guesses(self):
        """Returns number of guesses
        
        """

        return self._guesses

    def get_intro_message(self, updated_hidden_word):
        """ Returns jumper intro text art along with message. 
        
        """

        self._message = (f"""\nThe Parashooter jumped out of a plain! If you can guess the hidden word they will land safely. 
The hidden word is {updated_hidden_word}.
  _________
 /         \\
/ _   _   _ \\  
|/ \ / \ / \|  _____________
 \  | _ |  /  /             \\
  o '(_)' o  <      Help!    |
   \/.X.\/    \\_____________/
     |_|
     / \\
     \\ /
     U U           
            """)
    
        return self._message


    def get_messages(self, guess_right_wrong, won_lost, updated_hidden_word, letter = "", word = ""):
        """Method to retrieve messages. Returns jumper text art and message
        
        Args:
            self (Jumper): An instance of Jumper.
            message (str): Jumper text art and message
        """
        if won_lost == True:
            self._message = (f"""Congratulations, you guessed the word! You win!"
  _________
 /         \\
/ _   _   _ \\  
|/ \ / \ / \|  _____________
 \  | _ |  /  /             \\
  o '(_)' o  < You saved me! |
   \/.X.\/    \\_____________/
     |_|
     / \\
     \\ /
     U U  
            """)
            return self._message


        if guess_right_wrong == False:

            self._guesses = self._guesses - 1 # Reduce guesses by one

            if self._guesses == 4:
                self._message = (f"""{letter} is not in the word. Please try again! You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.

 /         \\
/ _   _   _ \\  
|/ \ / \ / \|  _____________
 \  | _ |  /  /             \\
  o '(_)' o  <     Oh No!    |
   \/.X.\/    \\_____________/
     |_|
     / \\
     \\ /
     U U 
                """)
                return self._message

            elif self._guesses == 3:
                self._message = (f"""{letter} is not in the word. Please try again! You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.

/ _   _   _ \\  
|/ \ / \ / \|  _____________
 \  | _ |  /  /             \\
  o '(_)' o  <     Yikes!    |
   \/.X.\/    \\_____________/
     |_|
     / \\
     \\ /
     U U 
                """)
                return self._message


            elif self._guesses == 2:
                self._message = (f"""{letter} is not in the word. Please try again! You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.

|/ \ / \ / \|  _____________
 \  | _ |  /  /             \\
  o '(_)' o  <    Not Good!  |
   \/.X.\/    \\_____________/
     |_|
     / \\
     \\ /
     U U 
                """)
                return self._message

            elif self._guesses == 1:
                self._message = (f"""{letter} is not in the word. Please try again! You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.

               _____________
 \  | _ |  /  /             \\
  o '(_)' o  <     Scary!    |
   \/.X.\/    \\_____________/
     |_|
     / \\
     \\ /
     U U 
                """)
                return self._message

            elif self._guesses == 0:
                self._message = (f"""The jumper died! Sorry, you ran out of tries! The secret word was {word}. 

             _____________
  o   _   o /             \\
   \ (_) / <    Nooooo!    |
     .X.    \\_____________/
     |_|
     / \\
     \\ /
     U U 
                """)
                return self._message


        if guess_right_wrong == True:
            if won_lost == False:
                if self._guesses == 5:
                    self._message = (f"""You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.
  _________
 /         \\
/ _   _   _ \\  
|/ \ / \ / \|  ___________________________________
 \  | _ |  /  /                                   \\
  o '(_)' o  <  Good job, {letter} is in the word!        |
   \/.X.\/    \\___________________________________/
     |_|
     / \\
     \\ /
     U U 
                """)
                    return self._message

                if self._guesses == 4:
                    self._message = (f"""You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.

 /         \\
/ _   _   _ \\  
|/ \ / \ / \|  ___________________________________
 \  | _ |  /  /                                   \\
  o '(_)' o  <  Good job, {letter} is in the word!        |
   \/.X.\/    \\___________________________________/
     |_|
     / \\
     \\ /
     U U 
                """)
                    return self._message

                if self._guesses == 3:
                    self._message = (f"""You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.

/ _   _   _ \\  
|/ \ / \ / \|  ___________________________________
 \  | _ |  /  /                                   \\
  o '(_)' o  <  Good job, {letter} is in the word!        |
   \/.X.\/    \\___________________________________/
     |_|
     / \\
     \\ /
     U U    
                """)

                    return self._message   

                if self._guesses == 2:
                    self._message = (f"""You have {self._guesses} guesses left. The secret word is {updated_hidden_word}.      

|/ \ / \ / \|  ___________________________________
 \  | _ |  /  /                                   \\
  o '(_)' o  <  Good job, {letter} is in the word!        |
   \/.X.\/    \\___________________________________/
     |_|
     / \\
     \\ /
     U U     
                """)
                    return self._message 

                if self._guesses == 1:
                    self._message = (f"""You have {self._guesses} guesses left. The secret word is {updated_hidden_word}. 

               ___________________________________
 \  | _ |  /  /                                   \\
  o '(_)' o  <  Good job, {letter} is in the word!        |
   \/.X.\/    \\___________________________________/
     |_|
     / \\
     \\ /
     U U   
                """)
                    return self._message 

 



            


