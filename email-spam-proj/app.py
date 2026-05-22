from flask import Flask, render_template, request

app = Flask(__name__)

spam_words = [
    "win", "free", "urgent",
    "click", "offer", "money",
    "prize", "lottery",
    "claim", "bonus",
    "otp", "bank",
    "verify", "password"
]

def classify_email(subject, body):
    score = 0

    text = (subject + " " + body).lower()

  
    for word in spam_words:
        if word in text:
            score += 2
    if "http://" in text or "https://" in text:
        score += 2
    if body.count("!") > 3:
        score += 1
    if subject.isupper():
        score += 2

    if score <= 2:
        return "SAFE EMAIL", score
    elif score <= 5:
        return "SPAM EMAIL", score
    else:
        return "PHISHING / SCAM EMAIL", score


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    score = None

    if request.method == "POST":
        subject = request.form["subject"]
        body = request.form["body"]

        result, score = classify_email(subject, body)

    return render_template(
        "index.html",
        result=result,
        score=score
    )

if __name__ == "__main__":
    app.run(debug=True)