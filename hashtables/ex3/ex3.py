def intersection(arrays):
    result = []
    number_counts = {}
    
    for array in arrays:
        for number in array:
            if number in number_counts:
                number_counts[number] += 1
            else:
                number_counts[number] = 1
    
    for num, count in number_counts.items():
        if count > 1:
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
