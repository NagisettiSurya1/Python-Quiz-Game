def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
            "answer": "A"
        },
        {
            "question": "2 + 2 = ?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "Which is the largest planet in our Solar System?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
            "answer": "C"
        },
        {
            "question": "Who wrote the national anthem of India?",
            "options": ["A) Rabindranath Tagore", "B) Bankim Chandra Chatterjee", "C) Mahatma Gandhi", "D) Sarojini Naidu"],
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A) Ag", "B) Au", "C) Gd", "D) Go"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Mars", "B) Mercury", "C) Saturn", "D) Neptune"],
            "answer": "A"
        }
    ]
    
    score = 0
    total_questions = len(questions)

    print("\n📌 **Type 'EXIT' to quit anytime, 'SCORE' to view your score**\n")
    
    for i, q in enumerate(questions, start=1):
        print(f"\nQ{i}. {q['question']}")
        for opt in q["options"]:
            print(opt)
        
        while True:
            ans = input("Your answer (A/B/C/D): ").strip().upper()
            
            # Special commands
            if ans == "EXIT":
                print(f"\n🚪 You exited the quiz. Final Score: {score}/{i-1}")
                return
            elif ans == "SCORE":
                print(f"📊 Current score: {score}/{i-1}\n")
                continue  # Ask the same question again
            
            # Validate answer
            if ans in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Enter A, B, C, D, or a command (SCORE/EXIT).")

        # Check correctness
        if ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")
    
    print(f"🎯 Quiz Over! Your Score: {score}/{total_questions}")


if __name__ == "__main__":
    quiz_game()
