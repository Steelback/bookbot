
counters = [0] * 26
letters = []

def main():
    book = load_book("books/Frankenstein.txt")
    book = book.lower()


    for letter in book:
        letter = ord(letter) - 97
        if(letter >= 0 & letter <=26):
            counters[letter] += 1

    for i in range(26):
        letters.append(chr(i + 97))

    for i in range(26):
        for j in range(25 - i):
            if counters[j] < counters[j + 1]:
                swap_letters(j)

    print("Here is a summery of the letter counts in the book:-")
    print("====================================================")
    print()
    for i in range(26):
        print(letters[i], ": ", counters[i])

    print()
    print("--- End of report ---")
    

def load_book(file_path):
    with open(file_path) as f:
        return f.read()
    
def swap_letters(first_index):
    letter_tmp = letters[first_index]
    counter_tmp = counters[first_index]
    letters[first_index] = letters[first_index + 1]
    letters[first_index + 1] = letter_tmp
    counters[first_index] = counters[first_index + 1]
    counters[first_index + 1] = counter_tmp
    
        
main()