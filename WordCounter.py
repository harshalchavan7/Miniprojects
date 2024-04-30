def word_counter(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == "__main__":
    text = input("Enter some text: ")
    result = word_counter(text)
    print("\nWord count:")
    for word, count in result.items():
        print(f"{word}: {count}")
