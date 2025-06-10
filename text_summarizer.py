"""
A Python script to demonstrate text summarization using gensim's TextRank algorithm.
"""

import nltk
from gensim.summarization import summarize

# Download the punkt tokenizer for sentence splitting (required by gensim)
nltk.download('punkt')

def summarize_text(text, ratio=0.3):
    """
    Summarizes the input text.

    :param text: str, input text
    :param ratio: float, summary length ratio (default 0.3)
    :return: str, summary
    """
    try:
        summary = summarize(text, ratio=ratio)
        if not summary:
            return "Summary could not be generated. Try using a lower ratio or longer text."
        return summary
    except Exception as e:
        return f"Error during summarization: {e}"

if __name__ == "__main__":
    # Example input text
    input_text = """
    Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) focused on enabling computers to understand, interpret, and produce human language.
    NLP combines computational linguistics—rule-based modeling of human language—with statistical, machine learning, and deep learning models.
    These technologies enable computers to process human language in the form of text or voice data and 'understand' its full meaning, complete with the speaker or writer's intent and sentiment.
    NLP is used in applications such as speech recognition, machine translation, sentiment analysis, chatbots, and more.
    The ultimate goal of NLP is to help computers understand language as well as humans do.
    """

    print("Original Text:\n")
    print(input_text.strip())
    print("\n--- Concise Summary ---\n")

    summary = summarize_text(input_text, ratio=0.3)
    print(summary)

