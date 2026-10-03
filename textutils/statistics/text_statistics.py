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
    
    characters_no_spaces = 0
    for i in range(len(text)):
        if text[i] != " ":
            characters_no_spaces += 1
            
    words = len(text.split())
    
    normalized_text = text.replace(".", " ").replace("!", " ").replace("?", " ").replace(",", " ").replace(";", " ")
    normalized_words = normalized_text.lower().split()
    unique_words = len(set(normalized_words))
    
    all_sentences = re.split(r'[.!?]+', text)
    sentences = 0
    for i in range(len(all_sentences)):
        if all_sentences[i].strip() != "":
            sentences += 1

    characters_words = 0
    for i in range(len(normalized_words)):
        characters_words += len(normalized_words[i])
    
    if words != 0: 
        average_word_length = characters_words / words
    else :
        average_word_length = 0.0
    
    if len(normalized_words) != 0:   
        characters_shortest_word = len(normalized_words[0])
        shortest_word = normalized_words[0]
        for i in range(1,len(normalized_words)):
            if characters_shortest_word > len(normalized_words[i]):
                characters_shortest_word = len(normalized_words[i])
                shortest_word = normalized_words[i]
                
            if characters_shortest_word == len(normalized_words[i]):
                if shortest_word > normalized_words[i]:
                    characters_shortest_word = len(normalized_words[i])
                    shortest_word = normalized_words[i]
    else:
        shortest_word = None
        
    if len(normalized_words) != 0:   
        characters_longest_word = len(normalized_words[0])
        longest_word = normalized_words[0]
        for i in range(1,len(normalized_words)):
            if characters_longest_word < len(normalized_words[i]):
                characters_longest_word = len(normalized_words[i])
                longest_word = normalized_words[i]
                
            if characters_longest_word == len(normalized_words[i]):
                if longest_word > normalized_words[i]:
                    characters_longest_word = len(normalized_words[i])
                    longest_word = normalized_words[i]
    else:
        longest_word = None
    
    number_by_word = {}
    for word in normalized_words:
        if word in number_by_word:
            number_by_word[word] += 1
        else:
            number_by_word[word] = 1
            
    

    most_frequent_word = None
    most_frequent_count = 0
    for word in number_by_word:
        if most_frequent_count < number_by_word[word]:
            most_frequent_word = word
            most_frequent_count = number_by_word[word]
        if most_frequent_count == number_by_word[word]:
            if most_frequent_word > word:
                most_frequent_word = word
                most_frequent_count = number_by_word[word]
                
    result = {
        "characters": characters,
        "characters_no_spaces": characters_no_spaces,
        "words": words,
        "unique_words": unique_words,
        "sentences": sentences,
        "average_word_length": average_word_length,
        "shortest_word": shortest_word,
        "longest_word": longest_word,
        "most_frequent_word": most_frequent_word,
        "most_frequent_count": most_frequent_count
    }
    
    return result
