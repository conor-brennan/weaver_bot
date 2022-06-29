AllWords = []
with open('4letterwords_official.txt') as file:
    lines = file.readlines()
for l in lines:
    AllWords.append(l[:4])

def lets_in_common(stringA, stringB):
    if len(stringA) != 4 or len(stringB) != 4:
        return 0
    score = 0
    lowerA = stringA.lower()
    lowerB = stringB.lower()
    for i in range(4):
        if lowerA[i] == lowerB[i]:
            score += 1
    return score

def next_words(currentWord):
    result = []
    for w in AllWords:
        if lets_in_common(currentWord, w) == 3:
            result.append(w)
    return result

