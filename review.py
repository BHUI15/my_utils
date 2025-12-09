# class module

class Review:
    """
    A class to represent review with sentiment label
    """
    def __init__(self, text, label):
        # set up the constructor
        """
        Initialize the review with text and label.
        
        :param self: Description
        :param text (str): The review text.
        :param label (str): The sentiment label ("positive" or "negative").
        """
        self.text = text
        self.label = label

    def is_positive(self):
        return self.label.lower() == "positive"

    def word_count(self):
        words = self.text.split()
        return len(words)