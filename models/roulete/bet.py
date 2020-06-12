import datetime

MaxNumbreRolute=36
MinNumbreRolute=0
MaxQtyBet=10000
MaxNumberColors=2
class bet : 

    def __init__(self, betData ):
        self.id = betData['id']
        self.type = betData['type']
        self.bet = betData['bet']
        self.client = betData['client']
        self.Qty = betData['Qty']
        self.Qty_win = 0
        self.state = 0
        self.betTime = betData['betTime']  
        if self.ValidBet() ==  0 :
            self.CreateBet()
        else :
            self.state = 4

        return

    def CreateBet(self):
        self.state = 1

        return
            
    def PlayBet (self , NumberPlayRolute):
        self.Qty_win = 0
        self.state = 3
        if self.type == 0 :
            self.ColorBet( NumberPlayRolute )
        elif  self.type == 1 :
            self.NumberBet( NumberPlayRolute )

        return

    def ColorBet (self , NumberPlayRolute) :
        self.state = 3
        if NumberPlayRolute % 2 and self.bet == 0:
            self.state = 2
            self.Qty_win = self.Qty * 2
        elif not NumberPlayRolute % 2 and self.bet == 1:
            self.state = 2
            self.Qty_win = self.Qty * 2
         
        return 

    def NumberBet (self , NumberPlayRolute) :
        self.state = 3
        if NumberPlayRolute == self.bet :
            self.state = 2
            self.Qty_win = self.Qty * 36
         
        return 

    def ValidBet (self):
        ValidState=0 
        if  self.type > 1 :
            ValidState = 1
        elif self.type == 0  and not 0 <= self.bet < MaxNumberColors :  # color bet
            ValidState = 2
        elif self.type == 1  and not  MinNumbreRolute <= self.bet <= MaxNumbreRolute   : # number bet
            ValidState = 3
        elif self.Qty > MaxQtyBet :
            ValidState = 4
       
        return ValidState

    def StrinValidations(self):
        StrinValidationsbet = ["Valid","Not Valid Type","Not Valid Color 0-Red 1-Black","Not Valid Number range 0-36","Not Valid qty max value $10.000"]

        return StrinValidationsbet[ ( self.ValidBet()  ) ]

    def StrinStates(self):
        StrinStatesbet = ["Validaing" ,"Aceppted", "Win" , "Lose" , "Error"  ]
        return StrinStatesbet[ self.state  ]

    def StringBet(self):
        varTemp=""
        StrinColor = ["Red","Black"]
        if self.type == 0 :
            varTemp= StrinColor[self.bet]
        elif  self.type == 1 :
            varTemp=  str(self.bet)

        return varTemp

    def StringTime(self) :

        return self.betTime

    def StringTypeBet(self):
        StrinTypeBet = ["Color","Number"]

        return StrinTypeBet[self.type]

    def StringMessageBet(self):
        tempMessageString = self.StrinStates()
        if self.state == 0 or self.state == 1 :
            tempMessageString = tempMessageString + '  TypeBet : '+ self.StringTypeBet()
            tempMessageString = tempMessageString  +  ' Time : ' +  self.StringTime()
            tempMessageString = tempMessageString  +  ' Bet : ' +  self.StringBet()
            tempMessageString = tempMessageString  +  ' Value Bet : $' +  str (self.Qty) 
        elif self.state == 2:
            tempMessageString = 'Your Win !!!!!!'
            tempMessageString = tempMessageString + '  TypeBet : '+ self.StringTypeBet()
            tempMessageString = tempMessageString  +  ' Time : ' +  self.StringTime()
            tempMessageString = tempMessageString  +  ' Bet : ' +  self.StringBet()
            tempMessageString = tempMessageString  +  ' Value Bet : $' +  str (self.Qty)
            tempMessageString = tempMessageString  +  ' Value WIN : $' +  str (self.Qty_win)
        elif self.state == 3:
            tempMessageString = 'Your Loss !!!!!!'
            tempMessageString = tempMessageString + '  TypeBet : '+ self.StringTypeBet()
            tempMessageString = tempMessageString  +  ' Time : ' +  self.StringTime()
            tempMessageString = tempMessageString  +  ' Bet # ' +  str (self.bet)
            tempMessageString = tempMessageString  +  ' Value Bet : $' +  str (self.Qty)
        elif self.state == 4 : 
             tempMessageString = tempMessageString + " " +  self.StrinValidations()
        else : 
            tempMessageString = tempMessageString + "bet it "
            
        return tempMessageString