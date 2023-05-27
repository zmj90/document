@[TOC](proEnv)

> 首先去官网查看需要什么安装环境

# multipass

https://multipass.run/docs

```shell
# 准备条件：

# 关闭防火墙

# 初始化
multipass set local.driver=virtualbox
multipass set local.privileged-mounts=true

# 创建实例
multipass launch --network WLAN -d 10G -n primary
multipass launch --network WLAN -d 10G -n primary docker

# 挂载与取消挂载
multipass mount D:\doing\ubuntu primary:/home/ubuntu/zmj
multipass umount primary:Home
```



# docker

## install

```sh
#!/bin/sh
sudo apt-get remove docker docker-engine docker.io containerd runc

sudo apt-get update

sudo apt-get install -y ca-certificates curl gnupg lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin


```



## dockerfile

-   eg1

```bash
# FROM scratch
FROM ubuntu:20.04
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak \
&& sed -ri "s/(archive|security).ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
```

-   规定

```shell
不指定目录默认在根目录
```



```shell
docker build -t ubuntu-z:20.04 .
```



# ubuntu

```shell
#!/bin/sh
# 更换源
cp /etc/apt/sources.list /etc/apt/sources.list.bak
sed -ri "s/(archive|security).ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list
sed -ri "s/(archive|security).ubuntu.com/mirrors.aliyun.com/g" /etc/apt/sources.list
apt-get update
apt-get install --assume-yes apt-utils
apt-get -y install sudo vim fontconfig inetutils-ping locales wget git mysql-client make gcc build-essential python-dev python-setuptools python-pip python-smbus libncursesw5-dev \
libgdbm-dev libc6-dev zlib* libssl-dev libsqlite3-dev tk-dev libffi-dev
DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata
# 修复依赖关系(depends)
sudo apt-get -f install

```

## dpkg

```shell
dpkg-reconfigure tzdata
```



## 环境变量

```bash
1. 什么是环境变量
环境变量（environment variables）一般是指在操作系统中用来指定操作系统运行环境的一些参数，这些参数会对系统行为产生影响。

比如常用的PATH环境变量，当要求系统运行一个程序而没有告诉它程序所在的完整路径时，系统除了在当前目录下面寻找此程序外，还会到PATH中指定的路径去找。你可以在终端使用printenv PATH查看当前PATH变量的值。

2. 用户环境变量和系统环境变量
Ubuntu系统包含两类环境变量：系统环境变量和用户环境变量。系统环境变量对所有系统用户都有效，用户环境变量仅仅对当前的用户有效。

用户环境变量可存储在以下文件中：
~/.profile
~/.bashrc, ~/.bash_profile, ~/.bash_login
推荐将环境变量保存在~/.profile中，因为无论是通过控制台还是图形界面启动程序时，都会自动执行该文件。
而~/.bashrc, ~/.bash_profile, ~/.bash_login这些文件，当通过shell启动程序时，它们也会被加载；但当通过图形界面环境启动程序时，这些文件中的环境变量设置便不可用了。

系统环境变量可存储在以下文件中：
/etc/profile
/etc/profile.d（它是文件夹）
/etc/bash.bashrc
/etc/profile和/etc/profile.d都是常用的设置环境的地方。其中/etc/profile.d文件夹来源于/etc/profile，在该目录下的*.sh，即以sh为后缀的文件都会被加载。
类似地，不推荐使用/etc/bash.bashrc，因为在图形界面环境下启动程序时，不会加载它里边的环境变量设置。

3. 设置永久环境变量实例（以/etc/profile为例）
vim /etc/profile

在文件末尾处添加如下，保存并退出：
export JAVA_HOME=/usr/lib/jvm/jdk1.7.0
export PATH=$PATH:$JAVA_HOME/bin
其中，export命令：使得变量真正输出成为环境变量。

source /etc/profile


```



## git

```bash
# C:\Program Files\Git\etc\gitconfig	系统
# C:\Users\zmj\.gitconfig	用户
git config -l
git config --system --list
git config --global -l
$ git config --global user.name "[name]"
对你的commit操作设置关联的用户名
$ git config --global user.email "[email address]"
对你的commit操作设置关联的邮箱地址
$ git config --global color.ui auto
启用有帮助的彩色命令行输出
git config --global user.name "钟马俊"
git config --global user.email 674495630@qq.com
```



## ssh

```shell
1. 安装ssh服务 ： sudo apt-get install openssh-server
2. 查看ssh服务状态 ： ps -e|grep ssh
3. 启动关闭： sudo service ssh start/restart/stop
4. 登录：ssh  levi@192.168.100.5    # 登录
5. 退出：exit
6. scp拷贝
	# 注意：`:` 后面的路径写绝对路径
	scp  demo.py levi@192.168.100.5:/home/tarena
	# 把远程主目录下demo.py文件 复制到本地当前目录下
	scp  levi@192.168.100.5:/home/tarena/demo.py  .
	# 加上 -r 选项可以传送文件夹
	scp -r demo levi@192.168.100.5:/home/tarena/
7. ssh秘钥 使用方法
	1. 在个人计算机中生产秘钥对 ： ssh-keygen  执行以后会在主目录下生成一个.ssh文件夹,其中包含私钥文件	id_rsa和公钥文件id_rsa.pub。
	2. 在服务器主机上创建文件~/.ssh/authorized_keys，将信任的计算机的id_rsa.pub文件内容追加到服务器	 authorized_keys文件中。
	chmod 600 authorized_keys
	chmod 700 .ssh

ssh-keygen -t rsa -C "674495630@qq.com"


# 开启密码登录
vim /etc/ssh/sshd_config

PubkeyAuthentication yes #启用PublicKey认证
AuthorizedKeysFile .ssh/authorized_keys #PublicKey文件路径
PasswordAuthentication no #不适用密码认证登录	修改这项就可以

systemctl restart sshd
```

## selenium

```python
# 配置浏览器驱动
【1】定义
    phantomjs为无界面浏览器(又称无头浏览器)，在内存中进行页面加载,高效
【2】下载地址
    2.1) chromedriver : 下载对应版本
		http://npm.taobao.org/mirrors/chromedriver/  
    2.2) geckodriver
    	https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html
    	http://npm.taobao.org/mirrors/geckodriver/
		https://github.com/mozilla/geckodriver/releases    
    2.3) phantomjs
       https://phantomjs.org/download.html
【3】Ubuntu安装
    3.1) 下载后解压 : tar -zxvf geckodriver.tar.gz 
    3.2) 拷贝解压后文件到 /usr/bin/ （添加环境变量）
         sudo cp geckodriver /usr/bin/
    3.3) 添加可执行权限
         sudo chmod 777 /usr/bin/geckodriver
【4】Windows安装
    4.1) 下载对应版本的phantomjs、chromedriver、geckodriver
    4.2) 把chromedriver.exe拷贝到python安装目录的Scripts目录下(添加到系统环境变量)
         # 查看python安装路径: where python
    4.3) 验证
         cmd命令行: chromedriver
# 验证
【Ubuntu | Windows】
ipython3
from selenium import webdriver
webdriver.Chrome()
或者
webdriver.Firefox()
【mac】
ipython3
from selenium import webdriver
webdriver.Chrome(executable_path='/Users/xxx/chromedriver')
或者
webdriver.Firefox(executable_path='/User/xxx/geckodriver')
```

## mysqlclient

```python
# ubuntu
1. 安装 mysqlclient [版本 mysqlclient 1.3.13以上 ，官网目前为1.4.x]
    - 安装前确认ubuntu是否已安装 python3-dev 和  default-libmysqlclient-dev

    - sudo apt list --installed|grep -E 'libmysqlclient-dev|python3-dev' 

- 若命令无输出则需要安装 -  sudo apt-get install python3-dev default-libmysqlclient-dev

    - 确保上述两个库已经安装，执行 sudo pip3 install mysqlclient即可 
# ubuntu
sudo apt install nginx

# ubuntu
查看已安装的库
   sudo pip3 list|grep -i 'uwsgi'
   sudo pip3 freeze|grep -i 'uwsgi'
   -i 参数指 不区分大小写
   如果pip3安装过uwsgi，则会输出
   uWSGI==2.0.18
   uWSGI 2.0.18
```



## mysql

-   client

```bash
apt-get install mysql-client

```



```shell
show databases;
use mysql;
update user set authentication_string=PASSWORD("自定义密码") where user='root';
update user set plugin="mysql_native_password";
flush privileges;
https://www.cnblogs.com/xiwusheng/p/10925669.html
查看：mysql -V
【1】修改配置文件,允许远程连接
linux开启连接步骤：
    sudo gedit /etc/mysql/mysql.conf.d/mysqld.cnf
    将如下行注释并保存退出:
     # bind-address = 127.0.0.1
windows开启连接步骤：
1.进入mysql命令行
2.输入use mysql; 回车
3.输入update user set host = ‘%’ where user =‘root’; 回车
4.输入flush privileges; 回车
5.输入quit；退出
     
【2】给用户授权
    mysql -uroot -p123456
    mysql> grant all privileges on *.* to 'root'@'%' identified by '123456' with grant option;
    mysql> flush privileges;
    
【3】重启MySQL服务
    sudo /etc/init.d/mysql restart
    
【4】远程连接测试(远程服务器上)
    mysql -hIP地址 -uroot -p123456
```



>   Important
>
>   MySQL 8.0 Server requires the Microsoft Visual C++ 2015 Redistributable Package to run on Windows platforms. Users should make sure the package has been installed on the system before installing the server. The package is available at the [Microsoft Download Center](http://www.microsoft.com/en-us/download/default.aspx). Additionally, MySQL debug binaries require Visual Studio 2015 to be installed.
>
>   MySQL 8.0 Server 需要 Microsoft Visual C++ 2015 Redistributable Package 才能在 Windows 平台上运行。用户在安装服务器之前应确保系统上已安装该软件包。该软件包可从 [Microsoft 下载中心获得](http://www.microsoft.com/en-us/download/default.aspx)。此外，MySQL 调试二进制文件需要安装 Visual Studio 2015。

-   my.ini

```shell
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8

[mysqld]
port=3306
basedir=C:/Program Files/MySQL/mysql-5.7.32-winx64
datadir=C:/Program Files/MySQL/mysql-5.7.32-winx64/data
max_connections=200
max_connect_errors=10
character-set-server=utf8
default-storage-engine=INNODB
server-id=1
loose_mysqlx_port=33060
```



```shell
1 mysqld --initialize-insecure --console
# mysqld --defaults-file="C:\Program Files\MySQL\mysql-8.0.23-winx64\my.ini" --initialize-insecure --console
2 mysqld --install
# .\mysqld --install mysql8.0.23 --defaults-file="C:\Program Files\MySQL\mysql-8.0.23-winx64\my.ini"
# 更改注册表
# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services
3 net start mysql8.0.23
4 mysql -uroot -p
5 ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码'
# mysqladmin -u用户名 -p旧密码 password 新密码
# mysqld --remove
# sc delete mysql
# mysqld --console # 前台启动
# net start mysql
# net stop mysql
# "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqladmin" -u root shutdown

# 查看启动的服务
net start | find /i "mysql"
# 查看启动的进程
tasklist
```



~/.vimrc

```bash
set termencoding=utf-8
set encoding=utf8
set fileencodings=utf8
```









# python

## install

```shell
# Ubuntu

################################ 在线安装python
ubuntu 系统级组件 如下命令安装
sudo apt-get install  名字
sudo apt install software-properties-common -y
# 第三方维护的PPA软件源来方便的安装所需要的Python版本
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7

https://packaging.python.org/guides/installing-using-linux-tools/#debian-ubuntu
sudo apt install python3-venv python3-pip

################################ 离线安装python
# 安装依赖
https://devguide.python.org/setup/#install-dependencies
sudo apt-get install pkg-config
sudo apt-get install make gcc build-essential zlib*
      
tar -zxvf Python-3.6.1.tgz
./configure --with-pydebug --prefix=/usr/local/bin/python3.8.2
make && make install


```



## pip

-   pip.conf

    ```bash
    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    [install]
    trusted-host = https://pypi.tuna.tsinghua.edu.cn
    ```

    ​

```shell
################################ 配置pip源
https://pip.pypa.io/en/stable/user_guide/#configuration


python -m pip install -U pip
-m:导入模块
-U：升级。原来已经安装的包，带上U才会更新到最新版本，不带U不会装新版本。
pip3 - Python库的管理工具
   sudo pip3 install uwsgi==2.0.18 -i https://pypi.tuna.tsinghua.edu.cn/simple/
-i 参数 指定当前 安装命令 去哪个网站下载 安装包
    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    华中理工大学：http://pypi.hustunique.com/
    山东理工大学：http://pypi.sdutlinux.org/
    豆瓣：http://pypi.douban.com/simple/
      
查看已安装的库
sudo pip3 list|grep -i 'uwsgi'
-i 参数指 不区分大小写 
pip3 show requests
pip freeze > requirements.txt

pip --help
pip list -h
pip list -o
# 卸载
sudo pip3 uninstall django

################################ 离线安装python第三方库
1、tar -zxvf django-cors-headers-3.0.2.tar.gz
	tar -xvf Django-2.2.12.tar.gz`
2、cd django-cors-headers-3.0.2
3、sudo python3 setup.py install
4、pip3 freeze|grep -i 'cors'

################################ 在线安装python第三方库
sudo pip3 install django==2.2.12 -i https://pypi.mirrors.ustc.edu.cn/simple/
									https://pypi.tuna.tsinghua.edu.cn/simple/
									http://mirrors.aliyun.com/pypi/simple/
									http://pypi.douban.com/simple/


################################ python虚拟环境安装
# https://docs.python.org/zh-cn/3/tutorial/venv.html
# 方法一
1 python3 -m venv tutorial-env
2 source tutorial-env/bin/activate
# 方法二
pycharm创建虚拟环境

################################ 多版本python中pip配置
# 例如：python3.6和python3.8
1. sudo cp pip pip3.6
2. sudo cp pip pip3.8
3. sudo vim pip3.6或者pip3.8
4. 更改第一行python所在路径

################################ 多版本python中的ipython库的配置
# 1 找到ipython的位置
which ipython
# 2 复制一份
例如：cp ipython ipython3.8
# 3 打开文件更改相应的版本号变量
vim ipython3.8
```



## 模块搜索路径

### 添加方式

1.  `PYTHONPATH`
2.  在site-packages中创建*.pth文件
3.  sys.path
4.  将模块直接放入site-packages
5.  集成开发环境



## chrome

```shell
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -f install 
google-chrome --version
```





# jdk

```bash
# 解压
tar -zxvf jdk-11.0.15_linux-x64_bin.tar.gz -C /usr/local
vim .bashrc
# 添加一下内容 保存
export JAVA_HOME=/usr/local/jdk-11.0.15
export CLASS_PATH=.:${JAVA_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
# 使文件生效
source .bashrc
# 测试
java -version

```







# tomcat

```bash
tar -zxvf apache-tomcat-8.5.81.tar.gz -C /usr/local/
# 启动
./startup.sh //直接启动
nohup ./startup.sh & //作为服务启动
./catalina.sh run //控制台动态输出方式启动，动态的显示tomcat控制台输出信息，Ctrl+c退出并停止服务
```

-   $CATALINA_HOME/bin/setenv.sh

    ```shell
    # 解决jenkins日志乱码
    JAVA_OPTS="$JAVA_OPTS -Dfile.encoding=utf-8 --illegal-access=warn -Dhudson.footerURL=https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json"
    ```

-   $CATALINA_HOME/webapps/manager/META-INF/context.xml

    ```shell
    # 限制ip访问（manager 应用）
    <Context antiResourceLocking="false" privileged="true" >
      <CookieProcessor className="org.apache.tomcat.util.http.Rfc6265CookieProcessor"
                       sameSiteCookies="strict" />
      <!--
      <Valve className="org.apache.catalina.valves.RemoteAddrValve"
             allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1" />
      -->
      <Valve className="org.apache.catalina.valves.RemoteAddrValve"
             allow="127\.\d+\.\d+\.\d+|::1|0:0:0:0:0:0:0:1|192.168.1.163" />
      <Manager sessionAttributeValueClassNameFilter="java\.lang\.(?:Boolean|Integer|Long|Number|String)|org\.apache\.catalina\.filters\.CsrfPreventionFilter\$LruCache(?:\$1)?|java\.util\.(?:Linked)?HashMap"/>
    </Context>
    ```

-   $CATALINA_HOME/conf/tomcat-users.xml

    ```shell
    # 设置用户名和密码（manager 应用）
    <!--
      <user username="admin" password="<must-be-changed>" roles="manager-gui"/>
      <user username="robot" password="<must-be-changed>" roles="manager-script"/>
    -->
    <user username="admin" password="<must-be-changed>" roles="manager-gui,manager-status"/>
    ```

    ​



# jenkins

```bash
# 后台运行
nohup java --illegal-access=warn -Dhudson.footerURL=https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json -jar jenkins.war --httpPort=8080 &

# 采用通用的URL方式，就可以实现Jenins的停止，重启和重载。
http://[jenkins-server-address][:port]/[command] where [command] can be
exit to shutdown jenkins 
restart to restart jenkins 
reload to reload the configuration
```



-   ./jenkins

```shell
# 更新插件地址
vim hudson.model.UpdateCenter.xml

https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
http://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
https://mirrors.aliyun.com/jenkins/updates/update-center.json
https://mirrors.huaweicloud.com/jenkins/updates/update-center.json
```







# jmeter

```bash
jmeter运行环境搭建
1 需要安装JDK
    - JDK--Java开发工具包
    - JRE--Java运行时环境
    - JVM--Java虚拟机
2 验证机器是否安装好Java环境
    - java -version
    - java 验证系统的环境变量path是否设置ok
3. 设置环境变量-目标：任意路径可以识别jmeter
    - JMETER_HOME
        eg:- D:\BaiduNetdiskDownload\apache-jmeter-5.4.1
    - PATH
        eg:- D:\BaiduNetdiskDownload\apache-jmeter-5.4.1\bin
        - %JMETER_HOME%\bin-推荐使用这个
```












