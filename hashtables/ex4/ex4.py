def has_negatives(a):
    result = []
    numbers = set(a)
    
    for num in a :
        if num > 0 and -num in numbers:
            result.append(num)
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
