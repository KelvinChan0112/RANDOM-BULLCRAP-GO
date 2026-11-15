import random as rd

def coin_flip(time_per_flip: int,chance_of_head: int) -> float :
    streak: int = 0
    total_time_taken: float = 0
    streak_required_to_win: int = 10
    consecutive_heads_chance: float = (chance_of_head ** streak_required_to_win) * 100 ** -(streak_required_to_win)
    current_tail_streak: int = 0
    highest_tail_streak: int = 0
    consecutive_tails_chance: float = 0
    temp = chance_of_head
                
    while streak < streak_required_to_win:
        if streak == 9:
            temp = chance_of_head
            chance_of_head = 10
        if rd.randint(1,100) <= chance_of_head:
            print("HEAD"+"!"*streak)
            streak += 1
            total_time_taken += time_per_flip
            current_tail_streak = 0
        else:
            streak = 0
            total_time_taken += time_per_flip
            current_tail_streak += 1
            print("Tail" + "." * current_tail_streak)
            chance_of_head = temp
    else:
        return float(total_time_taken)

n = 100
all_time: list[float] = []
for i in range(n):  
    all_time.append(coin_flip(1,60))
average:float = sum(all_time) / n
print(f"It took an average of {average}")
