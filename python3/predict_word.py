def find_next_word(text, word, start_pos):
    text = text[text.find(word, start_pos) + len(word) + 1: len(text)]
    text_next = text[: text.find(" ")]
    print(text_next)

    start_pos = text.find(" ") + 1
    return  text, start_pos

text = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning but still keep coding. "
text = text.lower()
word = "keep"
start_pos = 0


text, start_pos = find_next_word(text, word, start_pos)
text, start_pos = find_next_word(text, word, start_pos)
text, start_pos = find_next_word(text, word, start_pos)

