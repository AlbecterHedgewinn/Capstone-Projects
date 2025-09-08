# Refactored Quiz Application

quiz_library = {
    "art": [
        ("Who painted the Mona Lisa?", "Leonardo Da Vinci"),
        ("What precious stone is used to make the artist\'s pigment ultramarine?", "Lapis Lazuli"),
        ("Anish Kapoor\'s bean-shaped Cloud Gate sculpture is a landmark of which city?", "Chicago")
    ],
    "space": [
        ("Which planet is closest to the sun?", "Mercury"),
        ("Which planet spins in the opposite direction to all the others in the solar system?", "Venus"),
        ("How many moons does Mars have?", "2")
    ]
}

def choose_topic(quiz_data):
    print("These are the Quiz Topics:")
    for ind, topic in enumerate(quiz_data.keys()):
        print(f"{ind + 1}. {topic}")

    choice = input("Which topic would you like to choose? ").strip().lower()
    if choice in quiz_data:
        return choice
    else:
        print("Invalid choice. Please choose a valid topic.")
        return choose_topic(quiz_data)
    
def run_quiz(questions):
    score = 0
    for question_text, correct_answer in questions:
        user_answer = input(f"{question_text} ").strip().lower()
        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}")
    print(f"\nQuiz completed. You scored {score} out of {len(questions)}.")
    if score == len(questions):
        print("Congratulations! You got a perfect score!")

def main():
    topic = choose_topic(quiz_library)
    run_quiz(quiz_library[topic])

main()
