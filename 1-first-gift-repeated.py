gift1 = [3, 1, 2, 3, 4, 2, 5]

def prepare_gifts(gifts):
    unique_gifts = list(set(gifts))
    sorted_gifts = sorted(unique_gifts)
    
    return sorted_gifts

result = prepare_gifts(gift1)
print(result)
