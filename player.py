

class Player:

    def __init__(self, name):
        self.name = name
        self.ships_list = ["Destroyer", "Submarine",
                           "Battleship1", "battleship2", "Aircraft carrier"]
        self.create_game_board()

    def create_game_board(self):
        """
        method will create an empty battleship game board (20*20)
        """
        self.rows = 20
        self.cols = 20
        self.game_board = [["|_|" for i in range(
            self.cols)] for j in range(self.rows)]

    def display_game_board(self):
        """
        method will display the battleship game board
        """
        # print(self.game_board)
        for row in self.game_board:
            print("".join(row))

    def select_ship_to_place(self):
        """
        method will select which ship to be placed on the battleship game board
        """

        print("----choosing ship to place----")
        for i in range(len(self.ships_list)):
            print(f"choose {i} to place {self.ships_list[i]}")
        self.user_select_ship_index = int(input("Enter here: "))
        self.selected_ship_length = self.determine_ship_length(
            self.user_select_ship_index)
        print(
            f"you selected {self.ships_list[self.user_select_ship_index]} with length {self.selected_ship_length}\n")
        return self.user_select_ship_index

    def determine_ship_length(self, ship_index):
        """
        method returns length of selected ship
        """
        if ship_index == 0:
            # destroyer length
            ship_length = 2
        elif ship_index == 1:
            # submarine
            ship_length = 3
        elif ship_index == 2:
            # battleship1
            ship_length = 4
        elif ship_index == 3:
            # battleship1
            ship_length = 4
        else:
            # aircraft carrier
            ship_length = 3
        return ship_length

    def place_ship(self):
        """
        method will identify which direction and location to place the selected ship 
        """
        while True:
            print("Do you want to place your ship on the Horizontal or Vertical?")
            self.user_select_direction = input(
                "Enter 'h' to place on the Horizontal, 'v' to place on the Vertical: ")
            print("Which row you want to place your ship?")
            self.row_index = input(f"Row index, enter from 0 to {self.rows}: ")
            print("Which column you want to place your ship?")
            self.col_index = input(
                f"Column index, enter from 0 to {self.cols}: ")
            self.row_index = int(self.row_index)
            self.col_index = int(self.col_index)

            if self.game_board[self.row_index][self.col_index] != "|_|":
                print(f"overlaps with other ship, choose another location\n\n")
                continue
            else:
                self.game_board[self.row_index][
                    self.col_index] = f"|{self.ships_list[self.user_select_ship_index][0]}|"

            if self.user_select_direction == 'h':
                # user wants to place ship horizontally
                # row index remains the same
                for i in range(self.selected_ship_length):
                    self.game_board[self.row_index][i +
                                                    self.col_index] = f"|{self.ships_list[self.user_select_ship_index][0]}|"
            if self.user_select_direction == 'v':
                # user wants to place ship vertically
                # column index remains the same
                for i in range(self.selected_ship_length):
                    self.game_board[i +
                                    self.row_index][self.col_index] = f"|{self.ships_list[self.user_select_ship_index][0]}|"
            break
        self.display_game_board()


# player_one = Player("One")

# player_one.select_ship_to_place()
# player_one.place_ship()
# print("--------------------placing second ship---------------------")
# player_one.select_ship_to_place()
# player_one.place_ship()
