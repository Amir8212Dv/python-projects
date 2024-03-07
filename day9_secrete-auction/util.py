import sys


def clear_lines(n):
    for _ in range(n):
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line
