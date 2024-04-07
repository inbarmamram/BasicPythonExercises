# For ex6()
import re
from collections import Counter
# For ex9()
# import pip # not working
import pkg_resources # need to install with "python3 -m pip install setuptool"


def ex6():
    """
    print a long text,
    converts it to a list,
    and prints all the words and the frequency of each word.
    """
    with open("random_text.txt") as file:
        lines = [line.rstrip() for line in file if line.rstrip()]
    
    words = []
    for line in lines:
        unformatted_words = line.split(' ')
        formatted_words = []
        for unformatted in unformatted_words:
            formatted_words.append(re.sub("[^a-z']+", "", unformatted.lower()))
        # formatted_words = [re.sub("[^a-z']+", "", unformatted.lower()) for unformatted in unformatted_words]
        words += formatted_words

    frequency = Counter(words)
    print(frequency)

def ex9():
    """
    Get a list of locally installed Python modules.
    """
    #installed_modules = pip.get_installed_distributions()
    #module_list = sorted([str(module) for module in installed_modules])

    installed_modules = pkg_resources.working_set
    module_list = sorted([f"{module.key}={module.version}" for module in installed_modules])
    
    print(*module_list, sep="\n")

def ex18():
    """
    Find the median among three given numbers.
    """
    numbers = []
    for number in range(3):
        numbers.append(int(input("Enter a number: ")))
    numbers = sorted(numbers)
    print(f"The median is: {numbers[1]}")

def ex23():
    """
    Create a sequence where:
        The first four members of the sequence are equal to one.
        Each successive term of the sequence is equal to the sum of the four previous ones.
    Find the Nth member of the sequence.
    """
    AMOUNT_TO_SUM = 4
    INITIAL_VALUE = 1
    seq_length = int(input("Enter sequence length: "))
    sequence = []
    
    for index in range(seq_length):
        if index < AMOUNT_TO_SUM:
            sequence.append(INITIAL_VALUE)
        else:
            sequence.append(sum(sequence[-AMOUNT_TO_SUM:]))

    print(sequence[seq_length - 1])

def ex24():
    """
    Find the total number of even or odd divisors of a given integer.
    """
    number = int(input("Enter a number: "))
    devisors = [devisor for devisor in range(1, number + 1) if number % devisor == 0]
    even_devisors = [devisor for devisor in devisors if devisor % 2 == 0]
    odd_devisors = [devisor for devisor in devisors if devisor % 2 != 0]
    print("Even devisors:", even_devisors)
    print("Odd devisors:", odd_devisors)


def ex26(numbers):
    """
    Compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).
    """
    for index in range(len(numbers)):
        for pair_index in range(index + 1, len(numbers)):
            print(numbers[index], numbers[pair_index])

def ex30():
    """
    Reverse the digits of a given number and add them to the original.
    Repeat this procedure if the sum is not a palindrome.
    """
    number = int(input("Enter a number: "))
    number += int(str(number)[::-1])
    while not is_palindrome(str(number)):
        number += int(str(number)[::-1])
    print(number)

def is_palindrome(input):
    return input == input[::-1]

def ex32():
    """
    find the heights of the top three buildings in descending order from eight given buildings.
    """
    BUILDINGS_AMOUNT = 8
    
    building_heights = []
    print(f"Input the heights of {BUILDINGS_AMOUNT} building(s):")
    for height in range(BUILDINGS_AMOUNT):
        building_heights.append(int(input("Enter building height: ")))
    
    building_heights.sort(reverse=True)
    print("height of the top three buildings:")
    print(*building_heights[:3], sep='\n')


def main():
    # ex6()
    # ex9()
    # ex18()
    # ex23()
    # ex24()
    # ex26([1, 2, 3])
    # ex30()
    ex32()


if __name__ == "__main__":
    main()