-   加载镜像

```bash
docker load < jenkins.tar.gz
docker images
```

-   启动容器

```bash
# 支持的端口号：8080-8090;80;443;8443;17878;7443;22;30713;9080;2222;30001-30100;2181;9092;9000;18080;45001;9200;60805;8099;10107
docker run -d -p 填写支持的端口号:8080 --name jenkins 镜像:版本
docker ps
```

-   进入容器

```bash
docker exec -it 容器id /bin/bash
```

-   更换jenkins源

```bash
vim .jenkins/hudson.model.UpdateCenter.xml
将地址改为如下地址
# http://mirrors.tools.huawei.com/jenkins/updates/update-center.json
```

-   重启容器

```bash
docker restart 容器id
```


