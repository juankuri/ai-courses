#1
a = ""
length = 0
q0.a.check()

#2
b = "it's ok"
length = 7
q0.b.check()

#3
c = 'it\'s ok'
length = 7
q0.c.check()

#4
d = """hey"""
length = 3
q0.d.check()

#5
e = '\n'
length = 1
q0.e.check()

#6
    def is_valid_zip(zip_code):
        """Returns whether the input string is a valid (5 digit) zip code
        """
        if (zip_code.isdigit()) and (len(zip_code) == 5):
            return True
        return False
    
    # Check your answer
    q1.check()

#7
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    l = []
    keyword = keyword.lower()

    for i in range(len(doc_list)):
        doc = doc_list[i].lower()
        words=doc.split()
        for word in words:
            word = word.strip(",.")
            if keyword == word:
                l.append(i)
                break
    return l
# Check your answer
q2.check()