# rouletteAPI
Little API for play roulette use redis 

# dependecies 
 pip install flask
 pip install redis

# URL for the api 

http://127.0.0.1:5000/addRoulete
function : create a new roulette  
parameter : none 
return:   id_roulette and state of roulette   in format json  

{
  "Roulute_State": "Close", 
  "Roulute_id": 3
}

http://127.0.0.1:5000/open/idRoulette
function : open roulette  
parameter : idRoulette
return:   id_roulette and state of roulette   in format json  

{
  "Roulute_Message": "Open", 
  "Roulute_State": 1, 
  "Roulute_id": 1
}

http://127.0.0.1:5000/deleteAllRouletes
function : delee alld data 
parameter : none
return: Allempty message 

{
  "message": "Allempty"
}


http://127.0.0.1:5000/StateRouluttes
function : list all the roulettes with state in list  
parameter : none
return:list od roulettes  with :  id for roulettes and  data for bets and message  in format json ,
{
  "Roulute_List": [
    {
      "Roulute_Data": {
        "BetsTable": "bet3", 
        "bets": [], 
        "id": 3, 
        "state": 0
      }, 
      "Roulute_Id": 3, 
      "Roulute_Message": "Close"
    }, 
    {
      "Roulute_Data": {
        "BetsTable": "bet2", 
        "bets": [], 
        "id": 2, 
        "state": 0
      }, 
      "Roulute_Id": 2, 
      "Roulute_Message": "Close"
    }, 
    {
      "Roulute_Data": {
        "BetsTable": "bet1", 
        "bets": [
          {
            "Qty": 2000, 
            "Qty_win": 0, 
            "bet": 13, 
            "betTime": "2020-06-12T10:25:15-05:00", 
            "client": 23, 
            "id": 0, 
            "state": 1, 
            "type": 1
          }
        ], 
        "id": 1, 
        "state": 1
      }, 
      "Roulute_Id": 1, 
      "Roulute_Message": "Open"
    }, 
    {
      "Roulute_Data": {
        "BetsTable": "bet0", 
        "bets": [], 
        "id": 0, 
        "state": 0
      }, 
      "Roulute_Id": 0, 
      "Roulute_Message": "Close"
    }
  ]
}

http://127.0.0.1:5000/CloseBetRoulutte/idRoulette
function : close bet in a roulette  
parameter : idRoulette
return: list of the   with : bet , id for bet  , client id , type of bet and quanty of bet  , state of bet , and quanty of win  , and  id_roulette  in format json  

{
  "Bets_List": [
    {
      "Bet": {
        "Qty": 2000, 
        "Qty_win": 0, 
        "bet": 13, 
        "betTime": "2020-06-12T10:19:09-05:00", 
        "client": 23, 
        "id": 1, 
        "state": 3, 
        "type": 1
      }, 
      "MessageBet": "Your Loss !!!!!!  TypeBet : Number Time : 2020-06-12T10:19:09-05:00 Bet # 13 Value Bet : $2000"
    }, 
    {
      "Bet": {
        "Qty": 1000, 
        "Qty_win": 0, 
        "bet": 1, 
        "betTime": "2020-06-12T10:18:56-05:00", 
        "client": 23, 
        "id": 0, 
        "state": 3, 
        "type": 1
      }, 
      "MessageBet": "Your Loss !!!!!!  TypeBet : Number Time : 2020-06-12T10:18:56-05:00 Bet # 1 Value Bet : $1000"
    }
  ], 
  "ResultPlay": 27, 
  "Roulute_id": 1
}


http://127.0.0.1:5000/NewBetRoulutte/idRoulette/idCliente/TypeBet/Bet/BetQuanty
function : create new bet in a roulette  
parameter : idRoulette , idCliente , TypeBet , Bet , BetQuanty
return:   id for bet ,  state of the bet , id_roulette  in format json  

{
  "Bet": {
    "Qty": 2000, 
    "Qty_win": 0, 
    "bet": 13, 
    "betTime": "2020-06-12T10:25:15-05:00", 
    "client": 23, 
    "id": 0, 
    "state": 1, 
    "type": 1
  }, 
  "Bet_Id": 0, 
  "Bet_Message": "Aceppted  TypeBet : Number Time : 2020-06-12T10:25:15-05:00 Bet : 13 Value Bet : $2000", 
  "Roulute_id": 1
}


StatesRolute = ["Close","Open","Play"]
StrinStatesbet = ["Validaing" ,"Aceppted", "Win" , "Lose" , "Error"  ]
StrinValidationsbet = ["Valid","Not Valid Type","Not Valid Color 0-Red 1-Black","Not Valid Number range 0-36","Not Valid qty max value $10.000"]
