def createFrame(names):
    longest_length = len(max(names, key=len))
    line_frames = '*' * (longest_length + 4)

    result_frame: str = [line_frames]

    for name in names:
        result_frame.append(f'* {name}{" " * (longest_length - len(name))} *')

    result_frame.append(line_frames)
    return "\n".join(result_frame)


result = createFrame(['midu', 'madeval', 'educalvolpz'])
print(result)
