import sys
if len(sys.argv) < 2:
    print("ERROR: Please provide a list of numbers as parameters.")
    print("Usage: python3 even_odd_counter.py <NUM1> <NUM2> ... <NUMN>")
    sys.exit(1)
numbers = list(map(int, sys.argv[1:]))

print("\n=== INPUT RECEIVED FROM PARAMETERS ===")
print("Numbers:", numbers)
even_count = sum(1 for n in numbers if n % 2 == 0)
odd_count = sum(1 for n in numbers if n % 2 != 0)
print("\n===== RESULT =====")
print("Count of Even Numbers:", even_count)
print("Count of Odd Numbers:", odd_count)
