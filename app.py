from flask import Flask, request, render_template, jsonify
from collections import defaultdict

app = Flask(__name__)

# Load word list once at startup
with open("words.txt") as f:
    WORD_LIST = [line.strip().lower() for line in f if len(line.strip()) == 5]

def get_feedback(guess, target):
    feedback = ['0'] * 5
    target_letters = list(target)
    used = [False] * 5

    # Green pass
    for i in range(5):
        if guess[i] == target[i]:
            feedback[i] = '2'
            used[i] = True

    # Yellow pass
    for i in range(5):
        if feedback[i] == '0':
            for j in range(5):
                if not used[j] and guess[i] == target[j]:
                    feedback[i] = '1'
                    used[j] = True
                    break

    return ''.join(feedback)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate")
def generate():
    target = request.args.get("target", "").strip().lower()
    if len(target) != 5 or not target.isalpha():
        return jsonify({"error": "Target word must be 5 letters."}), 400

    results = []
    for guess in WORD_LIST:
        pattern = get_feedback(guess, target)
        results.append({"word": guess, "pattern": pattern})

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
