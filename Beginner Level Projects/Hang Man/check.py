def contain_blank(list):
    for item in list:
        if item == "_" :
            return True


def contain_letter(list, letter):
    for item in list:
        if item == letter:
            return True

