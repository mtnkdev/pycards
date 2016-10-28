import ttk

from pysollib import dataloader
from pysollib import gamelayout
from pysollib.gamelayout import k
from pysollib.dealer import Dealer


def findClosest(x,y):

    for i in range(len(k.stacks)):
        stack = k.stacks[i]
        if abs(stack.x - x) < 20 and abs(stack.y + stack.offset*len(stack.cards) - y) < 20:
            return i
    return -1

def drawGame(root):
    cardset = dataloader.Cardset.cardsets["Standard"]
    dealer = Dealer(k, cardset)
    dealer.cardgen()
    dealer.dealCards()

    def dragCard(event):
        if not validSelection(event):
            return
        ID = event.widget.stackID
        if event.widget.cardNum == len(k.stacks[ID].cards) - 1:
            x = event.widget.winfo_x() + event.x - event.widget.winfo_width()/2
            y = event.widget.winfo_y() + event.y - event.widget.winfo_height()/2
            event.widget.place(x=x, y=y)
        else:
            cardID = event.widget.cardNum
            for cardImg in k.stacks[ID].cardWidgets[cardID:]:
                x = cardImg.winfo_x() + event.x - cardImg.winfo_width() / 2
                y = cardImg.winfo_y() + event.y - cardImg.winfo_height() / 2
                cardImg.place(x=x, y=y)

    def tryDrop(event):
        ID = event.widget.stackID
        x = event.widget.winfo_x() + event.x - event.widget.winfo_width() / 2
        y = event.widget.winfo_y() + event.y - event.widget.winfo_height() / 2
        destID = findClosest(x,y)

        if destID == -1:
            event.widget.place(x=k.stacks[ID].x, y=k.stacks[ID].y + (event.widget.cardNum) * k.stacks[ID].offset)
            return
        #print "destID=", destID

        select = validSelection(event)
        #print "select", select
        drop = validDrop(event, destID)
        #print "drop", drop
        if select and drop:
            #print "Valid"
            destID = ID
            event.widget.place(x=k.stacks[destID].x, y=k.stacks[destID].y + (event.widget.cardNum) * k.stacks[destID].offset)
        else:
            event.widget.place(x=k.stacks[ID].x,y=k.stacks[ID].y + (event.widget.cardNum)*k.stacks[ID].offset)

    def validSelection(event):
        stackID = event.widget.stackID
        cardNum = event.widget.cardNum
        stack = k.stacks[stackID]

        if cardNum == len(stack.cards) - 1:
            return True

        prev = stack.cards[cardNum]
        for i in range(cardNum + 1, len(stack.cards)):
            if stack.cards[i].rank >= prev.rank \
                    or stack.cards[i].color == prev.color:
                return False

    def validDrop(event, destID):
        color = event.widget.color
        rank = event.widget.rank
        stack = k.stacks[destID]

        #print "moverank", rank
        #print "movecolor", color
        #print "destrank", stack.cards[-1].rank
        #print "destcolor", stack.cards[-1].color

        if stack.cards[-1].rank <= rank \
                or stack.cards[-1].color == color:
            return False
        return True


    # for stack in k.piles:
    stackNum = 0
    for stack in k.stacks:
        for num in range(len(stack.cards)):
            label = ttk.Label(root.canvas, image=stack.cards[num].setImage(), borderwidth=0)
            setattr(label, "rank", stack.cards[num].rank)
            setattr(label, "suit", stack.cards[num].suit)
            setattr(label, "color", stack.cards[num].color)
            setattr(label, "stackID", stackNum)
            setattr(label, "cardNum", num)

            stack.cardWidgets[num] = label
            label.place(x=stack.x, y=stack.y + stack.offset*num)
            label.bind("<ButtonRelease-1>", tryDrop)
            label.bind("<B1-Motion>", dragCard)
        stackNum += 1