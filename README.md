# Interpreter
This is an interpreter for a language similar to Scheme.
The language is based on the following grammar:

IDENTIFIER = (a‐z|A‐Z)(a‐z|A‐Z|0‐9)*
BOOLEAN = #t | #f
INTEGER = (0‐9)+
REAL = (0‐9)+\.(0‐9)* | (0‐9)*\.(0‐9)+
PUNCTUATION = \( | \) | { | } | , | \+ | ‐ | \* | / | %
  | := | != | < | > | <= | >= | ;
KEYWORD = var | fun | if | else | return
  | read | write | not | or | and
