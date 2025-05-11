def get_num_words(book_string: str):
    words = book_string.split()
    return len(words)


def count_chars(book_string: str):
    count = {}
    for x in book_string:
        if x.lower() in count:
            count[x.lower()] += 1
        else:
            count[x.lower()] = 1

    return count


def list_dict_char(char_count: dict):
    list_of_dicts = []

    for key in char_count:
        tmp_dict = {}

        tmp_dict["char"] = key
        tmp_dict["num"] = char_count[key]

        list_of_dicts.append(tmp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    for char_dict in list_of_dicts:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")


def sort_on(dict):
    return dict["num"]
