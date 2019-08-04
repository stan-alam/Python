class SecretString:
    """None secure - string storage"""

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """show the string if the pass_phrase is correct."""
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""