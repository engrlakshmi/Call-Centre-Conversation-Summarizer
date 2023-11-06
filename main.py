from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

app = Flask(__name__)

# Initialize the summarization model
summarizer = pipeline(
    task="summarization",
    model="t5-small",
    min_length=20,
    max_length=40,
    truncation=True,
    model_kwargs={"cache_dir": '/Documents/Huggin_Face/'},
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize_text():
    input_text = request.form['input_text']

    if input_text:
        # Generate the summary
        output = summarizer(input_text, max_length=150, min_length=30, do_sample=False)
        summary = output[0]['summary_text']
        return render_template("index.html", summary=summary)
    else:
        return render_template("index.html", error="Please provide text to summarize")

if __name__ == '__main__':
    app.run()
