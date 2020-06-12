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
                print(loadroulet)
                newRouleta = roulete.Roulete(  loadroulet['id'] )
                newRouleta.state = loadroulet['state'] 

        return  newRouleta

    def RouleteCommit( newRouleta ) :
        #DeleteRoulete(newRouleta.id)
        #db.lrem('Rouletes',1 , )
    
        for i in range(0, db.llen('Rouletes')):
            tempJSON =  db.lindex('Rouletes', i )
            loadroulet = json.loads ( tempJSON )
            print(loadroulet)
            if loadroulet['id'] == newRouleta.id :
                newrouleteJson = json.dumps( newRouleta.__dict__ )
                db.lset('Rouletes', i  , newrouleteJson)

        return  newRouleta


    def AllRouletes () :
        Rouletes = []
        for i in range(0, db.llen('Rouletes')):
            tempJSON =  db.lindex('Rouletes', i )
            loadroulet = json.loads ( tempJSON )
            newroulute = roulete.Roulete(  db.llen('Rouletes') )
            RouleteData={ 'id':  loadroulet['id']  , 'state' : loadroulet['state']  , 'message' : "message"  }
            Rouletes.append(loadroulet)
    
        return  Rouletes

    def RouleteLength () :

        return  db.llen('Rouletes')

    def AddRoulete () :
        newroulete = roulete.Roulete( db.llen('Rouletes') )
        newrouleteJson = json.dumps( newroulete.__dict__ )
        db.lpush('Rouletes', newrouleteJson)
        return newroulete

    def DeleteRoulete ( id ) :
        db.flushdb()

    def DeleteAllRoulete () :
        for i in range(0, db.llen('Rouletes') ):
                db.lpop('Rouletes' )


   