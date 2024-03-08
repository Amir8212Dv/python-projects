import sys


def clear_lines(lines=1):
    for _ in range(lines):
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear line
