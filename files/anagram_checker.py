
class AnagramChecker:
    def __init__(self):
        try:
            with open("files/sowpods.txt", 'r') as file:
                self.word_list = [word.strip().lower() for word in file.readlines()]
        except FileNotFoundError:
            print(f"Error: File not found.")
            print("Please ensure the word list file is in the same directory.")
            self.word_list = []
    
    def is_valid_word(self, word):
        return word.lower() in self.word_list
    
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    
    def get_anagrams(self, word):
        anagrams = []
        word_lower = word.lower()
        
        for dictionary_word in self.word_list:
            if self.is_anagram(word_lower, dictionary_word) and dictionary_word != word_lower:
                anagrams.append(dictionary_word)
        
        return anagrams