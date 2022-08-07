import time
from player import Player


class Game:

    def __init__(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")
        self.player1_view_player2_board = Player("Player1 view Player2 board")
        self.player2_view_player1_board = Player("Player2 view Player1 board")

    def game_rule(self):
        print("\nWelcome to Two Players Battleshipe Game!\n\n")
        print("Each player has a battleshop game board 20*20 dimension")
        print("Each player has 5 ships in the fleet, a destroyer (space size: 2), submarine (space size: 3), 2 battleship (space size: 4, and aircraft carrier (space size: 5)")
        print("Player can place each ship in any horizontal or vertical position, but not diagonally or overlapped")
        print("Player take turns to enter the location he/she wants to shoot on the other player's game board")
        print("If it is a miss, location displays 'O', if it hits ship, location displays 'X' ")
        print("Player who destories all ships of the other player wins the game")
        print(f"\n\n\n\n")

    def display_empty_game_board(self):
        print("Battleshipe Board Example\n")
        self.player1.display_game_board()

    def player_place_fleet(self, player):
        """
        method will ask player to place thier 5 ships on the gameboard
        """
        self.counter = 0
        while self.counter < 5:
            player.select_ship_to_place()
            player.place_ship()
            self.counter += 1

    def player1_turn(self):
        self.player1.player_shoot_index()
        self.player1_shoot_result = self.player2.determine_hit_miss(
            self.player1.shoot_row_index, self.player1.shoot_col_index)

        print(self.player1_shoot_result)
        print(f"{self.player1.name} score is {self.player1.score}\n\n")

        self.player1_view_player2_board.updated_board(
            self.player1_shoot_result, self.player1.shoot_row_index, self.player1.shoot_col_index)

    def player2_turn(self):
        self.player2.player_shoot_index()
        self.player2_shoot_result = self.player1.determine_hit_miss(
            self.player2.shoot_row_index, self.player2.shoot_col_index)

        print(self.player2_shoot_result)
        print(f"{self.player2.name} score is {self.player2.score}\n\n")

        self.player1_view_player2_board.updated_board(
            self.player1_shoot_result, self.player1.shoot_row_index, self.player1.shoot_col_index)

    def determin_winner(self, is_game_on):
        """
        method will print out the winner who's score reaches to 16 first, then return is_game_on
        """
        if self.player1.score >= 16:
            print(f"{self.player1.name} wins!")
            is_game_on = False
        elif self.player2.score >= 16:
            print(f"{self.player2.name} wins!")
            is_game_on = False
        else:
            is_game_on = True
        return is_game_on

    def run_game(self):
        """
        the central method to run the game, and to be called in main.py
        """
        self.game_rule()
        time.sleep(2)
        self.display_empty_game_board()
        print(f"\n\n\n\n\n\n")
        print(f"----{self.player1.name} game board")
        self.player2.display_game_board()
        print(f"----{self.player1.name} places the fleet----")
        self.player_place_fleet(self.player1)
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"----{self.player2.name} game board")
        self.player2.display_game_board()
        print(f"----{self.player2.name} places the fleet----")
        self.player_place_fleet(self.player2)
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        self.is_game_on = True
        while self.is_game_on:
            print(f"---{self.player1.name}'s turn----")
            self.player1_turn()
            self.is_game_on = self.determin_winner(self.is_game_on)
            if self.is_game_on == True:
                print(f"---{self.player2.name}'s turn----")
                self.player2_turn()


# game_one = Game()
# game_one.run_game()
# # game_one.player1_turn()
