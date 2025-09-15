def count_words (text):
    words = text.split()
    return len(words)


def toLower (text):
    counts = {}
    for character in text.lower():
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1
    return counts


def counting_letters (counts_dict):
    result = []
    for ch, count in counts_dict.items():
        result.append({"char": ch, "num": count})
    return result



def sort_on(item):
    return item["num"]



