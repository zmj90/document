Postman动态变量

```javascript
1 {{$guid}}:uuid
2 {{$timestamp}}:时间戳
3 {{$randomInt}}:0~1000随机数

```



```javascript
var jsonData = pm.response.json();
for (var i=0; i<jsonData.data.length;i++){
var flag="flag"+i;
var uuid="uuid"+i
pm.environment.set(flag, jsonData.data[i].deleteFlag);
pm.environment.set(uuid, jsonData.data[i].taskUUID);
// console.log(flag);
// console.log(jsonData.data[i].deleteFlag);
}
```



```javascript
var jsonData = pm.response.json();
var id = jsonData.data.id;
pm.environment.set("id", id);
```

