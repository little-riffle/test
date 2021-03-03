def get_components_of_sum(numbers, result):
    hash_table = {}

    for number in numbers:
        if number in hash_table.keys():
            return hash_table[number], number
        else:
            hash_table[result - number] = number
