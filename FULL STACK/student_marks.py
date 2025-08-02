scores = []

score1 = int(input("enter score 1 (0-100):"))
scores.append(score1)

score2 = int(input("enter score 2 (0-100):"))
scores.append(score2)

score3 = int(input("enter score 3 (0-100):"))
scores.append(score3)

score4 = int(input("enter score 4 (0-100):"))
scores.append(score4)

score5 = int(input("enter score 5 (0-100):"))
scores.append(score5)

average = sum(scores)/len(scores)
highest = max(scores)
lowest = min(scores)

print("\nScores entered:", scores)
print("Average score:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)

