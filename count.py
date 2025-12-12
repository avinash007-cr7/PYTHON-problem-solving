def count_subsequence(genome, sequence):
    leng = 0
    for i in genome:
        leng += 1
    lens = 0
    for i in sequence:
        lens += 1
    if (lens == 0 or lens > leng):
        return 0
    count = 0
    i = 0
    while i <= leng - lens:
        flag = True
        j = 0
        while j < lens:
            if genome[i + j] != sequence[j]:
                flag = False
                break
            j += 1

        if flag:
            count += 1
        i += 1
    return count

genome = input("Enter the genome: ")
sequence = input("Enter the sequence: ")

result = count_subsequence(genome, sequence)
print("The number of occurrences is:", result)
