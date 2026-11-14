#file name: main.py
import random as rd
def main() -> None:
    try:
        time_per_flip: float = float(input("Enter time taken to flip the coin once(s): "))
        chance_of_head: float = float(input("Enter chance of getting a head(no need to type %): "))
        streak: int = 0
        total_time_taken: float = 0
        streak_required_to_win: int = 10
        consecutive_heads_chance: float = (chance_of_head ** streak_required_to_win) * 100 ** -(streak_required_to_win)
        current_tail_streak: int = 0
        highest_tail_streak: int = 0
        consecutive_tails_chance: float = 0
            
        while streak < streak_required_to_win:
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
                if current_tail_streak > highest_tail_streak:
                    highest_tail_streak = current_tail_streak
        else:
            consecutive_tails_chance: float = ((100-chance_of_head) ** highest_tail_streak) * 100 ** -(highest_tail_streak)
            print(f"You got {streak_required_to_win} heads in a row! It would've taken {total_time_taken:.1f} seconds")
            print(f"The chance of that happening is {consecutive_heads_chance}%")
            print(f"Your highest tail streak was {highest_tail_streak}. The chance of that happening is {consecutive_tails_chance}%")
                
    except RuntimeError:
        print("Maybe it was your luck's fault = =")
    except TypeError, ValueError, NameError:
        print("Please enter actual value..")


if __name__ == "__main__":
    main()
