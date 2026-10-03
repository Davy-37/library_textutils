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

    
    
    result = {
        "characters": characters,
        "characters_no_spaces": characters_no_spaces,
        "words": words,
        "unique_words": unique_words
    }

    return result
