# python3

def read_input():

    input_type = input()

    if 'I' in input_type:
        pattern = input().rstrip()
        text = input().rstrip()
         
    elif 'F' in input_type:
        filename = "struktura"
         
        with open("tests/" + filename, 'r') as f:
         
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()

    return (pattern, text)


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):


    p_z = z(pattern)
      
    t_z = z(text)
   
    p_x = x(pattern)
      
    t_x = x(text[:p_len])
   

    positions = []

    for i in range(t_z - p_z + 1):
      
        if p_x == t_x and pattern == text[i:i+p_z]:
            positions.append(i)
            
        if i < t_z - p_z:
         
            t_x = hash(text[i+1:i+p_z+1])


    return positions


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


