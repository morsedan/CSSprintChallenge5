def get_indices_of_item_weights_brute_force(weights, length, limit):
    for i in range(length):
        for j in range(i+1, length):
            if weights[i] + weights[j] == limit:
                return (j, i)
    return None

def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}
    
    for i in range(len(weights)):
        weight_dict[weights[i]] = i
    
    for i in range(len(weights)):
        left = limit - weights[i]
        if left in weight_dict:
            return (weight_dict[left], i)
        
    return None