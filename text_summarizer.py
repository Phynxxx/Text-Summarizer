import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


def summarizer(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_md')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    word_freq = {}
    for word in doc:
        if word.text.lower() not in STOP_WORDS and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] /= max_freq
    sentence_tokens = [sentence for sentence in doc.sents]
    sentence_score = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text in word_freq:
                if sent not in sentence_score.keys():
                    sentence_score[sent] = word_freq[word.text]
                else:
                    sentence_score[sent] += word_freq[word.text]
    select_len = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_len, sentence_score, key=sentence_score.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    return summary, len(text.split(' ')), len(summary.split(' '))

