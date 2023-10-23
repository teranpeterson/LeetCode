# SOLVED

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        size = 0
        word_count = 0
        start_index = 0
        for index, word in enumerate(words):
            if size + len(word) + word_count > maxWidth:
                spaces = (maxWidth - size)
                remaining = 0
                if word_count > 1:
                    remaining = spaces % (word_count - 1)
                    print(f'{remaining} = {spaces} % ({word_count} - {1})')
                    spaces //= (word_count - 1)
                    print(f'{spaces} //= ({word_count} - 1)')
                line = ""
                for i in range(start_index, index):
                    line += words[i] + " " * spaces
                    if remaining > 0:
                        line += " "
                        remaining -= 1
                res.append(line[:maxWidth])
                size = 0
                word_count = 0
                start_index = index
                print(f'|{res[-1]}|')

            size += len(word)
            word_count += 1
        
        line = ""
        for i in range(start_index, len(words)):
            line += words[i] + " "
        res.append(line.ljust(maxWidth, " ")[:maxWidth])
        print(f'|{res[-1]}|')
        print()

        return res

s = Solution()
s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
s.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16)

[
    'This    is    an',
    'example  of text',
    'justification.  ']
[
    "This    is    an",
    "example  of text",
    "justification.  "
]