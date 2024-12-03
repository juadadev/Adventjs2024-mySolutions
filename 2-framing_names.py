def createFrame(names):
    longest_name = max(names, key=len)
    length_longest_name = len(longest_name)

    length_longest_name_end_and_start = length_longest_name + 4

    result_frame:str = []

    for i in range(len(names) + 2):
        if i == 0 or i == len(names) + 1:
            result_frame.append(f'{"*" * length_longest_name_end_and_start}') 
        else:
            result_frame.append(f'* {names[i - 1]}{" " * (length_longest_name - len(names[i - 1]))} *')

    return "\n".join(result_frame)

result = createFrame(['midu', 'madeval', 'educalvolpz'])
print(result)
