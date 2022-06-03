class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.move = [None, None]
        self.wins = [0, 0]
        self.ties = 0
        self.cash = self.ori_cash =  10000
        self.cashp1 = 0
        self.cashp2 = 0

    def get_cash(self):
        return self.cash

    def get_cashp1(self):
        return self.cashp1

    def get_cashp2(self):
        return self.cashp2

    def get_player_move(self, p):
        return self.move[p]

    def play(self, player, move):
        self.move[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def result(self):

        if self.move[0] == None or self.move[1] == None:
            return False

        p1 = self.move[0].upper()
        p2 = self.move[1].upper()

        if (p1 == "SPLIT" and p2 == "SPLIT"):
            self.cashp1 = self.cash // 2
            self.cashp2 = self.cash // 2

        if (p1 == "STEAL" and p2 == "STEAL"):
            self.cashp1 = 0
            self.cashp2 = 0

        if (p1 == "SPLIT" and p2 == "STEAL"):
            self.cashp1 = 0
            self.cashp2 = self.cash

        if (p1 == "STEAL" and p2 == "SPLIT"):
            self.cashp1 = self.cash
            self.cashp2 = 0
           
        return True


    def reset(self):
        self.p1Went = False
        self.p2Went = False
        self.move = [None, None]
        self.cash = self.ori_cash
        self.cashp1 = 0
        self.cashp2 = 0