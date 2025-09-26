classes = [[1,2],[3,5],[2,2]]

def return_average(classes):
    class_score = 0
    for student_class in classes:
        class_score += student_class[0] / student_class[1]
        print(f"class score: {class_score}")
    return  class_score / len(classes)


print(return_average(classes))
for i in range(len(classes)):
    classes[i][0] += 3
    classes[i][0] -= 3 

print(return_average(classes))
print(classes)


