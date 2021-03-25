# Search Engine

""""
It takes a list of sentences from the user as an input.
and asks user for a specific word as an input..
and this program shows the result according to the most relevant sentence...
"""


def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    mylist = []
    ask1 = int(input("How many sentence(s) do you wanna add to your list? "))
    for i in range(ask1):
        ask2 = str(input("Enter a sentence for your list: "))
        mylist.append(ask2)
    # print(matchingWords("This is samrat", "Samrat is sahsdasd"))
    sentences = mylist
    print()
    query = str(input("Enter the query string: "))
    print()
    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)
                       if sentScore[0] != 0]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found")
    print()
    for score, item in sortedSentScore:
        print(f"'{item}' : with a score of {score}")
    print()
