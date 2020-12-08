### 航空公司

POST : 添加航空公司		{name}

DELETE : 删除航空公司		{id}

GET : 查询航空公司列表		{} -> {id, name}

| method | url             | effect           |
| ------ | --------------- | ---------------- |
| GET    | queryAllCompay/ | 查询所有航空公司 |
| POST   | addCompany/     | 添加航空公司     |
| DELETE | deleteCompany/  | 删除航空公司     |

### 机场

POST : 添加机场		{name, city}

DELETE: 删除机场		{id}

GET: 查询所有机场		{} -> {id, name, city}

GET: 查询指定机场		{id} -> {name, city}

| method | url              | effect               |
| ------ | ---------------- | -------------------- |
| GET    | queryAllAirport/ | 查询所有机场信息     |
| GET    | queryAirport/    | 查询指定某个机场信息 |
| POST   | addAirport/      | 添加机场             |
| DELETE | deleteAirport/   | 删除机场             |

### 飞机型号

POST: 添加型号		{name, capacity, voyage}

DELETE: 删除型号		{id}

GET:查询所有型号		{} -> {id, name, capacity, voyage}

GET:查询指定型号的信息		{id} -> {name, capacity, voyage}

| method | url                | effect           |
| ------ | ------------------ | ---------------- |
| GET    | queryAllPlaneType/ | 查询所有飞机型号 |
| GET    | queryPlaneType/    | 查询指定飞机型号 |
| POST   | addPlaneType/      | 添加飞机型号     |
| DELETE | deletePlaneType/   | 删除飞机型号     |

### 飞机信息

POST: 添加飞机		{type, company, work_time}

DELETE: 删除飞机		{id}

GET: 查询所有飞机		{} -> {id,type, company, work_time}

| method | url  | effect       |
| ------ | ---- | ------------ |
| GET    |      | 查询所有飞机 |
| POST   |      | 添加航空公司 |
| DELETE |      | 删除航空公司 |

### 航线信息

POST:添加航线

DELETE:删除航线

GET:查询所有航线信息 

| method | url          | effect           |
| ------ | ------------ | ---------------- |
| GET    |              | 查询所有航线信息 |
| POST   | addRoute/    | 添加航线信息     |
| DELETE | deleteRoute/ | 删除航线信息     |

### 航班信息

POST: 添加航班		{route_id, plane_id, price, time1, time2, num}

POST:卖出一票		{account_id, flight_id}	//暂时不用写

DELETE: 删除航班

| method | url             | effect                     |
| ------ | --------------- | -------------------------- |
| GET    | queryAllFlight/ | 查询目前所有航班有关的信息 |
| POST   | addFlight/      | 添加航班                   |
| DELETE | deleteFlight/   | 删除航班                   |

### 账户信息

创建账户:{身份证号,姓名,联系方式,密码}(顾客和账户一起创建)

| method | url           | effect         |
| ------ | ------------- | -------------- |
| GET    | queryAccount/ | 查询用户账户   |
| GET    | queryAdmin/   | 查询管理员账户 |
| POST   |               | 创建账户       |