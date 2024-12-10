start_dot: str = "."


def input_number(input_message: str) -> int:
    try:
        number: int = int(input(f"{input_message}: "))
        return number
    except:
        print(
            "You typed something that isn't a whole number or a whole number with decimals!")
        raise SystemExit


print("How many characters are between the two dots?")
characters: int = input_number("Characters")

print("Do you want to show a line between the two dots?")
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
