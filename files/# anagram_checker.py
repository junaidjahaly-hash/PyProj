
class AnagramChecker:
    def __init__(self):
        try:
            with open("files/sowpods.txt", 'r') as file:
                self.word_list = [word.strip().upper() for word in file.readlines()]
        except FileNotFoundError:
            print(f"Error: File not found.")
            print("Please ensure the word list file is in the same directory.")
            self.word_list = []
    
    def is_valid_word(self, word):
        return word.upper() in self.word_list
    
    def is_anagram(self, word1, word2):
        return sorted(word1.upper()) == sorted(word2.upper())
    
    def get_anagrams(self, word):
        anagrams = []
        word_upper = word.upper()
        
        for dictionary_word in self.word_list:
            if self.is_anagram(word_upper, dictionary_word) and dictionary_word != word_upper:
                anagrams.append(dictionary_word)
        
        return anagrams