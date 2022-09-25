from ast import If
from game.hilo import Card


class Director:
    """ A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[card]): A list of card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        self.old_card = Card()
        self.nextCard = Card()
        self.keep_playing = True
        self.election = ''
        self.total_score = 400

    def start_game(self):
        while self.keep_playing:
            print(f'\nThe card is {self.old_card.value}')
            self.get_election()
            self.do_outputs()
            self.check()
            self.get_play_again()
            self.do_updates()
            self.check()
        else:
            print('Game Over')

    def get_election(self):
        #
        election_H_L = input("Higher or lower? [h/l]: ")
        self.election = election_H_L
        print(f'Next card was: {self.nextCard.value}')

    def get_play_again(self):
        play_Again = input('Play again? [y/n]: ')
        if play_Again == 'y':
            self.keep_playing = True
        else:
            self.keep_playing = False
       
    def do_updates(self):
        if not self.keep_playing:
            return 
        self.old_card = Card()
        self.nextCard = Card()
    def do_outputs(self):
        if not self.keep_playing:
            return
        
        if self.election == 'h':
            if self.nextCard.value >= self.old_card.value:
                self.total_score += 100
            else:
                self.total_score -= 75
        elif self.election == 'l':
            if self.nextCard.value <= self.old_card.value:
                self.total_score += 100
            else:
                self.total_score -= 75
        print(f"Your score is: {self.total_score}")
        
        if self.total_score >= 1000:
            print('You win!')

    def check(self):
        if self.total_score <= 0:
            self.keep_playing = False
        else:
            self.keep_playing = True