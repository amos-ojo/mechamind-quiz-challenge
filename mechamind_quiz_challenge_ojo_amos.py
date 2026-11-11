"""
MECHAMIND QUIZ CHALLENGE
An interactive 10-question multiple-choice quiz on introductory mechatronics.

Student: OJO AMOS OLUWAFUNMINIYI
Course: CTE213
"""

import random

STUDENT_NAME = "OJO AMOS OLUWAFUNMINIYI"
QUIZ_TITLE = "MECHAMIND QUIZ CHALLENGE"

QUESTIONS = [
    {
        "question": "What does mechatronics combine?",
        "options": [
            "A. Mechanical engineering, electronics, computing and control",
            "B. Agriculture, accounting and marketing",
            "C. Chemistry and geography only",
            "D. Architecture and painting only",
        ],
        "answer": "A",
        "explanation": "Mechatronics integrates mechanical systems, electronics, computing and control engineering.",
    },
    {
        "question": "Which component detects a physical condition such as temperature or pressure?",
        "options": [
            "A. Actuator",
            "B. Sensor",
            "C. Gearbox",
            "D. Fuse",
        ],
        "answer": "B",
        "explanation": "A sensor detects or measures a physical quantity and provides a signal.",
    },
    {
        "question": "What is the main function of an actuator?",
        "options": [
            "A. To display computer files",
            "B. To measure resistance only",
            "C. To convert an input signal or energy into physical action",
            "D. To store program instructions",
        ],
        "answer": "C",
        "explanation": "An actuator produces movement or another physical action in a system.",
    },
    {
        "question": "What does PLC stand for?",
        "options": [
            "A. Power Logic Cable",
            "B. Program Line Control",
            "C. Process Load Computer",
            "D. Programmable Logic Controller",
        ],
        "answer": "D",
        "explanation": "PLC means Programmable Logic Controller, commonly used in industrial automation.",
    },
    {
        "question": "Which Python function is used to display output?",
        "options": [
            "A. print()",
            "B. input()",
            "C. range()",
            "D. len()",
        ],
        "answer": "A",
        "explanation": "The print() function displays text and other values on the screen.",
    },
    {
        "question": "What is the SI unit of force?",
        "options": [
            "A. Watt",
            "B. Newton",
            "C. Joule",
            "D. Volt",
        ],
        "answer": "B",
        "explanation": "Force is measured in newtons, represented by the symbol N.",
    },
    {
        "question": "Which electronic component allows current to flow mainly in one direction?",
        "options": [
            "A. Resistor",
            "B. Capacitor",
            "C. Diode",
            "D. Transformer",
        ],
        "answer": "C",
        "explanation": "A diode is designed to conduct current mainly in one direction.",
    },
    {
        "question": "Which control system uses feedback to compare actual output with a desired output?",
        "options": [
            "A. Open-loop system",
            "B. Manual-only system",
            "C. Mechanical-only system",
            "D. Closed-loop system",
        ],
        "answer": "D",
        "explanation": "A closed-loop control system uses feedback to monitor and correct its output.",
    },
    {
        "question": "What does CAD stand for in engineering?",
        "options": [
            "A. Computer-Aided Design",
            "B. Control Action Device",
            "C. Current Application Diagram",
            "D. Computer Analysis Drive",
        ],
        "answer": "A",
        "explanation": "CAD means Computer-Aided Design and is used to create technical drawings and models.",
    },
    {
        "question": "Which instrument is used to measure electric current?",
        "options": [
            "A. Voltmeter",
            "B. Ammeter",
            "C. Thermometer",
            "D. Barometer",
        ],
        "answer": "B",
        "explanation": "An ammeter measures electric current, usually in amperes.",
    },
]


def show_header():
    print("=" * 64)
    print(f"                 {QUIZ_TITLE}")
    print("                  THE 10-QUESTION TEST")
    print("=" * 64)
    print(f"Student: {STUDENT_NAME}")
    print("Course: CTE213")
    print("Instructions: Choose A, B, C or D for each question.")
    print("Each correct answer earns 10 marks. Total: 100 marks.")
    print("=" * 64)


def ask_question(number, item):
    print(f"\nQUESTION {number}/10")
    print(item["question"])
    for option in item["options"]:
        print(option)

    while True:
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in ("A", "B", "C", "D"):
            return choice
        print("Invalid choice. Please enter A, B, C or D.")


def get_grade(score):
    if score >= 80:
        return "A - Excellent"
    if score >= 70:
        return "B - Very Good"
    if score >= 60:
        return "C - Good"
    if score >= 50:
        return "D - Pass"
    return "F - Needs Improvement"


def run_quiz():
    questions = QUESTIONS[:]
    random.shuffle(questions)
    score = 0
    correct_count = 0
    wrong_answers = []

    show_header()
    input("\nPress ENTER when you are ready to begin...")

    for number, item in enumerate(questions, start=1):
        choice = ask_question(number, item)
        if choice == item["answer"]:
            print("Correct! +10 marks")
            score += 10
            correct_count += 1
        else:
            print(f"Not quite. Correct answer: {item['answer']}")
            wrong_answers.append((item["question"], choice, item["answer"]))
        print("Explanation:", item["explanation"])

    print("\n" + "=" * 64)
    print("                       QUIZ RESULTS")
    print("=" * 64)
    print(f"Student: {STUDENT_NAME}")
    print(f"Correct answers: {correct_count}/10")
    print(f"Wrong answers:   {10 - correct_count}/10")
    print(f"Final score:     {score}/100")
    print(f"Grade:           {get_grade(score)}")
    print("=" * 64)

    if wrong_answers:
        print("\nREVISION SUMMARY")
        for question, selected, correct in wrong_answers:
            print(f"\n{question}")
            print(f"Your answer: {selected} | Correct answer: {correct}")
    else:
        print("\nPerfect score! You answered every question correctly.")

    print(f"\nThank you for using {QUIZ_TITLE}!")


def main():
    while True:
        run_quiz()
        again = input("\nWould you like to take the quiz again? (Y/N): ").strip().upper()
        if again != "Y":
            print("\nGoodbye, and keep learning!")
            break


if __name__ == "__main__":
    main()
