def get_counter(pair):
    """Return the count from a (word, count) pair for sorting."""
    return pair[1]


def word_frequency():
    """Word counter"""
    # Convert text to lowercase
    text = "How to use this in Notion: Create a new blank page, then paste this entire document in (Cmd/Ctrl+V). Notion auto-converts the headers, checkboxes, and tables into native blocks. Then import Notion_Daily_Tracker.csv (File → Import → CSV) as your daily-log database — that becomes your day-by-day checklist and notes table linked to this syllabus."
    lower_text = text.lower()

    #Remove punctuation manually by replacing it with spaces
    punctuations = ".,!?;:()[]{}\"'_-*"
    cleaned_text = ""

    for char in lower_text:
        if char in punctuations:
            cleaned_text += " "
        else:
            cleaned_text += char

    # Split the text into a list of individual words
    words = cleaned_text.split()

    #Count the words manually using a loop
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    #Turn the dictionary into a list of pairs
    pair_list = list(frequency_dict.items())

    #Sort the list
    pair_list.sort(key=get_counter, reverse=True)

    #Convert the sorted list back into a dictionary
    sorted_dict = dict(pair_list)

    print(f"This is the sorted dict: {sorted_dict}")

    return sorted_dict


if __name__ == "__main__":
    word_frequency()