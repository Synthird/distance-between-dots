start_string: str = "."

print("How far do you want your two dots to be? (In characters)")
distance: int = int(input("Distance: "))

print("Do you want to show a line between the two dots?")
print("1 = Yes\nAny other number = No")
show_line: int = int(input("Show a line: "))

if show_line == 1:
    for _ in range(distance):
        start_string = f"{start_string}_"
else:
    for _ in range(distance):
        start_string = f"{start_string} "

start_string = f"{start_string}."

print(start_string)
