from src.common.common import get_lines


all_answers = get_lines()

total = 0
group_questions = {}
group_size = 0

for person in all_answers:
	if person:
		for question in person:
			group_questions.setdefault(question, 0)
			group_questions[question] += 1
		group_size += 1
	else:
		total += list(group_questions.values()).count(group_size)
		group_questions = {}
		group_size = 0

total += list(group_questions.values()).count(group_size)

print(total)
