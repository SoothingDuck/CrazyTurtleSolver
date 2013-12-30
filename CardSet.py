from Card import Card

class CardSet(list):

    def __contains__(self, obj):
        """Surchage in pour CardSet"""
        seq = list(self)

        for card in seq:
            if obj.equals(card):
                return True
            
        return False

    def init_crazy_turle_cardset_internet(self):
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

    def init_crazy_turle_cardset_home(self):
        """Init avec les cartes presentes sur le Crazy Turtle Solver d'internet"""
        self.append(Card("TRTBCVCJ"))
        self.append(Card("CJTVTRCB"))
        self.append(Card("CBTRTJCV"))
        self.append(Card("CJTRTBCR"))
        self.append(Card("CBTVTJCV"))
        self.append(Card("CBTVTJCR"))
        self.append(Card("TVTBCJCR"))
        self.append(Card("CBTRTVCJ"))
        self.append(Card("CBTVTJCR"))

    def copy(self):
        """Cree une copie du CardSet"""
        tmp = CardSet()

        for card in self:
            tmp.append(card.copy())

        return tmp

    def __str__(self):
        return "".join([str(x) for x in self])

    def delete_card(self, card):
        
        seq = list(self)

        for i, obj in enumerate(seq):
            if obj.equals(card):
                del self[i]
                return None

    def equals(self, other):
        """S'assure que 2 cardSet sont identique"""
        if len(self) != len(other):
            return False

        for card in self:
            if not card in other:
                return False

        return True
