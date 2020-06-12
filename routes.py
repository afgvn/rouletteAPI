from app import app, db
from flask import  jsonify
from datetime import datetime
from models.roulete  import clouster_roulete  as rouleteSection

@app.route('/addRoulete', methods=['GET', 'POST'])
def NewRoulute():
    newroulete = rouleteSection.ClousterRoulete.AddRoulete()
    SrtingState= newroulete.StateToString()

    return jsonify( Roulute_id = newroulete.id , Roulute_State = SrtingState)
@app.route('/deleteRouletes', methods=['GET', 'POST'])
def DeleteRoulute():
    rouleteSection.ClousterRoulete.DeleteRoulete(1)
    return jsonify( message = 'empty')

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
                newBetReturn = actulaRoulute.NewBet(  Client_id , Type_bet , Bet , Qty_bet )   #client , type , bet , Qty 
                Bet_State = newBetReturn['Bet_State']
                Bet_Id = newBetReturn['Bet_Id']
                Bet_Message = newBetReturn['Bet_Message']

    return jsonify( Roulute_id = RouluteOpenid , Bet_Id= Bet_Id , Bet_State = Bet_State  ,Bet_Message = Bet_Message )

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
            listBets.append({'MessageBet': VarBet.StringMessageBet() , 'StateBet': VarBet.state  })
        actulaRoulute.ClearAllBets()

    return jsonify( Roulute_id = RouluteOpenid , Bets_List= listBets , ResultPlay =  Numbre_play   )

@app.route('/StateRoulutes', methods=['GET', 'POST'])
def StateRoulutes( ):
    Roulute_List = []
    for var in rouleteSection.ClousterRoulete.AllRouletes()  : 
        Roulute_List.append( {'Roulute_Id' : var['id'] , 'Roulute_State' : var ['state'] , 'Roulute_Message' : "tes 34 " }  )   

    return jsonify( Roulute_List = Roulute_List  )


