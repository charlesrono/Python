from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(c) Purple\n Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta \n(c) Yellow\n\n"
    "What color are strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n\n"


]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[0], "c"),
    Question(question_prompts[0], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        assert isinstance(question.prompt, object)
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)