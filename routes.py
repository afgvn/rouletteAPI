from app import app, db
from flask import  jsonify
from datetime import datetime
from models.roulete  import clouster_roulete  as rouleteSection

@app.route('/addRoulete', methods=['GET', 'POST'])
def NewRoulute():
    newroulete = rouleteSection.ClousterRoulete.AddRoulete()
    SrtingState= newroulete.StateToString()

    return jsonify( Roulute_id = newroulete.id , Roulute_State = SrtingState)
@app.route('/deleteAllRouletes', methods=['GET', 'POST'])
def DeleteAllRoulute():
    rouleteSection.ClousterRoulete.DeleteAllDatas()

    return jsonify( message = 'Allempty')

@app.route('/deleteRouletes/<int:Roulute_id>', methods=['GET', 'POST'])
def DeleteRoulute(Roulute_id):
    rouleteSection.ClousterRoulete.DeleteRoulete ( Roulute_id )
    
    return jsonify( message = 'Delete Roulute')

@app.route('/open/<int:Roulute_id>', methods=['GET', 'POST'])
def openRoulute(Roulute_id):
    RouluteOpenid = Roulute_id
    actulaRoulute = rouleteSection.ClousterRoulete.RouletefindById(Roulute_id)
    if not actulaRoulute  : 
        Roulute_Message = "Error Roulute not exist .."
        Roulute_State = 4 
    else : 
        actulaRoulute.open()
        rouleteSection.ClousterRoulete.RouleteCommit(actulaRoulute)
        Roulute_State = actulaRoulute.state
        RouluteOpenid = actulaRoulute.id
        Roulute_Message = actulaRoulute.StateToString()

    return jsonify( Roulute_id = RouluteOpenid, Roulute_State = Roulute_State , Roulute_Message = Roulute_Message )

@app.route('/NewBetRoulute/<int:Roulute_id>/<int:Client_id>/<int:Type_bet>/<int:Bet>/<int:Qty_bet>', methods=['GET', 'POST'])
def betRoulute(Roulute_id , Client_id , Type_bet, Bet ,  Qty_bet ):
    RouluteOpenid = Roulute_id
    Bet_Id = 0
    actulaRoulute = rouleteSection.ClousterRoulete.RouletefindById(Roulute_id)
    if not actulaRoulute  : 
        Bet_Message = "Error Roulute not exist .."
        Bet_State = 4 
    elif  Roulute_id < rouleteSection.ClousterRoulete.RouleteLength() :
            Bet_Message = "Error Roulute its close --  bet  cancelled"
            Bet_State = 4
            if  actulaRoulute.state == 1:
                betData = { 'client' :  Client_id ,'type' : Type_bet , 'bet' : Bet , 'Qty' : Qty_bet  }
                newBetReturn = actulaRoulute.NewBet(  betData )  
                Bet_State = newBetReturn['Bet'].__dict__
                Bet_Message = newBetReturn['Message']
                Bet_Id = Bet_State['id']

    return jsonify( Roulute_id = RouluteOpenid , Bet_Id= Bet_Id , Bet = Bet_State  ,Bet_Message = Bet_Message )

@app.route('/CloseBetRoulute/<int:Roulute_id>', methods=['GET', 'POST'])
def CloseBetRoulute(Roulute_id  ):
    RouluteOpenid = Roulute_id
    listBets = []
    Numbre_play =  0
    actulaRoulute = rouleteSection.ClousterRoulete.RouletefindById(Roulute_id)
    if not actulaRoulute  : 
        temp_Message = "Error Roulute not exist .."
        temp_State = 4 
    elif  Roulute_id < rouleteSection.ClousterRoulete.RouleteLength() :
        temp_Message = "Error Roulute its close --  bet  cancelled"
        temp_State = 'error'
        closeRoulute = actulaRoulute.closeAndplay()
        rouleteSection.ClousterRoulete.RouleteCommit(actulaRoulute)
        RouluteOpenid = closeRoulute['Roulutte_id']
        Numbre_play =  closeRoulute['Numbre_play']
        for  VarBet in closeRoulute['Bets_List'] :
            listBets.append({'MessageBet': VarBet.StringMessageBet() , 'Bet': VarBet.__dict__ })
        actulaRoulute.ClearAllBets()

    return jsonify( Roulute_id = RouluteOpenid , Bets_List= listBets , ResultPlay =  Numbre_play   )

@app.route('/StateRoulutes', methods=['GET', 'POST'])
def StateRoulutes( ):
    Roulute_List = []
    for var in rouleteSection.ClousterRoulete.AllRouletes()  : 
        Roulute_List.append( {'Roulute_Id' : var['id']  , 'Roulute_Message' : var['message'] , 'Roulute_Data' : var['roulete'].__dict__ ,  }  )   

    return jsonify( Roulute_List = Roulute_List  )


