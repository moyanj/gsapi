# Honkai: Star Rail

## All information

- URL: /sr/all

- Method: GET

- Description: According to UID, request the Mi You She server or ELi server to resolve it into a simpler and more direct one

- Parameters:

| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
|uid | GET parameter | player Honkai: Star Rail UID |



-Result significance

| Result Name | Type | Meaning | Example |
|: -------- |: -------- |: -------- |: --------|
| nickName | String | Player Nickname | Mo Yan |
| level | Number | Player Adventure Level | 45 |
| WL | Number | Player World Level | 5 |
| sign | string | player signature | 19 orders extracted from Grass God |
| Friend | number | number of friends | 25 |
| Birthday | number string | birthday | 20210805 |



- Example:

    - Request: GET /sr/all?uid=243997737

    - Response:

```Json

{

    "mickName": "Mo Yan",
    "level": 45,
    "WL": 5,
    "sign":" 19 Single Extraction Grass God ",
    "friend":25,
    "birthday":"20120405"
}

```




## Player nickname

- URL: /sr/name

- Method: GET

- Description: Obtain player nickname

- Parameters:

| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| uid | GET parameters | Player Honkai: Star Rail UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /sr/name?uid=243997737

    - Response:

```

Mo Yan

```



## Player Development Level

- URL:/sr/level

- Method: GET

- Description: Obtain player development level

- Parameters:



| Parameter Name | Type | Meaning |
|: ------ |: ------ |: ------|
| uid | GET parameters | Player Honkai: Star Rail UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /sr/level?uid=243997737

    - Response:

```

45

```



## Player Balance Level

- URL:/sr/wl

- Method: GET

- Description: Obtain player balance level

- Parameters:



| Parameter Name | Type | Meaning |
|: -------- |: -------- |: --------|
| uid | GET parameters | Player Honkai: Star Rail UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET /sr/wl?uid=243997737

    - Response:

```

five

```



## Player Signature

- URL:/sr/sign

- Method: GET

- Description: Obtain player signature

- Parameters:

| Parameter Name | Type | Meaning |

|: -------- |: -------- |: --------|

| uid | GET parameters | Player Honkai: Star Rail UID |



- Result significance

<br>

plain text



- Example:

    - Request: GET/sr/sign?uid=243997737

    - Response:

```

Mo Yan ssssssssss

```