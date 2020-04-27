acronym = ''
phrase = []
numberOfWords = 0
dp = {}

def countPossibilities(acronymIndex, phraseIndex, wordCount):
    if acronymIndex >= len(acronym):
        if wordCount == numberOfWords:
            # print ('finished - {}, {}, {}'.format(acronymIndex, phraseIndex, wordCount))
            return 1
        else:
            return 0

    if wordCount >= numberOfWords:
        return 0

    if phraseIndex >= len(phrase[wordCount]):
        return 0

    if (acronymIndex, phraseIndex, wordCount) in dp:
        return dp[(acronymIndex, phraseIndex, wordCount)]

    tAns = 0

    if acronym[acronymIndex] == phrase[wordCount][phraseIndex]:
        # print('equal - {}, {}, {}'.format(acronymIndex, phraseIndex, wordCount))
        tAns = countPossibilities(acronymIndex + 1, phraseIndex + 1, wordCount) + countPossibilities(acronymIndex, phraseIndex + 1, wordCount) + countPossibilities(acronymIndex + 1, 0, wordCount + 1)
    else:
        tAns = countPossibilities(acronymIndex, phraseIndex + 1, wordCount)

    dp[(acronymIndex, phraseIndex, wordCount)] = tAns
    return tAns

n = int(input())

while n != 0:

    insigWords = []

    for _ in range(n):
        insigWord = input()
        insigWords.append(insigWord)

    testCase = input()

    while testCase != "LAST CASE":
        lst = testCase.split()
        acronym = lst[0].lower()
        phrase = list(filter(lambda x: x not in insigWords, lst[1:]))
        numberOfWords = len(phrase)

        dp = {}

        ans = countPossibilities(0, 0, 0)

        if ans == 0:
            print('{} is not a valid abbreviation'.format(acronym.upper()))
        else:
            print('{} can be formed in {} ways'.format(acronym.upper(), ans))

        testCase = input()

    n = int(input())
