text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido 
van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using 
significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 
2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years. Python features a 
dynamic type system and automatic memory management. It supports multiple programming paradigms, including 
object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library. Python 
interpreters are available for many operating systems. CPython, the reference implementation of Python, 
is open source software and has a community-based development model, as do nearly all of Python's other 
implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!"""

lower_case_alphabetic_sequence = ''.join(filter(str.isalpha, text)).lower()

letters_count = {}
for letter in lower_case_alphabetic_sequence:
    letters_count[letter] = letters_count[letter] + 1 if letter in letters_count else 1

most_common_letter = max(letters_count, key=letters_count.get)
print(f"The most common letter in the text is '{most_common_letter}' which occurs {letters_count[most_common_letter]} "
      f"times. The word 'Python' occurs in the text {lower_case_alphabetic_sequence.count('python')} times.")
