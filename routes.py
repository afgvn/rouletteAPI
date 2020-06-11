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
    Bet_State = "Error Roulute not exist -- bet   cancelled"
    if  Roulute_id < len( rouleteSection.Rouletes ):
            Bet_State = "Error Roulute its close --  bet  cancelled"
            if  rouleteSection.Rouletes[Roulute_id].state == 1:
                newBetReturn = rouleteSection.Rouletes[Roulute_id].NewBet(  Client_id , Type_bet , Bet , Qty_bet )   #client , type , bet , Qty 
                Bet_State = newBetReturn['Bet_State']
                Bet_Id = newBetReturn['Bet_Id']


    return jsonify( Roulute_id = RouluteOpenid , Bet_Id= Bet_Id , Bet_State = Bet_State  )

@app.route('/CloseBetRoulute/<int:Roulute_id>', methods=['GET', 'POST'])
def CloseBetRoulute(Roulute_id  ):
    RouluteOpenid = Roulute_id
    Bets_List = [
        {'Bet_Id' : 1,'Client_id' : 23,'Type_bet' : 0,'Bet' : 3, 'Qty_bet' : 1000 , 'State_bet' : "Win" , 'Qty_win' : 1000 },
        {'Bet_Id' : 2,'Client_id' : 56,'Type_bet' : 1,'Bet' : 0, 'Qty_bet' : 104500 , 'State_bet' : "lose" , 'Qty_win' : 0 }
    ]

    return jsonify( Roulute_id = RouluteOpenid , Bets_List= Bets_List   )

@app.route('/StateRoulutes', methods=['GET', 'POST'])
def StateRoulutes( ):
    Roulute_List = []
    for var in rouleteSection.Rouletes  : 
        Roulute_List.append( {'Roulute_Id' : var.id , 'Roulute_state' : var.StateToString() }  )   

    return jsonify( Roulute_List = Roulute_List  )


