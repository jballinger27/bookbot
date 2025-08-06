def number_of_words(text):
    return len(text.split())

def character_usage(text):
    usage = {}
    for char in text.lower():
        if(char in usage):
            usage[char] += 1
        else :
            usage[char] = 1
    return usage

def sort_usage(usage_dict):
    sorted_usage = []
    for character in usage_dict.keys():
        if character.isalpha():
            pair = {"char": character, "num": usage_dict[character]}
            sorted_usage.append(pair)
    sorted_usage.sort(reverse=True, key=lambda x: x["num"])
    return sorted_usage
