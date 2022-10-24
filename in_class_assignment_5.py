#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.

'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British 
computer scientist Tony Hoare in 1959.
Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to 
sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists 
based on the pivot item and recursively sort the sublists.
The steps of the algorithm are as follows:
1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 
The base cases occur when the sublists are either empty or have one element, as 
these are inherently sorted. 
 '''
import re
# Quicksort function 
def quicksort(numbers_in_a_list):
    if len(numbers_in_a_list) <= 1:
        return numbers_in_a_list
    else:
        pivot = numbers_in_a_list[0]
        small = []
        large = []
        for z in range(1,len(numbers_in_a_list)):
            if numbers_in_a_list[z] < pivot:
                small.append(numbers_in_a_list[z])
            if numbers_in_a_list[z] > pivot:
                large.append(numbers_in_a_list[z])
        return quicksort(small) + [pivot] + quicksort(large)
    '''
     source from: https://stackoverflow.com/questions/20175380/quick-sort-python-recursion
    '''  
# Function for reading numbers    
def read(fileinput):
    list_number = []
    with open(fileinput) as file_object:
        line = file_object.readline()
        number = re.findall("[0-9]+", line)
        for z in number:
            z = int(z)
            list_number.append(z)
    return list_number
    '''
    https://vegibit.com/how-to-read-and-write-files-in-python
    '''

# Write output into sorted.txt
def write(fileoutput, number):
    with open(fileoutput, "w") as sorted_output:
        for z in quicksort(number):
            z = str(z)
            sorted_output.write(f"{z}\n")
   

# Main function
def main():
    number = read("numbers.txt")
    return write("sorted.txt", number)


if __name__ == "__main__":
    main()
