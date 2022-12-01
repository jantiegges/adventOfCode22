# Part 1
calories = [0]

with open("./1_Calorie_Counting/input.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            calories.append(0)
            continue
        calories[-1] += int(line)

print(f"Maximum calories: {max(calories)}")

# Part 2
top_three = sorted(calories, reverse=True)[:3]
print(f"Sum of top three: {sum(top_three)}")