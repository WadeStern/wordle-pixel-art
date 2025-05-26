import os

def get_feedback(guess, target):
    feedback = ['0'] * 5
    target_letters = list(target)
    used = [False] * 5

    # Greens
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = '2'
            used[i] = True

    # Yellows
    for i in range(5):
        if feedback[i] == '0':
            for j in range(5):
                if not used[j] and guess[i] == target[j]:
                    feedback[i] = '1'
                    used[j] = True
                    break

    return ''.join(feedback)

def load_words(filename):
    with open(filename) as f:
        return [line.strip().lower() for line in f if len(line.strip()) == 5]

def write_results(wordlist, target, out_dir="output"):
    os.makedirs(out_dir, exist_ok=True)
    output_file = os.path.join(out_dir, f"{target}.txt")

    with open(output_file, "w") as f:
        for guess in wordlist:
            pattern = get_feedback(guess, target)
            f.write(f"{guess} {pattern}\n")

if __name__ == "__main__":
    wordlist = load_words("words.txt")  # full guess list
    target = input("Enter the target word: ").strip().lower()

    if len(target) != 5:
        print("Target word must be 5 letters.")
        exit()

    write_results(wordlist, target)
    print(f"Output written to output/{target}.txt")
