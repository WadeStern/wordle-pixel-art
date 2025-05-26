import os
import argparse

def search_pattern(target, pattern, out_dir="output"):
    path = os.path.join(out_dir, f"{target}.txt")
    try:
        with open(path) as f:
            found = False
            for line in f:
                word, feedback = line.strip().split()
                if feedback == pattern:
                    print(word)
                    found = True
            if not found:
                print(f"No matches found for pattern {pattern}.")
    except FileNotFoundError:
        print(f"No file found for target word: {target}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for words matching a Wordle pattern.")
    parser.add_argument("--word", required=True, help="The target word (e.g., stone)")
    parser.add_argument("--pattern", required=True, help="The feedback pattern (e.g., 01010)")

    args = parser.parse_args()

    if len(args.pattern) != 5 or any(c not in "012" for c in args.pattern):
        print("Invalid pattern. Must be 5 digits using only 0 (gray), 1 (yellow), or 2 (green).")
        exit()

    search_pattern(args.word.lower(), args.pattern)
