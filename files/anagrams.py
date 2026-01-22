
from anagram_checker import AnagramChecker

def display_menu():
    print("ANAGRAM CHECKER")
    print("1. Enter a word to find its anagrams")
    print("2. Exit")

def get_user_choice():
    while True:
        try:
            choice = input("\nEnter your choice (1 or 2): ").strip()
            if choice in ['1', '2']:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            return '2'

def validate_word(word):
    if not word:
        return False,
    words = word.split()
    if len(words) > 1:
        return False,
    word = words[0]

    if not word.isalpha():
        return False,
    
    word = word.strip()
    
    return True, word

def main():

    print("Initializing Anagram Checker...")
    
    try:
       
        checker = AnagramChecker()
        
        if not checker.word_list:
            print("Failed to load word list. Please check the file.")
            return
    except Exception as e:
        print(f"Error initializing Anagram Checker: {e}")
        return
    
    print("Anagram Checker initialized successfully!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '2':
            print("Thank you for using Anagram Checker. Goodbye! ")
            break
        
        user_input = input("Enter a word: ").strip()
        
        is_valid, result = validate_word(user_input)
        
        if not is_valid:
            print(f" Error: {result}")
            continue
        
        word = result.lower()
  
        if not checker.is_valid_word(word):
            print(f"'{word}' is NOT a valid English word.")
            continue
        
        print(f"'{word}' is a valid English word!")
 
        anagrams = checker.get_anagrams(word)

        print(f"YOUR WORD: '{word}'")
        
        if anagrams:
            print(f"Found {len(anagrams)} anagram(s):")
            anagrams_str = ", ".join(anagrams)
            print(f"Anagrams for your word: {anagrams_str}")
        else:
            print("No anagrams found for this word.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()