my_numbers: list[float] = []  # making a list that is initally empty

my_numbers.append(
    1.5
)  # add 1.5 to the end of whatever is in the list using append function
print(my_numbers)


# make a list of numbers

game_points: list[int] = [102, 86, 94]
print(game_points[2])


# modifying/change the value of an item
game_points[1] = 72
print(game_points)

# we cannot change str , gives an error
my_name: str = "Izzi"
my_name[3] = "y"

name_as_list: list[str] = list(my_name)  # converting my_name to type list
print(name_as_list)

name_as_list.append("e")  # add e to the very end
print(name_as_list)

game_points.pop(1)  # remove the number 72 by using the index of 72 and pop function
