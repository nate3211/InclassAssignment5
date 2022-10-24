#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.

import re

def quicksort(numbers_in_a_list):
    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list
    else:
        pivot = numbers_in_a_list[0]
        small = []
        big = []
        for i in range(1,len(numbers_in_a_list)):
            if numbers_in_a_list[i] < pivot:
                small.append(numbers_in_a_list[i])
            if numbers_in_a_list[i] > pivot:
                big.append(numbers_in_a_list[i])
        return quicksort(small) + [pivot] + quicksort(big)
    '''
     source: https://stackoverflow.com/questions/20175380/quick-sort-python-recursion
    ''' 
    
def read(fileinput):
    list_number = []
    with open(fileinput) as file_object:
        line = file_object.readline()
        number = re.findall("[0-9]+", line)
        for x in number:
            x = int(x)
            list_number.append(x)
    return list_number


def write(fileoutput, number):
    with open(fileoutput, "w") as sorted_output:
        for x in quicksort(number):
            x = str(x)
            sorted_output.write(f"{x}\n")
   


def main():
    number = read("numbers.txt")
    return write("sorted.txt", number)


if __name__ == "__main__":
    main()
