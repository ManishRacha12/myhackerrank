#mansi@gmail.com
import re
m=re.match(r"(\w+)@(\w+)\.(\w+)","user@hacker.com")
print(m.groups())
m1=re.match(r"(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)","ham@gm.com")
print(m1.groupdict())

import re

pattern = r"your_pattern_here"
target_string = "your_target_string_here"

# Attempt to find a match
match = re.search(pattern, target_string)

if match:
    # Match was found, so access groups
    groups = match.groups()
    # Now you can work with the captured groups
else:
    print("no match")# No match was found, handle this case as needed
