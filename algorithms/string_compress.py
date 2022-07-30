def compressed_string(string: str):
    # handle edge cases
    if len(string) <= 1:
        return string
    compressed = ""
    count = 1
    start = True
    for i in range(len(string)):
        if start:
            compressed += string[i]
        try:
            if string[i] == string[i + 1]:
                count += 1
                start = False
            else:
                start = True
                compressed += str(count)
                count = 1
        except IndexError:
            compressed += str(count)
            break

    return compressed


print(compressed_string('a'))
