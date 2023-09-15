if __name__ == "__main__":
    ls = [1, 3, 4, 2, 3]
    slow = ls[0]
    fast = ls[0]
    while True:
        slow = ls[slow]
        fast = ls[ls[fast]]
        if slow == fast:
            break
    fast = ls[0]
    while slow != fast:
        slow = ls[slow]
        fast = ls[fast]
    print(slow)
