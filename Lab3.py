print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order=None):

        # Copy input list to results list
        arr_result = arr.copy()

        # Get number of elements in the list
        n = len(arr_result)
        for values in arr:
            if not isinstance(values,int):
                return 2

        if n < 10 and n != 0:
            if sorting_order == SORT_ASCENDING:
                arr_result.sort()
            elif sorting_order == SORT_DESCENDING:
                arr_result.sort(reverse=True)
        else:
            if n == 0:
                arr_result = 0
            else:
                arr_result = 1
        return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

    print("Numbers include in arrary is 0")
    result = bubble_sort([],    )
    print(result)

    print("Numbers include in arrary more than 10")
    result = bubble_sort([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],)
    print(result)


if __name__ == "__main__":
    main()


