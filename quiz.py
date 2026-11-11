# MECHATRONICS QUIZ APP
# ND2 Mechatronics Engineering Project

# Get student's ND level using integer conversion
try:
    nd_level = int(input("Enter your ND level (1 or 2): "))

    if nd_level not in [1, 2]:
        print("Invalid ND level. Enter 1 or 2.")
        exit()

except ValueError:
    print("Invalid input! Please enter a number.")
    exit()


# Store quiz questions in a list
questions = [
    "What does PLC stand for?",
    "Which component detects physical changes?",
    "What is the unit of electrical resistance?",
    "Which system uses compressed air?",
    "What does CPU stand for?",
    "Which device converts electrical energy to mechanical energy?",
    "What is the unit of pressure?",
    "Which programming language are we using?"
]

# Store answer options in a list
options = [
    ["A. Programmable Logic Controller", "B. Power Line Control", "C. Personal Logic Computer"],
    ["A. Motor", "B. Sensor", "C. Battery"],
    ["A. Volt", "B. Ampere", "C. Ohm"],
    ["A. Hydraulic", "B. Pneumatic", "C. Electrical"],
    ["A. Central Processing Unit", "B. Computer Power Unit", "C. Control Processing Utility"],
    ["A. Motor", "B. Resistor", "C. Capacitor"],
    ["A. Pascal", "B. Ohm", "C. Watt"],
    ["A. Java", "B. Python", "C. C++"]
]

# Store correct answers
answers = ["A", "B", "C", "B", "A", "A", "A", "B"]


# Function to collect a valid answer
def get_answer():
    while True:
        choice = input("Enter A, B or C: ").upper()

        if choice in ["A", "B", "C"]:
            return choice
        else:
            print("Invalid answer! Enter A, B or C.")


# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 40:
        return "Fair"
    else:
        return "Needs Improvement"


# Main quiz function
def start_quiz():
    score = 0
    wrong_answers = []

    print("\nWELCOME TO MECHATRONICS QUIZ APP")
    print("ND Level:", nd_level)
    print("--------------------------------")

    # Display each question
    for i in range(len(questions)):
        print("\nQuestion", i + 1)
        print(questions[i])

        for option in options[i]:
            print(option)

        user_answer = get_answer()

        # Check the answer
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
            wrong_answers.append(i)

    # Calculate percentage
    percentage = (score / len(questions)) * 100

    print("\n======= QUIZ RESULT =======")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(wrong_answers))
    print("Percentage:", percentage, "%")
    print("Grade:", calculate_grade(percentage))

    # Special feature: review wrong answers
    if len(wrong_answers) > 0:
        print("\nREVIEW YOUR MISTAKES")

        for i in wrong_answers:
            print(questions[i])
            print("Correct answer:", answers[i])
    else:
        print("Congratulations! All answers are correct!")


# Start the quiz
start_quiz()
