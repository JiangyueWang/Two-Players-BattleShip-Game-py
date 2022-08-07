

class Player:

    def __init__(self, name):
        self.name = name
        self.ships_list = ["Destroyer", "Submarine",
                           "Battleship1", "battleship2", "Aircraft carrier"]
        self.selected_ships_list = []
        self.row_letter = ["A", "B", "C", "D", "E", "F", "G", "H",
                           "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        self.score = 0
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
        while True:
            print("----choosing ship to place----")
            for i in range(len(self.ships_list)):
                print(f"choose {i} to place {self.ships_list[i]}")
            self.user_select_ship_index = int(input("Enter here: "))
            if self.ships_list[self.user_select_ship_index] in self.selected_ships_list:
                print(
                    f"You have selected {self.ships_list[self.user_select_ship_index]}, change another ship")
                continue
            else:
                self.selected_ship_length = self.determine_ship_length(
                    self.user_select_ship_index)
                print(
                    f"you selected {self.ships_list[self.user_select_ship_index]} with length {self.selected_ship_length}\n")
                self.selected_ships_list.append(
                    self.ships_list[self.user_select_ship_index])
                break

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
                "Enter 'h' to place on the Horizontal, 'v' to place on the Vertical: ").lower()

            print(
                f"Location you want to place your ship, letter 'A-T'for row, number '0 to {self.cols} for column'")
            self.user_place_ship_location = input("Enter here: ")
            self.col_index = self.user_entered_location_index(
                self.user_place_ship_location)[0]
            self.row_index = self.user_entered_location_index(
                self.user_place_ship_location)[1]

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

    def player_shoot(self):
        """
        method will ask player which location to shoot
        """
        print(
            f"Location you want to shoot, letter 'A-T'for row, number '0 to {self.cols} for column'")
        self.user_shoot_location = input("Enter here: ")
        self.user_entered_location_index(self.user_shoot_location)

    def determine_hit_miss(self, row_index, col_index):
        """
        method will return whether player has hit or miss the other player's ship

        """
        if self.game_board[row_index][col_index] != "|_|":
            return "Hit"
        else:
            return "Missed"

    def updated_board(self, shoot_result, row_index, col_index):
        """
        method will update the location with "|X|" if the player hits the other player's ship, player's score increased by 1
        and will update location with "|O|" if the player missed the target
        """
        if shoot_result == "Hit":
            self.game_board[row_index][col_index] = "|X|"
            self.score += 1
        else:
            self.game_board[row_index][col_index] = "|O|"
        self.display_game_board()

    def user_entered_location_index(self, user_entered_location):
        """
        method will return the column and row index of user entered location
        """
        location_col_index = int(user_entered_location[1:])
        location_row_index = self.row_letter.index(
            user_entered_location[0])
        return location_col_index, location_row_index


# player_one = Player("One")

# player_one.select_ship_to_place()
# player_one.place_ship()
# # print("--------------------placing second ship---------------------")
# # player_one.select_ship_to_place()
# # player_one.place_ship()
