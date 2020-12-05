from src.common.common import get_lines


def get_seat_row(boarding_pass):
	rows = range(128)
	# print(rows)
	for char in boarding_pass[:7]:
		half = int(len(rows) // 2)
		if char == 'F':
			rows = rows[:half]
		elif char == 'B':
			rows = rows[half:]
		else:
			print("ERROR")
		# print(char, rows)
	return rows.start


def get_seat_col(boarding_pass):
	cols = range(8)
	# print(cols)
	for char in boarding_pass[7:]:
		half = int(len(cols) // 2)
		if char == 'L':
			cols = cols[:half]
		elif char == 'R':
			cols = cols[half:]
		else:
			print("ERROR")
		# print(char, cols)
	return cols.start


def get_seat_id(boarding_pass):
	row = get_seat_row(boarding_pass)
	col = get_seat_col(boarding_pass)
	return row * 8 + col


boarding_passes = get_lines()

all_seat_ids = list(map(get_seat_id, boarding_passes))

for id in range(min(all_seat_ids), max(all_seat_ids)):
	if id not in all_seat_ids:
		print(id)
