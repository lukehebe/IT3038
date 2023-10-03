def count_letters_vowels_consonants(word):
   
    letter_count = 0
    vowel_count = 0
    consonant_count = 0
    vowels = set("AEIOUaeiou")

    for char in word:

        if char.isalpha():
            letter_count += 1
         
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return letter_count, vowel_count, consonant_count

if __name__ == "__main__":
    word = input("Enter a word: ")
    letter_count, vowel_count, consonant_count = count_letters_vowels_consonants(word)

    print(f"Number of letters: {letter_count}")
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")







R
