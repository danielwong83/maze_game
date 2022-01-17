import random
from colors import colors


class Maze:

    def __init__(self, x = 5, y = 5, mode="E"):
        self.x = int(x)
        self.y = int(y)
        self.mode = mode

    def __str__(self):
        return "Dimensions: " + str(self.x) + ", " + str(self.y) + "; Mode: " + self.mode

    def mazeMap(self, starting_vertice):

        self.x = 5  # remove when dynamic
        self.y = 5  # remove when dynamic

        moves = 10

        functional_map = False

        while not functional_map:

            map_list = list()
            map_list.append(starting_vertice)

            while len(map_list) < moves:

                if map_list[-1][1] == (self.y - 1):
                    random_move = random.choice(["q", "w", "a"])
                elif map_list[-1][1] == 0:
                    random_move = random.choice(["w", "e", "d"])
                else:
                    random_move = random.choice(["w", "e", "d", "a", "q"])

                if random_move == "q":
                    vertice = [(map_list[-1][0] - 1), (map_list[-1][1] - 1)]
                elif random_move == "a":
                    vertice = [map_list[-1][0], (map_list[-1][1] - 1)]
                elif random_move == "w":
                    vertice = [(map_list[-1][0] - 1), map_list[-1][1]]
                elif random_move == "e":
                    vertice = [(map_list[-1][0] - 1), (map_list[-1][1] + 1)]
                elif random_move == "d":
                    vertice = [map_list[-1][0], (map_list[-1][1] + 1)]

                if vertice in map_list:
                    continue
                else:
                    map_list.append(vertice)

            if map_list[-1][0] < 0:
                continue
            else:
                functional_map = True

        return map_list

    def starting_vertice(self):

        starting_vertice_value = random.randint(0, self.y - 1)
        starting_vertice = [self.y - 1, starting_vertice_value]

        return starting_vertice


    def initial_visual(self, maze, step):

        full_matrix = list()

        for i in (range(self.x)):

            row_list = list()

            for j in (range(self.y)):

                if [i, j] == maze[0]:
                    row_list.append(str(colors.fg.blue + "⦾" + colors.reset))
                elif [i, j] == maze[-1]:
                    row_list.append(str(colors.fg.green + "⦾" + colors.reset))
                elif [i, j] == maze[step]:
                    row_list.append(str(colors.fg.yellow + "⦾" + colors.reset))
                else:
                    row_list.append("-")

            full_matrix.append(row_list)

        for i in full_matrix:

            printer = ""

            for j in i:
                printer += j + " "

            print(printer)





# game start

# x, y = input("Choose Maze Dimensions (X {space} Y): ").split()

# mode = input("Maze Difficulty (E, H): ")


game = Maze()

game_starting_vertice = game.starting_vertice()
game_answer = game.mazeMap(game_starting_vertice)
# print(game_answer)



finished = False

while True:

    user_list = [game_starting_vertice]

    while finished == False:

        if len(user_list) == 1:
            game.initial_visual(game_answer, len(user_list) - 1)

        user_guess_letter = input("Guess (a, q, w, e, d), currently on Guess " + str(len(user_list)) + ": ")

        if user_guess_letter == "a":
            user_guess_coordinates = [user_list[-1][0], (user_list[-1][1] - 1)]
        elif user_guess_letter == "q":
            user_guess_coordinates = [(user_list[-1][0] - 1), (user_list[-1][1] - 1)]
        elif user_guess_letter == "w":
            user_guess_coordinates = [(user_list[-1][0] - 1), user_list[-1][1]]
        elif user_guess_letter == "e":
            user_guess_coordinates = [(user_list[-1][0] - 1), (user_list[-1][1] + 1)]
        elif user_guess_letter == "d":
            user_guess_coordinates = [user_list[-1][0], (user_list[-1][1] + 1)]

        if user_guess_coordinates == game_answer[len(user_list)]:
            user_list.append(game_answer[len(user_list)])

            if user_list == game_answer:
                finished = True
            else:
                game.initial_visual(game_answer, len(user_list) - 1)
        else:
            print("Incorrect, Start from the beginning")
            break

    if finished == True:
        break



