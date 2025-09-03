class StringTools:
    def __init__(self, words):
        self.words = words

    @staticmethod
    def is_palindrome(text):
        text = text.lower().replace(" ", "") 
        return text == text[::-1]

    @classmethod
    def from_sentence(cls, sentence):
        words = sentence.split()
        return cls(words)



print(StringTools.is_palindrome("level"))  
print(StringTools.is_palindrome("Python"))  

st = StringTools.from_sentence("I love Python")
print(st.words) 
