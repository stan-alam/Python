#283C 
class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

        def __iter__(self):
            return self

        def __next__(self):
            l = self.insequence.readline()
            while l and "WARNING" not in l:
                l = self.insequence.readline()
            if not l:
    raise StopIteration
            return l.replace("\tWARNING", "")
