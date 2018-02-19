def find_items(items, value):
    new_list = []
    for i in items:
        if i < value:
            new_list.append(i)
    print new_list

def main():
    numbers = [15, 4, 5, 2, 6, 43, 23, 12, 4, 32, 12, 7, 65, 8, 66, 4, 5, 43, 2, 1, 3]
    find_items(numbers, 7)

main()
