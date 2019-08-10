def format_string(string, formatter=None):
    """Format a string using the formatter obj - is expecting to have a format() method that accepts a string value"""
    
    class DefaultFormatter:
        """Format a string in the title case."""
        
        def format(self, string):
            return str(string).title()
            
    if not formatter:
        formatter = DefaultFormatter()
        
    return formatter.format(string)
    
hello_string = "hellow multiverse(s)! where are you?"
print(" input: " + hello_string)
print(" output:  " + format_string(hello_string))
