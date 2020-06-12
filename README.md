# rouletteAPI
Little API for play roulette 




# dependecies 
 pip install flask
 pip install redis

# URL for the api 

http://127.0.0.1:5000/add
function : create a new roulette  
parameter : none 
return:   id_roulette and state of roulette   in format json  

{
  "Roulutte_State": "close", 
  "Roulutte_id": 10
}

http://127.0.0.1:5000/open/idRoulette
function : open roulette  
parameter : idRoulette
return:   id_roulette and state of roulette   in format json  

{
  "Roulutte_State": "open", 
  "Roulutte_id": 5
}

http://127.0.0.1:5000/StateRouluttes
function : list all the roulettes with state in list  
parameter : none
return:list od roulettes  with :  id for roulettes and  state in format json ,

{
  "Roulutte_List": [
    {
      "Roulutte_Id": 1, 
      "Roulutte_state": "open"
    }, 
    {
      "RoulutteBet_Id": 2, 
      "Roulutte_state": "close"
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
      "Bet": 20,
      "Bet_Id": 1, 
      "Client_id": 23, 
      "Qty_bet": 1000, 
      "Qty_win": 1000, 
      "State_bet": "Win", 
      "Type_bet": 0
    }, 
    {
      "Bet": 20,
      "Bet_Id": 2, 
      "Client_id": 56, 
      "Qty_bet": 104500, 
      "Qty_win": 0, 
      "State_bet": "lose", 
      "Type_bet": 1
    }
  ], 
  "Roulutte_id": 5
}


http://127.0.0.1:5000/NewBetRoulutte/idRoulette/idCliente/TypeBet/Bet/BetQuanty
function : create new bet in a roulette  
parameter : idRoulette , idCliente , TypeBet , Bet , BetQuanty
return:   id for bet ,  state of the bet , id_roulette  in format json  

{
  "Bet": 20,
  "Bet_Id": 1, 
  "Bet_State": "Cancel", 
  "Roulutte_id": 5
}
