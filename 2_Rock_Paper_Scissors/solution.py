def get_score_s1(hand1, hand2):
    match hand2:
        case "X":
            match hand1:
                case "A":
                    return 3 + 1
                case "B":
                    return 0 + 1
                case "C":
                    return 6 + 1
        case "Y":
            match hand1:
                case "A":
                    return 6 + 2
                case "B":
                    return 3 + 2
                case "C":
                    return 0 + 2
        case "Z":
            match hand1:
                case "A":
                    return 0 + 3
                case "B":
                    return 6 + 3
                case "C":
                    return 3 + 3

def get_score_s2(hand1, hand2):
    match hand2:
        case "X":
            match hand1:
                case "A": # Rock
                    return 0 + 3
                case "B": # Paper
                    return 0 + 1
                case "C": # Scissors
                    return 0 + 2
        case "Y":
            match hand1:
                case "A":
                    return 3 + 1
                case "B":
                    return 3 + 2
                case "C":
                    return 3 + 3
        case "Z":
            match hand1:
                case "A":
                    return 6 + 2
                case "B":
                    return 6 + 3
                case "C":
                    return 6 + 1

with open ('./2_Rock_Paper_Scissors/input.txt', 'r') as f:
    score_s1 = 0
    score_s2 = 0
    for line in f:
        hand1, hand2 = line.split()
        score_s1 += get_score_s1(hand1, hand2)
        score_s2 += get_score_s2(hand1, hand2)

print(f"Score for strategy 1: {score_s1}")
print(f"Score for strategy 2: {score_s2}")