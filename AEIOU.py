def findVowels(str):
    if ('a' and 'e' and 'i' and 'o' and 'u') in str:
        return True
    else:
        return False


def shower(s):
    print(s, '=>', eval(s))


print(findVowels("you ever climb the aggro-crag"))
print(findVowels("water, ships, and boats turn"))
