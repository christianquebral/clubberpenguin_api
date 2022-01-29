# CLUBBERPENGUIN API

## API For ClubberPenguin 
(Not affiliated with Club Penguin)
Play now at clubberpenguin.com!

## Usage
All responses will have the form
```json
{
	"success": boolean,
	"message": "",
	"data": {}
}
```
The following definitions will only detail the response in the `data` field.

`POST/PUT` requests are limited to application use.

### Get Player Stats
#### Definition
`GET /player/{player name}`
Returns a single JSON object with player stats information.  These stats are updated every time a player concludes a game.
#### Response
`200 OK` on success
```
{
    "player_id": "2",
    "player_name": "ANGRY PENGUIN",
    "high_score": 2550,
    "total_score": "2550",
    "player_rank": "2",
    "games_played": 1,
    "average_game_duration": "184.69020080566406",
    "total_game_duration": "184.69020080566406",
    "date_joined": "2022-January-29th"
}
```

### Get Leaderboard List
#### Definition
`GET /leaderboard`
Returns a JSON array containing data of the highest scoring games.  This is used to populate the LEADERBOARD menu within
the game.
#### Response
`200 OK` on success
```
[
    {
      "player_rank": 1,
      "player_name": "PONK_TOWN",
      "player_score": 3110,
      "date_achieved": "2022-01-29 00:02:53"
    },
    {
      "player_rank": 2,
      "player_name": "ANGRY PENGUIN",
      "player_score": 2550,
      "date_achieved": "2022-01-29 00:50:41"
    }
    < ... >
]
```

### Get Game Data
#### Definition
`GET /games`
Returns a JSON array containing data for the last 50 games played.  
#### Response
`200 OK` on success
```
[
    {
      "game_id": 2,
      "player_id": 2,
      "player_name": "ANGRY PENGUIN",
      "player_score": 2550,
      "created_date": "2022-01-29 00:50:41"
    },
    {
      "game_id": 1,
      "player_id": 1,
      "player_name": "PONK_TOWN",
      "player_score": 3110,
      "created_date": "2022-01-29 00:02:53"
    }
]
```

### Get Store Items
#### Definition
`GET /store`
Returns a JSON array containing items sold in the in-game store.
#### Response
`200 OK` on success
```
[
    {
      "item_id": 5,
      "item_name": "red_beanie",
      "item_price": 3000,
      "item_type": "head"
    },
    {
      "item_id": 6,
      "item_name": "green_beanie",
      "item_price": 3000,
      "item_type": "head"
    },
    {
      "item_id": 7,
      "item_name": "blue_beanie",
      "item_price": 3000,
      "item_type": "head"
    }
    < ... >
]
```

### Get Player Inventory
#### Definition
`GET /player/{player name}/inventory`
Returns a JSON object containing inventory data for a specific player.  
Inventories are populated once players make purchases in the in-game store using points earned while playing.
#### Response
`200 OK` on success
```
{
    "player_id": 2,
    "player_name": "ANGRY PENGUIN",
    "remaining_balance": 730,
    "inventory": "blue_beanie"
}
```
