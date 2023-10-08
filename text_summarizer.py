import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = '''Rickrolling or a Rickroll is an Internet meme involving the unexpected appearance of the music video to the 1987 hit song "Never Gonna Give You Up", performed by English singer Rick Astley. The aforementioned video has over 1.4 billion views on YouTube. The meme is a type of bait and switch, usually using a disguised hyperlink that leads to the music video. When one clicks on a seemingly unrelated link, the site with the music video loads instead of what was expected, and they have been "Rickrolled". The meme has also extended to using the song's lyrics, or singing it, in unexpected contexts. Astley himself has also been Rickrolled on several occasions.

The meme grew out of a similar bait-and-switch trick called "duck rolling" that was popular on the 4chan website in 2006. The video bait-and-switch trick grew popular on 4chan by 2007 during April Fools' Day and spread to other Internet sites later that year. The meme gained mainstream attention in 2008 through several publicized events, particularly when YouTube used it on its 2008 April Fools' Day event.

Astley, who had only returned to performing after a 10-year hiatus, was initially hesitant about using his newfound popularity from the meme to further his career but accepted the fame by Rickrolling the 2008 Macy's Thanksgiving Day Parade with a surprise performance of the song. Since then, Astley has seen his performance career revitalized by the meme's popularity.'''


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

