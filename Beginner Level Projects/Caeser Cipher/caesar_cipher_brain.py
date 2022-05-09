alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    text_list = list(text)
    if direction[0] == 'd':
        shift *= -1
    for i in range(len(text)):
        if text_list[i] in alphabet:
            text_list[i] = alphabet[(alphabet.index(text[i]) + shift) % 26]
    new_text = ''.join(text_list)
    print(f"Your {direction}d text : {new_text}")
