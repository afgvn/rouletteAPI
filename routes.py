from app import app, db
from flask import  jsonify
from datetime import datetime
from models  import roulete  as rouleteSection



@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def NewRoulute():
    newroulete = rouleteSection.Roulete( len( rouleteSection.Rouletes ) )
    SrtingState= newroulete.StateToString()
    rouleteSection.Rouletes.append(newroulete)

    return jsonify( Roulute_id = newroulete.id , Roulute_State = SrtingState)

@app.route('/open/<int:Roulute_id>', methods=['GET', 'POST'])
def openRoulute(Roulute_id):
    RouluteOpenid = Roulute_id
    Roulute_State = "Error Roulute not exist .."
    if  Roulute_id < len( rouleteSection.Rouletes ):
        rouleteSection.Rouletes[Roulute_id].open()
        RouluteOpenid = Roulute_id
        Roulute_State = rouleteSection.Rouletes[Roulute_id].StateToString()

    return jsonify( Roulute_id = RouluteOpenid, Roulute_State = Roulute_State )

@app.route('/NewBetRoulute/<int:Roulute_id>/<int:Client_id>/<int:Type_bet>/<int:Bet>/<int:Qty_bet>', methods=['GET', 'POST'])
def betRoulute(Roulute_id , Client_id , Type_bet, Bet ,  Qty_bet ):
    RouluteOpenid = Roulute_id
    Bet_Id = Bet
    Bet_Message = "Error Roulute not exist -- bet   cancelled"
    Bet_State = 4
    if  Roulute_id < len( rouleteSection.Rouletes ):
            Bet_Message = "Error Roulute its close --  bet  cancelled"
            Bet_State = 4
            if  rouleteSection.Rouletes[Roulute_id].state == 1:
                newBetReturn = rouleteSection.Rouletes[Roulute_id].NewBet(  Client_id , Type_bet , Bet , Qty_bet )   #client , type , bet , Qty 
                Bet_State = newBetReturn['Bet_State']
                Bet_Id = newBetReturn['Bet_Id']
                Bet_Message = newBetReturn['Bet_Message']

    return jsonify( Roulute_id = RouluteOpenid , Bet_Id= Bet_Id , Bet_State = Bet_State  ,Bet_Message = Bet_Message )

@app.route('/CloseBetRoulute/<int:Roulute_id>', methods=['GET', 'POST'])
def CloseBetRoulute(Roulute_id  ):
    RouluteOpenid = Roulute_id
    listBets = []
    Numbre_play =  0
    temp_Message = "Error Roulute not exist -- bet   cancelled"
    temp_State = 'error'
    if  Roulute_id < len( rouleteSection.Rouletes ):
        temp_Message = "Error Roulute its close --  bet  cancelled"
        temp_State = 'error'
        closeRoulute = rouleteSection.Rouletes[Roulute_id].closeAndplay()
        print(closeRoulute)
        print(closeRoulute['Bets_List'])
        RouluteOpenid = closeRoulute['Roulutte_id']
        Numbre_play =  closeRoulute['Numbre_play']
        for  VarBet in closeRoulute['Bets_List'] :
            listBets.append({'MessageBet': VarBet.StringMessageBet() , 'StateBet': VarBet.state  })
            
    return jsonify( Roulute_id = RouluteOpenid , Bets_List= listBets , ResultPlay =  Numbre_play   )

@app.route('/StateRoulutes', methods=['GET', 'POST'])
def StateRoulutes( ):
    Roulute_List = []
    for var in rouleteSection.Rouletes  : 
        Roulute_List.append( {'Roulute_Id' : var.id , 'Roulute_state' : var.StateToString() }  )   

    return jsonify( Roulute_List = Roulute_List  )


