start_dot: str = "."


def exit_with_possible_reasons() -> None:
	print("!!! Cannot print dots! !!!")
	print("Probably because you entered:")
	print("a) Decimals")
	print("b) Letters")
	print("c) Symbols")
	print("d) A negative number")
	print("e) You exited the program")
	raise SystemExit


def input_number(input_message: str) -> int:
	number: int = 0

	try:
		number = int(input(f"{input_message}: ").replace(" ", ""))
	except:
		exit_with_possible_reasons()

	if number > -1:
		return number
	else:
		exit_with_possible_reasons()


def ask_question(question: str) -> None:
	print(f"--- {question}? ---")


ask_question("How many characters are between the two dots")
characters: int = input_number("Characters")

ask_question("Show a line between them")
print("1 = Yes")
print("Any other number = No")
show_line: int = input_number("Show a line")

if show_line == 1:
	for _ in range(characters):
		start_dot = f"{start_dot}_"
else:
	for _ in range(characters):
		start_dot = f"{start_dot} "

print(f"{start_dot}.")
