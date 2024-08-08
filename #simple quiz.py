#simple quiz

quiz_marks = []

quiz = {
    "Can AI Replace Human?": ['Yes', 'No'],
    "Is machine learning a subset of deep learning?": ['Yes', 'No']
}

answers = ['No', 'No']
user_answers = []

for question, options in quiz.items():
    print(question)
    for i , option in enumerate(options , 1):
        print(f'{i} . {option}')

    while True:
        try:
            user_input = int(input("Enter The number OF Correct option: "))
            if user_input >=1 and user_input <= len(options):
                user_answers.append(options[user_input-1])
                break
            else:
                print("Please Enter The Valid Option Number: ")
        except ValueError:
            print('Invalid, Please Inter  A number: ')

score = 0

for user_answer , correct_answer in zip(answers, user_answers):
    if user_answer == correct_answer:
        score +=1
total_questions = len(quiz)

print(f"You Scored {score} in {total_questions}")

if score==total_questions:
    print("You Passed")
else:
    print("You Failed")


   
