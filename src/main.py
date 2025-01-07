start_dot: str = "."


def exit_with_message(message: str) -> None:
	print(message)
	raise SystemExit


def input_number(input_message: str) -> int:
	try:
		return int(input(f"{input_message}: ").replace(" ", ""))
	except ValueError:
		exit_with_message("Please enter a whole number without any decimals....")
	except KeyboardInterrupt:
		exit_with_message("\nYou exited the program!")


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
