import random

class SnakeAndLadders:
    def __init__(self, board_size=100):
        self.board_size = board_size
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.player_positions = [0, 0]  # Two players starting at position 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        initial_position = self.player_positions[player]
        new_position = initial_position + steps
        if new_position > self.board_size:
            new_position = initial_position  # Player stays in place if they exceed board size
        else:
            new_position = self.snakes.get(new_position, new_position)
            new_position = self.ladders.get(new_position, new_position)
        self.player_positions[player] = new_position

    def play(self):
        current_player = 0
        while True:
            input(f"Player {current_player + 1}'s turn. Press Enter to roll the dice...")
            dice_roll = self.roll_dice()
            print(f"Player {current_player + 1} rolled a {dice_roll}")
            self.move_player(current_player, dice_roll)
            print(f"Player {current_player + 1} is now on square {self.player_positions[current_player]}")
            if self.player_positions[current_player] == self.board_size:
                print(f"Player {current_player + 1} wins!")
                break
            current_player = 1 - current_player  # Switch player

if __name__ == "__main__":
    game = SnakeAndLadders()
    game.play()
