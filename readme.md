# Informações do Projeto
- Projeto do Cliente: WorkDB
- Desenvolvedor: Alexsandro Gehlen

# Descrição
```
Desenvolvimento de API para inserção de informações sobre estacionamento.

```


## Crie um Endpoint com Python e Django seguindo as instruções abaixo.
```
tabelas criadas:

TB_CUSTOMER
ID PK
NAME VARCHAR(50)
---------------------------
TB_CUSTOMER_VEHICLES
ID INT PK
CUSTOMER_ID INT FK
PLATE VARCHAR(10)

KIND INT(1= moto 2=carro)
------------------------------------
TB_PARKMOVEMENT
ID INT
ENTRY_DATE DATE
EXIT_DATE DATE
VALIDATE_DATE DATE
VALUE REAL
VEHICLE_ID INT FK
PLATE VARCHAR(50)
----------------------------------
```

# Instruções
Execução
```
python manage.py runserver
```
## Customer
Para inserção de novos usários
```
POST
/api/v1/customers/
```
Para alteração de usários
```
PUT
/api/v1/customers/pk/
```

## Vehicles
Para inserção de novos veiculos
```
POST
/api/v1/vehicles/
```
Para alteração de veiculos
```
PUT
/api/v1/vehicles/pk/
```

## Movements
Para inserção de entrada
```
POST
/api/v1/movements/
```
Para alteração de entrada
```
PUT
/api/v1/movements/pk/
```

## Movements Exit
Para dar baixa
```
PUT
/api/v1/movements_exit/pk/
```