import nltk
from gensim.summarization import summarize

# Download the punkt tokenizer for sentence splitting
nltk.download('punkt')

def summarize_text(text, ratio=0.2):
    """
    Summarize a given text using Gensim's TextRank algorithm.
    
    Parameters:
        text (str): The input text to summarize.
        ratio (float): The fraction of sentences in the original text to include in the summary (default: 0.2).
        
    Returns:
        str: The summarized text.
    """
    try:
        summary = summarize(text, ratio=ratio)
        if not summary:
            return "Summary could not be generated. Try adjusting the ratio or using a longer text."
        return summary
    except Exception as e:
        return f"Error in summarizing: {e}"

if __name__ == "__main__":
    # Example usage
    print("Enter the text to summarize (end input with Ctrl+D or Ctrl+Z on Windows):\n")
    input_text = ""
    try:
        while True:
            line = input()
            input_text += line + "\n"
    except EOFError:
        pass
    
    if input_text.strip():
        print("\n--- Summary ---\n")
        result = summarize_text(input_text)
        print(result)
    else:
        print("No text provided.")

