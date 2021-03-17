from Questions import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green \n(b) Yellow\n(c) Blue",
    "What color are bananas?\n(a) Red/Green \n(b) Yellow\n(c) Blue",
    "What color are strawberries?\n(a) Red \n(b) Yellow\n(c) Blue",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]


def run_Test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt + "\n")
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_Test(questions)