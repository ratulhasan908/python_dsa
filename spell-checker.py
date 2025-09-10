from spellchecker import SpellChecker

corrector = spellchecker()

word = input("Enter your word ")

if word in spellchecker:
    print(word)
else:
    correct_word = corrector(word)
    print(correct_word)