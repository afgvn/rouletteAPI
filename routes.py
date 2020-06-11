from app import app, db
from flask import  jsonify
from datetime import datetime

@app.route('/')
@app.route('/index')

def index():

    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def NewRoulutte():
    var =  'crear ruleta'
    return jsonify( Roulutte_id = 10, Roulutte_State = "close")

@app.route('/open/<int:Roulutte_id>', methods=['GET', 'POST'])
def openRoulutte(Roulutte_id):
    RoulutteOpenid = Roulutte_id
    Roulutte_State = "open"

    return jsonify( Roulutte_id = RoulutteOpenid, Roulutte_State = Roulutte_State )

@app.route('/NewBetRoulutte/<int:Roulutte_id>/<int:Client_id>/<int:Type_bet>/<int:Qty_bet>', methods=['GET', 'POST'])
def betRoulutte(Roulutte_id , Client_id , Type_bet, Qty_bet ):
    RoulutteOpenid = Roulutte_id
    bet = {'Bet_Id': 1 ,'Client_id' : 23,'Type_bet' : 0, 'Qty_bet' : 1000}
    Bet_State = "Cancel"
    Bet_Id = 1

    return jsonify( Roulutte_id = RoulutteOpenid , Bet_Id= Bet_Id , Bet_State = Bet_State  )

@app.route('/CloseBetRoulutte/<int:Roulutte_id>', methods=['GET', 'POST'])
def CloseBetRoulutte(Roulutte_id  ):
    RoulutteOpenid = Roulutte_id
    Bets_List = [
        {'Bet_Id' : 1,'Client_id' : 23,'Type_bet' : 0, 'Qty_bet' : 1000 , 'State_bet' : "Win" , 'Qty_win' : 1000 },
        {'Bet_Id' : 2,'Client_id' : 56,'Type_bet' : 1, 'Qty_bet' : 104500 , 'State_bet' : "lose" , 'Qty_win' : 0 }
    ]

    return jsonify( Roulutte_id = RoulutteOpenid , Bets_List= Bets_List   )

@app.route('/StateRouluttes', methods=['GET', 'POST'])
def StateRouluttes( ):
    Roulutte_List = [
        {'Roulutte_Id' : 1,'Roulutte_state' : "open"},
        {'RoulutteBet_Id' : 2,'Roulutte_state' : "close"}
    ]

    return jsonify( Roulutte_List = Roulutte_List  )


