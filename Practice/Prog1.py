n = 5  # You can adjust the size of the butterfly

for i in range(-n + 1, n):
    spaces = abs(i)
    stars = 2 * (n - spaces)
    print(" " * spaces + "*" * stars)

