from src.common.common import get_lines


all_answers = get_lines()

total = 0
group_questions = set()

for person in all_answers:
    if person:
        for question in person:
            group_questions.add(question)
    else:
        total += len(group_questions)
        group_questions = set()

total += len(group_questions)

print(total)
