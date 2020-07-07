# BinarySearch.

# It returns location of search in the given list
# if present, else returns -1
def binarySearch(nums, low, high, search):
    while low <= high:

        mid = low + (high - low) // 2

        # Check if search is present at mid
        if nums[mid] == search:
            return mid

        # If search is greater, ignore left half
        elif nums[mid] < search:
            low = mid + 1

        # If search is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

#Code
numbers = [22, 31, 40, 10, 40, 99, 33, 44, 11, 55]
numbers.sort()
print(numbers)
number_to_search = int(input("Enter number to search in the list"))
start = 0
end = len(numbers)-1

# function call
result = binarySearch(numbers, start, end, number_to_search)

if result != -1:
    print("Number is present at index % d" % result)
else:
    print("Number is not present in the list")
