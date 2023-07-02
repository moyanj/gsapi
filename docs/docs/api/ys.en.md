# Genshin Impact

## All information

- URL: /ys/all

- Method: GET

- Description: According to UID, request the HoYoLab server or Enka server to resolve it into a simpler and more direct one

- Parameters:

| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| UID | GET parameter | player Genshin Impact UID |

- Result significance

| Result Name | Type | Meaning | Example |
|: -------- |: -------- |: -------- |: --------|
| nickName | String | Player Nickname | Mo Yan |
| level | Number | Player Adventure Level | 45 |
| WL | Number | Player World Level | 5 |
| sign | string | player signature | 19 orders extracted from Nahida |
| NOA | Number | Number of Achievements | 265 |
| Abyss.string | String | Abyss Bar | 5-1 |
| Abyss.floor | Number | Number of Abyss | 5 |
| Abyss.room | Number | Number of Abyss | 1 |

- Example:
 
    - Request: GET /ys/all?uid=243997737

    - Response:

``` json

    {
        "nickName": "Mo Yan",
        "level": 45,
        "WL": 5,
        "sign": "19 single draw Nahida",
        "NOA": 265,
        "abyss":{
            "string": "5-1",
            "floor": 5,
            "room": 1
        }
    }

```

## Player nickname

- URL:/ys/name

- Method: GET

- Description: Obtain player nickname

- Parameters:

| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| uid | GET parameter | player Genshin Impact UID |

- Result significance
<br>
plain text

- Example:

- Request: GET /ys/name?uid=243997737

- Response:

```
Mo Yan
```



## Player adventure level

- URL:/ys/level

- Method: GET

- Description: Obtain player adventure level

- Parameters:



| Parameter Name | Type | Meaning |
|: ------ |: ------ |: ------|
| uid | GET parameter | player Genshin Impact UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /ys/level?uid=243997737

    -Response:

```

45

```



## Player World Level

- URL:/ys/wl

- Method: GET

- Description: Obtain player world level

- Parameters:



| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| uid | GET parameter | player Genshin Impact UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET/ys/wl?uid=243997737

    - Response:

```

5

```



## Player Signature

- URL:/ys/sign

- Method: GET

- Description: Obtain player signature

- Parameters:



| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| uid | GET parameter | player Genshin Impact UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /ys/sign?uid=243997737
    - Response:

```

Mo Yan ssssssssss

```



## Number of player achievements

- URL:/ys/achieve

- Method: GET

- Description: Obtain the number of player achievements

- Parameters:



| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| uid | GET parameter | player Genshin Impact UID|



- Result significance

<br>

plain text



- Example:

    - Request: GET /ys/achieve?uid=243997737

    - Response:

```

265

```



## Player Abyss Layer Count

- URL:/ys/abyss/floor

- Method: GET

- Description: Obtain the player's Abyss layer count

- Parameters:



| Parameter Name | Type | Meaning |

|: -------- |: -------- |: --------|

| uid | GET parameter | player Genshin Impact UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /ys/abyss/floor?uid=243997737

    -Response:

```

5

```



## Number of Players in Abyss

- URL:/ys/byss/room

- Method: GET

- Description: Obtain the number of players in the Abyss

- Parameters:



| Parameter Name | Type | Meaning |

|: -------- |: -------- |: --------|

| uid | GET parameter | player Genshin Impact UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /ys/byss/room?uid=243997737

    - Response:

```

3

```