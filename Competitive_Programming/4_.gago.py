def correct(text):
    words = text.split()
    words_corrected = []

    for word in words:
        if len(word) >= 4 and word[:2] == word[2:4]:
            word_corrected = word[2:]
        else:
            word_corrected = word
        
        words_corrected.append(word_corrected)

    return ' '.join(words_corrected)

text = input()

texto_corrigido = correct(text)

print(texto_corrigido)
