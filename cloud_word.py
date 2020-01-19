# HASHTABLES
# Average run time - space: O(n), insert:O(1), lookup:O(1), delete:O(1)
# STRENGTHS: Fast lookups, can be used for keys, as they are hashable
# HASHES: fingerprint. Possible concern: hash collision, when 2 files have the same hash value
# Solving hash collisions can be done by: instead of storing the actual values in an array, leet's have each array slot hold a pointer to a linked list
# holding the values for all the keys that hash to that index.
# WEAKNESSES: Slow lookups in the worst cases, keyas are NOT SORTED, looking up for a key for a given value is O(n), not cache-friendly(many hash table implementations use linked lists, which don't put data next to each other in memory)

# Think of a hash map as a "hack" on top of an array to let us use flexible keys instead of being stuck with sequential integer "indices."
# Sets are usually implemented very similarly to hash maps—using hashing to index into an array—but they don't have to worry about storing values alongside keys.


class CloudWord:
    def __init__(self, input_string):
        self.result = {}
        self.populate_result(input_string)

    def populate_result(self, input_string):
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dict()

        current_word_start_index = 0
        current_word_length = 0

        for i, character in enumerate(input_string):
            # if we reached the end of the string, check if it is letter and add as last word in dict;
            if i == len(input_string) - 1:
                if(character.isalpha()):
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[current_word_start_index:
                                                current_word_start_index+current_word_length]
                    self.add_word_to_dict(current_word)

            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif character == " " or character == '\u2014':
                if(current_word_length > 0):
                    current_word = input_string[current_word_start_index:
                                                current_word_start_index + current_word_length]
                    self.add_word_to_dict(current_word)
                    current_word_length = 0
            # we want to split on ellipses
            elif character == ".":
                if(i < len(input_string)-1 and input_string[i+1] == "."):
                    if(current_word_length > 0):
                        current_word = input_string[current_word_start_index:
                                                    current_word_start_index+current_word_length]
                        self.add_word_to_dict(current_word)
                        current_word_length = 0
            # If character is a letter or apostrophe, we add it to the current word
            elif character.isalpha() or character == '\'':
                if(current_word_length == 0):
                    current_word_start_index = i
                current_word_length += 1

            # If the character is a hyphen, check it is surrounded by letters: add to the word
            elif character == "-":
                if i > 0 and input_string[i-1].isalpha() and input_string[i+1].isalpha():
                    if(current_word_length == 0):
                        current_word_start_index = i
                    current_word_length += 1
                else:
                    if(current_word_length > 0):
                        current_word = input_string[current_word_start_index:
                                                    current_word_start_index+current_word_length]
                        self.add_word_to_dict(current_word)
                        current_word_length = 0

    def add_word_to_dict(self, word):
        if(word in self.result):
            self.result[word] += 1
        elif(word.lower() in self.result):
            self.result[word.lower()] += 1
        elif(word.capitalize() in self.result):
            self.result[word] = 1
            self.result[word] += self.result[word.capitalize()]
            del self.result[word.capitalize()]
        else:
            self.result[word] = 1


cloudword1 = CloudWord('Friends, Romans, countrymen! Let us eat cake.')
print(cloudword1.result)

cloudword2 = CloudWord('We came, we saw, we ate cake.')
print(cloudword2.result)
cloudword3 = CloudWord(
    'Bill finished his cake at the edge of the cliff and then paid his bill.')
print(cloudword3.result)
cloudword4 = CloudWord(
    'New tourists in New York often wait in long lines for cronuts, new.')
print(cloudword4.result)
