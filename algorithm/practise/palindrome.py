def palindrome(word: str):
    word_list = list(word)
    while(len(word_list) > 1):
        if word_list.pop(0) != word_list.pop():
            return False
    return True

def reverse_check(word: str):
    word_reversed = list(word)
    word_reversed.reverse()
    if list(word) != word_reversed:
        return False
    else:
        return True

    
if __name__ == "__main__":
    word = "1321"
    print(palindrome(word))
    print(reverse_check(word))