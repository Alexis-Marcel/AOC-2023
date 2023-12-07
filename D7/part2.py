def parser():
    with open('input2.txt') as f:
        lines = f.readlines()
    return lines

def parseHands(lines):
    
    hands = []
    
    for line in lines:      
        hands.append(line.split())
    return hands

handRank = { 'highCard': 0, 'pair': 1, 'twoPair': 2, 'threeOfAKind': 3, 'straight': 4, 'fullHouse': 5, 'fourOfAKind': 6, 'fiveOfAKind': 7, }
cardRank = { 'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12 }
def getHandRank(hand):
    cards = countCards(hand[0])
    
    if len(cards) == 5:
        rank = handRank['highCard']
    elif len(cards) == 4:
        rank = handRank['pair']
    elif len(cards) == 3:
        if isThreeOfAKind(cards):
            rank = handRank['threeOfAKind']
        else:
            rank = handRank['twoPair']
    elif len(cards) == 2:
        if isFourOfAKind(cards):
            rank = handRank['fourOfAKind']
        else:
            rank = handRank['fullHouse']
    elif len(cards) == 1:
        rank = handRank['fiveOfAKind']
    return rank

def isThreeOfAKind(cards):
    for card in cards:
        if cards[card] == 3:
            return True
    return False

def isFourOfAKind(cards):
    for card in cards:
        if cards[card] == 4:
            return True
    return False


def countCards(hand):
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    if 'J' in cards:
        countJ = cards['J']
        cards.pop('J')
        if cards == {}:
            return { 'J': countJ }
        
        maxCardCount = list(cards.keys())[0]
        for card in cards:
            if cards[card] > cards[maxCardCount]:
                maxCardCount = card
            elif cards[card] == cards[maxCardCount]:
                if cardRank[card] > cardRank[maxCardCount]:
                    maxCardCount = card
        
        cards[maxCardCount] += countJ
    return cards
        
    
def insertHand(hand, listHands):
    rank = getHandRank(hand)
    (cards, bid) = hand
    for i in range(len(listHands)):
        otherRank = listHands[i][1]
        if rank > otherRank:
            listHands.insert(i, (hand, rank))
            return listHands
        if rank == otherRank:
            otherCards = listHands[i][0][0]
            j = 0
            while j < len(cards):
                rankCard = cardRank[cards[j]]
                otherRankCard = cardRank[otherCards[j]]
                if rankCard > otherRankCard:
                    listHands.insert(i, (hand, rank))
                    return listHands
                elif rankCard < otherRankCard:
                    break
                j += 1
    listHands.append((hand, rank))
    return listHands
    
 
def main():
    lines = parser()
    
    hands = parseHands(lines)
        
    listHands = []
    
    for hand in hands:
        listHands = insertHand(hand, listHands)
    
    
    sum = 0
    
    for i in range(len(listHands)):
        sum += (len(listHands) - i) * int(listHands[i][0][1])
        
    print(sum)
                                    
main()

