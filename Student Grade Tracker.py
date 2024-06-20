def calculate_letter_grade(average):
    if average >= 90:
        return 'A', 4.0
    elif average >= 80:
        return 'B', 3.0
    elif average >= 70:
        return 'C', 2.0
    elif average >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def main():
    grades = {}
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            grades[subject] = grade
        except ValueError:
            print("Invalid grade. Please enter a number.")
    
    if grades:
        total = sum(grades.values())
        count = len(grades)
        average = total / count
        letter_grade, gpa = calculate_letter_grade(average)
        
        print("\nGrade Summary:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA: {gpa:.2f}")
    else:
        print("No grades entered.")

if __name__ == "__main__":
    main()
