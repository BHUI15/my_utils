# Refactor a python script into modules
from arith_utils import factorial, is_prime, is_even, safe_devide
import cowsay
import review 

def main():
    # List of numbers to analyze
    numbers = [3, 5, 10]
    for n in numbers:
        print(f"{n}! = {factorial(n)}, Prime? {is_prime(n)}")
        #print(n)

    # review1 = review.Review("Great!", "positive")
    # review2 = review.Review("Bad idea!", "negative")

    # print(review1.text,review1.is_positive())
    # print(review2.word_count())

    safe_devide()
    

if __name__ == "__main__":
    main()
