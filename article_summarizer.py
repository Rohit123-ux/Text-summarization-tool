import nltk
from gensim.summarization import summarize

# Download the Punkt tokenizer
nltk.download('punkt')

def summarize_text(text, ratio=0.3):
    """
    Summarizes the input text using gensim's TextRank algorithm.

    :param text: str, input article text
    :param ratio: float, fraction of text to include in summary
    :return: str, concise summary
    """
    try:
        summary = summarize(text, ratio=ratio)
        if not summary:
            return "Summary could not be generated. Try a lower ratio or longer text."
        return summary
    except Exception as e:
        return f"Error during summarization: {e}"

if __name__ == "__main__":
    # Example lengthy article text
    article_text = """
    Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction
    between computers and humans through natural language. The ultimate goal of NLP is to read, decipher,
    understand, and make sense of human languages in a manner that is valuable. NLP is used in a variety of
    applications such as sentiment analysis, machine translation, chatbots, and more. It combines computational
    linguistics with statistical, machine learning, and deep learning models to process human language data.
    The field has seen significant advancements in recent years, driven by the availability of large datasets
    and powerful computing resources. NLP has become an integral part of many modern applications, enhancing
    human-computer interaction and enabling new capabilities.
    """

    print("\n=== Original Text ===\n")
    print(article_text.strip())

    # Generate concise summary
    summary = summarize_text(article_text, ratio=0.3)

    print("\n=== Concise Summary ===\n")
    print(summary)
