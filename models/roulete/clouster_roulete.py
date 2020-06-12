from models.roulete import roulete
from app import db 
import json
class ClousterRoulete : 
 
    def RouletefindById ( FindId ) :
        newRouleta = None
        for i in range(0, db.llen('Rouletes')):
            tempJSON =  db.lindex('Rouletes', i )
            loadroulet = json.loads ( tempJSON )
            if loadroulet['id'] == FindId :
                newRouleta = roulete.Roulete(  loadroulet['id'] )
                newRouleta.state = loadroulet['state'] 

        return  newRouleta

    def RouleteCommit( newRouleta ) :
        for i in range(0, db.llen('Rouletes')):
            tempJSON =  db.lindex('Rouletes', i )
            loadroulet = json.loads ( tempJSON )
            if loadroulet['id'] == newRouleta.id :
                newrouleteJson = json.dumps( newRouleta.__dict__ )
                db.lset('Rouletes', i  , newrouleteJson)

        return  newRouleta

    def AllRouletes () :
        Rouletes = []
        for i in range(0, db.llen('Rouletes')):
            tempJSON =  db.lindex('Rouletes', i )
            loadroulet = json.loads ( tempJSON )
            newroulute = roulete.Roulete(  loadroulet['id'] )
            newroulute.BetsTable = loadroulet['BetsTable'] 
            newroulute.state = loadroulet['state'] 
            newroulute.ListAllBets()
            RouleteData={ 'id':  loadroulet['id']  , 'roulete' : newroulute  , 'message' : newroulute.StateToString() }
            Rouletes.append(RouleteData)
    
        return  Rouletes

    def RouleteLength () :

        return  db.llen('Rouletes')
    
    def AddRoulete () :
        newindex   = ClousterRoulete.FindIdxFree()
        newroulete = roulete.Roulete( newindex )
        newrouleteJson = json.dumps( newroulete.__dict__ )
        db.lpush('Rouletes', newrouleteJson)
        
        return newroulete

    def DeleteRoulete ( id ) :
        for i in range(0, db.llen('Rouletes')):
            tempJSON =  db.lindex('Rouletes', i )
            loadroulet = json.loads ( tempJSON )
            if loadroulet['id'] == id : 
                db.lrem('Rouletes' , 0 , tempJSON)
                break
       
    def DeleteAllRoulete () :
        for i in range(0, db.llen('Rouletes') ):
                db.lpop('Rouletes' )
        
    def DeleteAllDatas () :
        db.flushdb()
    
    def FindIdxFree () :
        newindex= db.llen('Rouletes')
        for j in range(0, db.llen('Rouletes') ):
            conuntEqual = 0
            for i in range(0, db.llen('Rouletes')):
                tempJSON =  db.lindex('Rouletes', i )
                loadroulet = json.loads ( tempJSON )
                if  loadroulet['id'] == j : 
                    conuntEqual = conuntEqual +1 
                    break
            if  conuntEqual == 0 and not newindex == j :
                newindex= j 
                break 

        return newindex           


   