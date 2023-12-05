from collections import Counter, defaultdict

def count_winners(winning, actual_nums):
    seen = set(winning)
    count = 0
    for num in actual_nums:
        if num in seen:
            count += 1
    return count
def add_copies(card_num, wins, total_scratch_cards, val):
    for i in range(card_num + 1, card_num + 1 + wins):
        total_scratch_cards[i] += val

    return total_scratch_cards


ans = 0
total_scratch_cards = defaultdict(int)
last_num = 0

with open("4_advent.txt", "r") as f:
    for card in f:
        game_id, draws = card.strip().split(": ")
        game_id = int(game_id.split()[-1])

        print(game_id)
        winning_numbers, drawn_numbers = draws.split(" | ")

        total_scratch_cards[game_id] += 1  # Count all cards we iterate over / part 2
       
        winning_numbers = [int(num) for num in winning_numbers.split()]
        drawn_numbers = drawn_numbers.strip()  # Sometimes drawn numbers have extra white space
        drawn_numbers = [int(num) for num in drawn_numbers.split()]  
        num_of_winners = count_winners(winning_numbers, drawn_numbers)
        if num_of_winners > 0:
            ans += 2 ** (num_of_winners - 1)
        # part two
        if total_scratch_cards.get(game_id, 0):
            total_scratch_cards = add_copies(game_id, num_of_winners, total_scratch_cards, total_scratch_cards.get(game_id,0))
        # Print results for verification
        print("Winning numbers:", winning_numbers)
        print("Drawn numbers:", drawn_numbers)
        last_num = game_id
print(total_scratch_cards)
part_2_ans = 0
for key,val in total_scratch_cards.items():
    if key <= last_num:
        part_2_ans += val
print(ans)
print("Part 2:", part_2_ans)


