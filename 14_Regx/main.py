# MATCH ANY CHARACTER:
#   .     Any character except newline
#   QUANTIFIERS (how many times):
#   *     0 or more   (greedy: takes as many as possible)
#   +     1 or more
#   ?     0 or 1  (makes preceding optional)
#   {n}   Exactly n times
#   {n,}  n or more times
#   {n,m} Between n and m times
#   *?    Non-greedy (lazy): as few as possible
#   ANCHORS (position, not characters):
#   ^     Start of string  (or start of line with re.MULTILINE)
#   $     End of string    (or end of line with re.MULTILINE)

#   \b    Word boundary    (between \w and \W)
#   CHARACTER CLASSES:
#   [abc]  Any one of: a, b, or c
#   [^abc] NOT a, b, or c
#   [a-z]  Any lowercase letter
#   [0-9]  Any digit
#   SPECIAL CLASSES:
#   \d   Digit         [0-9]
#   \D   Non-digit     [^0-9]
#   \w   Word char     [a-zA-Z0-9_]
#   \W   Non-word char [^a-zA-Z0-9_]
#   \s   Whitespace    [ \t\n\r\f\v]
#   \S   Non-whitespace
#   ALTERNATION AND GROUPING:
#   a|b      a OR b
#   (abc)    Group — captures match, remembered as group 1
#   (?:abc)  Non-capturing group — groups without remembering
#   (?P<name>abc)  Named group — access with m.group('name')