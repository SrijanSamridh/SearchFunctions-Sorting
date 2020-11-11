pos = -1

def LinearSearch(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()["pos"] = i
            return True
        i += 1
    return False

list = [4, 7, 8, 12, 45, 99]
n = 7

if BinarySearch(list, n):
    print("Found at ", pos+1)
else:
    print("Not Found")
