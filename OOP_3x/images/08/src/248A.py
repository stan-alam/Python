import sys
import re

pattern = sys.argv[1] #argument vector!
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    template = "'{}' matches patern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(search_string, pattern))
