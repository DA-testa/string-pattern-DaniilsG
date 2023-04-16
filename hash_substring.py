# python3

def read_input():
   

    input_type = input()

    if 'I' in input_type:
        pattern = input().rstrip()
        text = input().rstrip()

    elif 'F' in input_type:
        filename = "struktura"

        with open("tests/" + filename, 'a') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    return (pattern, text)


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    p = len(pattern)
    t = len(text)
    p = hash(pattern)
    t = hash(text[:p_l])


    positions = []


    for i in range(t - p + 1):
        if p == t and pattern == text[i:i+p_l]:

            positions.append(i)

        if i < t - p:
            t = hash(text[i+1:i+p_l+1])


    return positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


