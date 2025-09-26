##### SOLUTION ######
def checkNoZero(x):
    return "0" not in str(x)
answer = []
n = 6
for i in range(n):
    b = n - i
    if checkNoZero(i) and checkNoZero(b):
        answer.append(i)
        answer.append(b)

print(answer)
    