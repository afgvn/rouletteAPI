from models import bet 

Rouletes = []


class Roulete : 

    def __init__(self, id ):
        self.id = id
        self.state = 0
        self.bets = []



    def open (self ) : 
        self.state = 1
        var = {"Roulutte_State": self.state,  "Roulutte_id": self.id }

        return  var

    def close (self ) : 
        self.state = 0
        var = {  "Roulutte_id": self.id  ,"Bets_List" : self.bets}

        return  var
    
    def NewBet (self , client , type , valuebet , Qty ) : 
        newbet = bet.bet(len(self.bets), client , type , valuebet , Qty)
        self.bets.append(newbet)
        varReturn = {"Bet": newbet.bet,  "Bet_Id": newbet.id,   "Bet_State": newbet.StringMessageBet(),   "Roulutte_id": self.id}
       
        return  varReturn
    
    def ListAllBets (self ) : 

        return  self.bets
    
    def StateToString (self ) : 
        StrinTemp = ["Close","Open","Play"]
        
        return  StrinTemp[self.state]
    
