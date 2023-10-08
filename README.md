# Text-Summarizer


# Text Summarizer using Spacy and Word Frequency

This Python script provides a simple text summarization function using Spacy, a popular natural language processing library, and word frequency analysis. The summarizer generates a summary of a given text by extracting the most relevant sentences.

## How to Use

1. **Dependencies**
   - Ensure you have the following dependencies installed:
     - Spacy (`pip install spacy`)
     - SpaCy's English language model (`python -m spacy download en_core_web_md`)

2. **Function**
   - Import the necessary modules:
     ```python
     import spacy
     from spacy.lang.en.stop_words import STOP_WORDS
     from string import punctuation
     from heapq import nlargest
     ```

3. **Summarization Function**
   - Define the `summarizer` function:
     ```python
     def summarizer(text):
         # Code for summarization goes here
         # ...
         return summary, len(text.split(' ')), len(summary.split(' '))
     ```

4. **Input**
   - Call the `summarizer` function, passing the text you want to summarize as an argument:
     ```python
     text_to_summarize = "Your input text goes here."
     summary, original_word_count, summary_word_count = summarizer(text_to_summarize)
     ```

5. **Output**
   - `summary`: The summarized text
   - `original_word_count`: The word count of the original text
   - `summary_word_count`: The word count of the summary

## Algorithm Overview

1. **Preprocessing**
   - Load the Spacy language model and tokenize the input text into words.
   - Remove stop words and punctuation from the tokens.
   - Calculate word frequencies.

2. **Scoring Sentences**
   - Score each sentence based on the sum of the normalized frequencies of its constituent words.

3. **Summary Generation**
   - Select the top 30% of sentences based on their scores to form the summary.

4. **Return**
   - Return the summary and word counts for evaluation.

## Acknowledgments
- This code utilizes the Spacy library and the English language model provided by SpaCy. For more information, visit [Spacy](https://spacy.io/).

## License
This code is provided under the [MIT License](LICENSE).

Feel free to modify and use this code for your projects!
