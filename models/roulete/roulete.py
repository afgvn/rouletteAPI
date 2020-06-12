from models.roulete import bet
from app import db 
import random
import datetime
import json
import copy

class Roulete : 

    def __init__(self, id ):
        self.id = id
        self.state = 0
        self.bets = []
        self.BetsTable = "bet"+ str(self.id)
        
    def open (self ) : 
        self.state = 1
        self.openTime = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
        var = {"Roulutte_State": self.state,  "Roulutte_id": self.id }

        return  var

    def close (self ) : 
        self.state = 0
        var = {  "Roulutte_id": self.id  ,"Bets_List" : self.ListAllBets() }

        return  var
    
    def closeAndplay (self ) : 
        self.state = 0
        self.closeTime = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
        bets_list=[]
        numberEndRouleta = random.randrange(bet.MinNumbreRolute ,bet.MaxNumbreRolute,1)
        for varBet in self.ListAllBets() :
            actualbet = bet.bet(varBet)
            actualbet.PlayBet(numberEndRouleta)
            bets_list.append(actualbet)
        var = { "Roulutte_id": self.id  ,"Bets_List" : bets_list ,"Numbre_play" : numberEndRouleta}
        
        return  var

    def ClearAllBets(self):
        for i in range(0, db.llen(self.BetsTable ) ):
             db.lpop(self.BetsTable  )

    def NewBet (self , betData ):
        varTime = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
        newData = copy.deepcopy(betData)
        newData ['id'] =  self.lengthBets()
        newData ['betTime'] = varTime
        newbet = bet.bet(newData)
        varReturn = {"Bet": newbet, "Message": newbet.StringMessageBet()}
        if newbet.state == 1:
            newbetJson = json.dumps( newbet.__dict__ )
            db.lpush(self.BetsTable , newbetJson)
        return  varReturn
    
    def lengthBets(self) :

        return db.llen(self.BetsTable )
    
    def ListAllBets (self ) : 
        betsList = []
        for i in range(0, db.llen(self.BetsTable )):
            tempJSON =  db.lindex(self.BetsTable , i )
            loadbet = json.loads ( tempJSON )
            if not 'betTime' in loadbet :
                loadbet['betTime']=  datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
            betsList.append(loadbet)#newbet
        self.bets=copy.deepcopy(betsList)

        return  betsList
    
    def StateToString (self ) : 
        StatesRolute = ["Close","Open","Play"]
        
        return  StatesRolute[self.state]
    




