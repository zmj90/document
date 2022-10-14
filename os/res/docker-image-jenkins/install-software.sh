#!/bin/sh

# 构建python
tar -zxvf Python-3.10.6.tgz
cd Python-3.10.6
./configure
make && make install
python3 -V

# 安装一些python第三方库
cd ..
pip3 install -U pip
mkdir /root/.pip
mv pip.conf /root/.pip
pip3 install -r requirements.txt

# 安装谷歌浏览器
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get -y -f install 
google-chrome --version

# 安装jdk
tar -zxvf jdk-11.0.15_linux-x64_bin.tar.gz -C /usr/local
java -version

# 安装tomcat
tar -zxvf apache-tomcat-8.5.81.tar.gz -C /usr/local/
mv setenv.sh /usr/local/apache-tomcat-8.5.81/bin/

# jenkins
mv jenkins.war /usr/local/apache-tomcat-8.5.81/webapps/
