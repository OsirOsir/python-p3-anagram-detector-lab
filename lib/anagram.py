class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, possible_anagrams):
        matches = []
        
        for candidate in possible_anagrams:
            if self.sorted_word == ''.join(sorted(candidate)):
                matches.append(candidate)
        
        return matches