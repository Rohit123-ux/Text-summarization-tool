from flask import Flask, request, render_template_string
import nltk
from gensim.summarization import summarize

# Download the Punkt tokenizer for gensim
nltk.download('punkt')

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Article Summarizer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        textarea { width: 100%; height: 200px; }
        .summary { margin-top: 20px; padding: 10px; background-color: #f0f0f0; }
        button { padding: 10px 20px; font-size: 16px; }
    </style>
</head>
<body>
    <h1>Article Summarizer</h1>
    <form method="post">
        <textarea name="article" placeholder="Paste your lengthy article here...">{{ article }}</textarea><br><br>
        <button type="submit">Summarize</button>
    </form>

    {% if summary %}
    <h2>Summary:</h2>
    <div class="summary">{{ summary }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    article = ""
    if request.method == "POST":
        article = request.form["article"]
        if article.strip():
            try:
                summary = summarize(article, ratio=0.3)
                if not summary:
                    summary = "Could not generate a summary. Please try with a longer or different text."
            except Exception as e:
                summary = f"Error: {e}"
    return render_template_string(HTML_TEMPLATE, summary=summary, article=article)

if __name__ == "__main__":
    app.run(debug=True)
