text = "Hello My name is mike. How are you ? ".lower()
word = "how"

text = text[text.find(word) + len(word) + 1:]
text_next = text[: text.find(" ")]

print(text_next)