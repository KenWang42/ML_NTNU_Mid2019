def pirateTalk(msg):
    res = ""
    for index in range(len(msg)):
        if index == len(msg)-1:
            next = 'end'
        else:
            next = msg[index+1]

        if msg[index] == 'r':
            if next == ' ' or next == 'end':
                res = res + 'rrrgh'
            else:
                res = res + 'rrr'

        elif msg[index] == 'e'and next != ('a' or 'e' or 'i' or 'o' or 'u'):
            res = res + 'ee'
        else:
            res = res + msg[index]
    return res


print(pirateTalk("me mates yearn for the sea"))
print(pirateTalk("proud land lubber"))
print(pirateTalk("ship ahoy"))
