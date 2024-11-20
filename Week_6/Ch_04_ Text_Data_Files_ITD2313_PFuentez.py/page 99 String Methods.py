s = "hi there!"
# Output: s = 'hi there!'

len(s)
# Output: 9

s.center(11)
# Output: ' hi there! '

s.count('e')
# Output: 2

s.endswith("there!")
# Output: True

s.startswith("hi")
# Output: True

s.find("the")
# Output: 3

s.isalpha()
# Output: False

'abc'.isalpha()
# Output: True

"326".isdigit()
# Output: True

words = s.split()
words
# Output: ['hi', 'there!']

' '.join(words)
# Output: 'hi there!'

' '.join(words)
# Output: 'hi there!'

s.lower()
# Output: 'hi there!'

s.upper()
# Output: 'HI THERE!'

s.replace('i', 'o')
# Output: 'ho there!'

"hi there!".strip()
# Output: 'hi there!'
