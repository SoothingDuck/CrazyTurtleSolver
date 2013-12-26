from Card import Card

class CardSet(list):

    def __contains__(self, obj):
        """Surchage in pour CardSet"""
        seq = list(self)

        tmp = obj
        for _ in range(4):
            tmp = tmp.rotate_right()
            if tmp in seq:
                return True
            
        return False

    def init_crazy_turle_cardset(self):
        """Init avec les cartes presentes sur le Crazy Turtle Solver d'internet"""
        self.append(Card("TJTBTVCR"))
        self.append(Card("TBTRCBCV"))
        self.append(Card("TVTRCJCR"))
        self.append(Card("TBCVCJCV"))
        self.append(Card("TRTVCBCJ"))
        self.append(Card("CVTJTRTR"))
        self.append(Card("TJCBTJCR"))
        self.append(Card("TJCJCRTB"))
        self.append(Card("CVCBTVCB"))

    def copy(self):
        
        p = CardSet()
        for x in self:
            p.append(x)

        return p

    def __str__(self):
        return "".join([str(x) for x in self])

    def delete_card(self, card):
        
        seq = list(self)

        tmp = card
        for _ in range(4):
            tmp = tmp.rotate_right()
            for i, t in enumerate(seq):
                if t == tmp:
                    del self[i]
                    return None
            
