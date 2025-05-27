# Wordle Pattern Finder

This tool helps you explore Wordle feedback patterns to generate "pixel art" using Wordle guesses. It supports:

- Generating feedback patterns for a given target word
- Searching for guess words that produce a specific pattern (e.g., green-gray-yellow)
- Interactive frontend to visualize patterns

## Setup

1. Clone this repo
2. Make sure Python 3 is installed
3. Create and activate a virtual environment:

### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Scripts:

### Generate Feedback Data
Run this script to create a file that maps each guess word to its feedback pattern for a given target word.

Command:
python3 generate_patterns.py --target <target_word>

Example:
python3 generate_patterns.py --target stone

This creates a file at:
output/stone.txt

Containing lines like:
crane 20202
glove 01010

### Search for a Specific Pattern
To find all guess words that would produce a specific feedback pattern for a given target word, run:

Command:
python3 pattern_finder.py --word stone --pattern 01010

This will print all guess words from output/stone.txt that match the feedback pattern 01010.

Feedback Key:
0 = Gray (letter not in the word)
1 = Yellow (right letter, wrong position)
2 = Green (right letter, right position)

Example:
Pattern 20202 → green, gray, green, gray, green
