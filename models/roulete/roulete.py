from models.roulete import bet
from app import db 
import random
import time
import json

class Roulete : 

    def __init__(self, id ):
        self.id = id
        self.state = 0
        self.bets = []
        self.NameTable = "bet"+ str(self.id)



    def open (self ) : 
        self.state = 1
        var = {"Roulutte_State": self.state,  "Roulutte_id": self.id }

        return  var

    def close (self ) : 
        self.state = 0
        var = {  "Roulutte_id": self.id  ,"Bets_List" : self.ListAllBets() }

        return  var
    
    def closeAndplay (self ) : 
        self.state = 0
        bets_list=[]
        numberEndRouleta = random.randrange(bet.MinNumbreRolute ,bet.MaxNumbreRolute,1)
        print( 'roulete number play in  : ' + str( numberEndRouleta ) )
        for varBet in self.ListAllBets() :
            varBet.PlayBet(numberEndRouleta)
            bets_list.append(varBet)
        var = { "Roulutte_id": self.id  ,"Bets_List" : bets_list ,"Numbre_play" : numberEndRouleta}
        
        return  var

    def ClearAllBets(self):
        for i in range(0, db.llen(self.NameTable ) ):
             db.lpop(self.NameTable  )

    
    def NewBet (self , client , type , valuebet , Qty ) : 
        newbet = bet.bet(self.lengthBets(), client , type , valuebet , Qty)
        varReturn = {"Bet": newbet.bet,  "Bet_Id": newbet.id,"Bet_State":newbet.state ,   "Bet_Message": newbet.StringMessageBet(),   "Roulutte_id": self.id}
        newbetJson = json.dumps( newbet.__dict__ )
        db.lpush(self.NameTable , newbetJson)
        return  varReturn
    
    def lengthBets(self) :

        return db.llen(self.NameTable )
    
    def ListAllBets (self ) : 
        betsList = []
        for i in range(0, db.llen(self.NameTable )):
            tempJSON =  db.lindex(self.NameTable , i )
            loadbet = json.loads ( tempJSON )
            newbet = bet.bet(loadbet['id'], loadbet['client'] , loadbet['type'] , loadbet['bet'] , loadbet['Qty'])
            betsList.append(newbet)

        return  betsList
    
    def StateToString (self ) : 
        StrinTemp = ["Close","Open","Play"]
        
        return  StrinTemp[self.state]
    




