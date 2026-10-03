import re

def text_statistics(text):
    """
    Calculate statistics about a text.

    Args:
    text (str): The text to analyze.

    Returns:
    dict: A dictionary containing the statistics of the text.
    """
    characters = len(text)
    
    characters_no_spaces =0
    for i in range(len(text)):
        if text[i] != " ":
            characters_no_spaces += 1
            
    words = len(text.split())
    
    normalizer_text = text.replace(".", " ").replace("!", " ").replace("?", " ").replace(",", " ").replace(";", " ")
    normalizer_words = normalizer_text.lower().split()
    unique_words = len(set(normalizer_words))
    
    all_sentences = re.split(r'[.!?]+', text)
    sentences = 0
    for i in range (len(all_sentences)):
        if all_sentences[i].strip() != "":
            sentences +=1

    characters_words = 0
    for i in range(len(normalizer_words)):
        characters_words += len(normalizer_words[i])
    
    if words != 0: 
        average_word_length = characters_words / words
    else :
        average_word_length = 0.0
    
    if len(normalizer_words) != 0:   
        characters_shortest_word = len(normalizer_words[0])
        shortest_word = normalizer_words[0]
        for i in range(1,len(normalizer_words)):
            if characters_shortest_word > len(normalizer_words[i]):
                characters_shortest_word = len(normalizer_words[i])
                shortest_word = normalizer_words[i]
                
            if characters_shortest_word == len(normalizer_words[i]):
                if shortest_word > normalizer_words[i]:
                    characters_shortest_word = len(normalizer_words[i])
                    shortest_word = normalizer_words[i]
    else:
        shortest_word = None
        
    if len(normalizer_words) != 0:   
        characters_longest_word = len(normalizer_words[0])
        longest_word = normalizer_words[0]
        for i in range(1,len(normalizer_words)):
            if characters_longest_word < len(normalizer_words[i]):
                characters_longest_word = len(normalizer_words[i])
                longest_word = normalizer_words[i]
                
            if characters_longest_word == len(normalizer_words[i]):
                if longest_word > normalizer_words[i]:
                    characters_longest_word = len(normalizer_words[i])
                    longest_word = normalizer_words[i]
    else:
        longest_word = None
    
    result = {
        "characters": characters,
        "characters_no_spaces": characters_no_spaces,
        "words": words,
        "unique_words": unique_words,
        "sentences": sentences,
        "average_word_length": average_word_length,
        "shortest_word": shortest_word,
        "longest_word": longest_word
    }

    return result
