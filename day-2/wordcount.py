def words(a):
    b = a.split()
    split_words = []

    for x in b:
        try:
            x2 = int(x)
            split_words.append(x2)
        except:
            split_words.append(x)

    words_dict = {x: split_words.count(x) for x in split_words}

    return words_dict

a = "testing 1 2 testing 1 2"
print(words(a))