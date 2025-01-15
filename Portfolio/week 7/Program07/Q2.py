"""Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both"""

def letters_in_at_least_one(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower())) # | is union operator

def letters_in_both_words(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower())) # & is intersection operator

def letters_in_either_word_but_not_in_both(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower())) # ^is symmetric difference operator

word1 = "laptop"
word2 = "touchpad"

union = letters_in_at_least_one(word1, word2)
print("Letters in at least one of the two words: ",union)

intersection = letters_in_both_words(word1, word2)
print("Letters in both words: ", intersection)

symmetric_difference = letters_in_either_word_but_not_in_both(word1, word2)
print("Letters_in_either_word_but_not_in_both: ", symmetric_difference )