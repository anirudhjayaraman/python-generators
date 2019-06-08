# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:32:16 2019

@author: Anirudh
"""
# Example 1
def even_numbers_generator(n):
    for i in range(n): 
        if (i % 2 == 0): 
            yield(i)
           
# Example 2            
def fibonacci_seq(n):
    if(n <= 2): 
        return 1 
    else: 
        return fibonacci_seq(n-1) + fibonacci_seq(n-2)

# Example 3    
def fibonacci_generator(n): 
    return(fibonacci_seq(i) for i in range(1,n))

# Example 4    
def fibonacci_gen():
    trailing, lead = 0, 1
    while True:
        yield lead
        trailing, lead = lead, trailing + lead
            


def main():
    # Example 1
    players = ["Kohli","Dhoni","Rayudu","Bumrah"]
    players_upper = [player.upper() for player in players]
    players_upper_generator = (player.upper() for player in players)
    for i in range(4): 
        print(players_upper_generator.__next__())
        
    # Example 2
    integers = even_numbers_generator(10)
    for i in range(3):
        print(integers.__next__())
    print()
    for integer in integers:
        print(integer)
        
    # Example 3
    print()
    print("Fibonacci Generator: ")
    fib_gen = fibonacci_generator(10)
    for i in range(1,9): print(fib_gen.__next__())
    
    # Example 4
    fib_gen_alt = fibonacci_gen()
    for i in range(1,90): print(fib_gen_alt.__next__())
        


if __name__ == "__main__":
    main()
