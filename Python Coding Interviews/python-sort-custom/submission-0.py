from typing import List

# key parameter accepts function as a input and sort based on function's output

def get_length(value):
    return len(value)
def get_absolute(num):
    return abs(num)
def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_length,reverse=True)
    return words
    


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_absolute)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
