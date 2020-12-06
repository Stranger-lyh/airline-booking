### 航空公司

POST : 添加航空公司		{name}

DELETE : 删除航空公司		{id}

GET : 查询航空公司列表		{} -> {id, name}

### 机场

POST : 添加机场		{name, city}

DELETE: 删除机场		{id}

GET: 查询所有机场		{} -> {id, name, city}

GET: 查询指定机场		{id} -> {name, city}

### 飞机型号

POST: 添加型号		{name, capacity, voyage}

DELETE: 删除型号		{id}

GET:查询所有型号		{} -> {id, name, capacity, voyage}

GET:查询指定型号的信息		{id} -> {name, capacity, voyage}

### 飞机信息

POST: 添加飞机		{type, company, work_time}

DELETE: 删除飞机		{id}

GET: 查询所有飞机		{} -> {id,type, company, work_time}

GET: 查询指定飞机信息		{id} -> {type, company, work_time}

### 航线信息

POST:添加航线

DELETE:删除航线





### 航班信息

POST: 添加航班		{}

POST:卖出一票		{account_id, flight_id}

DELETE: 删除航班