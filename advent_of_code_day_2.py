from collections import Counter
from functools import reduce
from operator import mul, or_

with open("advent_of_code_2.txt", 'r') as file:
        lines = file.readlines()
# print(lines)
cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
}
def get_game_id(word):
    for i, token in enumerate(word):
         if token == "Game":
              return int(word[i+1][:-1])
    return -1
def is_valid_game(word):
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for i in range(len(word) - 1):
        ch = word[i]
        color = word[i + 1]
        color = color.replace(";", "").replace(",", "")
        color = color.strip()
        if ch.isdigit() and color:       
            cubes[color] = cubes[color] - int(ch)
    for key,val in cubes.items():
         if val < 0:
              return False
    return True
ans = 0
for line in lines:
    word = line.split(" ")
    if is_valid_game(word):
         print(get_game_id(word))
         ans += get_game_id(word)
print("Final Answer", ans)

thres = Counter({"red":12, "green":13, "blue":14})

tot_1 = 0
tot_2 = 0
with open("advent_of_code_2.txt", "r") as f:
    for game in f:
        print(game)
        game_id, draws = game.strip().split(": ")
        print(game_id, draws)
        game_id = int(game_id.split(" ")[1])
        print(game_id)
        draws = [[c.split(" ") for c in d.split(", ")] for d in draws.split("; ")]
        print(draws)
        draws = [Counter({c[1]:int(c[0]) for c in d}) for d in draws]
        print(draws)
        tot_1 += all(d<=thres for d in draws) * game_id

        tot_2 += reduce(mul, reduce(or_, draws).values())


print(1, tot_1)
print(1, tot_2)

