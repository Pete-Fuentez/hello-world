# testsort.py

def isSorted(lst):
    if len(lst) < 2:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

if __name__ == "__main__":
    test_lists = [
        [],
        [1],
        [1, 2, 3, 4],
        [1, 2, 2, 3, 4],
        [4, 3, 2, 1],
        [1, 3, 2],
        [1, 1, 1, 1]
    ]
    
    for lst in test_lists:
        result = isSorted(lst)
        print(f"List: {lst}, isSorted: {result}")
