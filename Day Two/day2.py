def is_safe_sequence(sequence):
    increasing = all(0 < sequence[i+1] - sequence[i] <= 3 for i in range(len(sequence)-1))
    decreasing = all(0 < sequence[i] - sequence[i+1] <= 3 for i in range(len(sequence)-1))
    
    return increasing or decreasing

def main():
    safe_count = 0
    with open('Day Two/input.txt', 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            sequence = list(map(int, line.split()))
            if is_safe_sequence(sequence):
                safe_count += 1
                continue
            found_safe_removal = False
            for i in range(len(sequence)):
                test_sequence = sequence[:i] + sequence[i+1:]
                if is_safe_sequence(test_sequence):
                    found_safe_removal = True
                    break
            if found_safe_removal:
                safe_count += 1
    print(safe_count)


main()