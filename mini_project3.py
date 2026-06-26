# Quiz app in python

def run_quiz():
 questions = [
   {
    "question": "What is the capital of France?", 
    "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
      "answer": "C : Paris"
    },
    {"question": "What is the largest planet in our solar system?", 
    "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
      "answer": "B : Jupiter"
    },
   {"question": "What is the chemical symbol for gold?", 
    "options": ["A) Au", "B) Ag", "C) Fe", "D) Hg"],
      "answer": "A : Au"
   },
   {"question": "Who wrote the play 'Romeo and Juliet'?", 
    "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Jane Austen"],
      "answer": "A : William Shakespeare"
    },
   {"question": "What is the largest ocean on Earth?", 
    "options":["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
      "answer": "D : Pacific Ocean"
  }
 ]

 score = 0
 for index, q in enumerate(questions):
    print(f"Question {index + 1}: {q['question']}")
    for option in q["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
    if user_answer == q["answer"][0]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The correct answer is: {q['answer']}\n")

    print(f"Your final score is: {score}/{len(questions)}")
 
run_quiz()