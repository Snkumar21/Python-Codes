# Example of quiz making project in python...

import json

def load_questions(topic):
    """Load questions based on the selected topic"""
    questions = {
        "math": [
            {"question": "What is 5 + 3?", "options": ["6", "8", "10", "7"], "answer": "8"},
            {"question": "What is 12 / 4?", "options": ["2", "3", "4", "6"], "answer": "3"},
        ],
        "science": [
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
            {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
        ]
    }
    return questions.get(topic.lower(), [])

def ask_questions(questions):
    """Ask each question and get user's answers"""
    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for i, option in enumerate(q["options"], 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                choice = int(input("Your answer (1-4): "))
                if 1 <= choice <= 4:
                    break
                else:
                    print("Invalid choice, please select 1-4.")
            except ValueError:
                print("Please enter a number between 1 and 4.")
        
        if q["options"][choice - 1] == q["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}")
    
    return score

def main():
    print("Welcome to the Personalized Quiz! 🎯")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Choose a topic: Math or Science")
    
    while True:
        topic = input("Enter topic: ").strip().lower()
        if topic in ["math", "science"]:
            break
        else:
            print("Invalid topic. Please choose 'Math' or 'Science'.")
    
    questions = load_questions(topic)
    if not questions:
        print("No questions available for this topic.")
        return
    
    score = ask_questions(questions)
    print(f"\n{name}, you scored {score}/{len(questions)}! 🎉")

if __name__ == "__main__":
    main()
