def calculate_average(marks):
    return sum(marks) / len(marks)


def class_performance(students):
    averages = {}
    top_student = ""
    highest_avg = 0

    for name, marks in students.items():
        avg = calculate_average(marks)
        averages[name] = round(avg, 2)

        if avg > highest_avg:
            highest_avg = avg
            top_student = name

    return averages, top_student


# Example Input
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

averages, top_student = class_performance(students)

print("Average Marks:", averages)
print("Top Performer:", top_student)