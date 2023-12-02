# 打开命令提示符

```shell
1 cmd 回车
2 ctrl+shift+cmd 回车 # 管理员登录
3 windows + r # 输入命令
4 windows 搜索 # 输入命令
5 通配符:？*
```

# dos命令(字母分类)

```shell
help
# help 命令 或 命令 /？
# 命令 /help 完整的帮助信息
```

```bash
@echo off
start cmd /k mysql -uroot -p123456
start cmd /k mysql -uroot -p123456 -P3307
```

```
https://baike.baidu.com/item/MS-DOS/1120792?fr=aladdin#6
https://baike.baidu.com/item/dos/6672671#1
https://baike.baidu.com/item/DOS/32025?fr=aladdin#1
```



## A

```shell
# 显示和修改地址解析协议中的条目 (ARP) 缓存。
arp
```

## B

```shell

```

## C

```shell
#1 从一个批处理程序调用另一个批处理程序，而不停止父批处理程序。当在脚本或批处理文件外使用时，调用在命令提示符下不起作用。
call
#2 显示当前目录的名称或更改当前目录。 如果仅用于驱动器号 (例如， cd C:) ， cd 将显示指定驱动器中当前目录的名称。 如果在没有参数的情况下使用， cd 将显示当前驱动器和目录。
cd
#3 更改活动控制台代码页。 如果使用不带参数， chcp 显示活动控制台代码页的数目。
chcp
chcp 936	#简体中文	
chcp 65001	#utf-8
#4 清除 "命令提示符" 窗口。
cls
#5 启动命令解释器 Cmd.exe 的新实例。 如果不使用参数， cmd 将显示操作系统的版本和版权信息。
cmd
#6 更改当前会话的命令提示符窗口中的前景色和背景色。 如果在没有参数的情况下使用，则 color 会还原默认的 "命令提示符" 窗口前景色和背景色。
color
#7 将一个或多个文件从一个位置复制到另一个位置。
copy

```

## D

```shell
#1 显示或设置系统日期。 如果在没有参数的情况下使用， date 将显示当前系统日期设置，并提示你输入新日期。
date
#2 删除一个或多个文件。
del
#3 显示目录的文件和子目录的列表。 如果在没有参数的情况下使用，则此命令将显示磁盘的卷标和序列号，后跟磁盘上的目录和文件的列表 (包含它们的名称和上次修改的日期和时间) 。 对于文件，此命令将显示名称扩展名和大小（以字节为单位）。 此命令还显示列出的文件和目录的总数、其累计大小和可用空间 (以字节为单位) 磁盘上剩余。
dir

```

## E

```shell
#1 显示目录的文件和子目录的列表。 如果在没有参数的情况下使用，则此命令将显示磁盘的卷标和序列号，后跟磁盘上的目录和文件的列表 (包含它们的名称和上次修改的日期和时间) 。 对于文件，此命令将显示名称扩展名和大小（以字节为单位）。 此命令还显示列出的文件和目录的总数、其累计大小和可用空间 (以字节为单位) 磁盘上剩余。
echo
#2 退出命令解释器或当前批处理脚本。
exit

```

## F

```shell
#1 比较两个文件或文件集，并显示它们之间的差异。
fc
#2 搜索文件中的文本字符串，并显示包含指定字符串的文本行。
find

```

## G

```shell
#1 将 cmd.exe 定向到批处理程序中带标签的行。 在批处理程序中，此命令将命令处理定向到由标签标识的行。 找到标签后，处理将从下一行开始的命令开始。
goto

```

## H

```shell
#1 显示有关指定命令的可用命令或详细帮助信息的列表。 如果在没有参数的情况下使用，则 " 帮助 " 列出并简要说明每个系统命令。
help

```

## I

```shell
#1 显示所有当前 TCP/IP 网络配置值并刷新动态主机配置协议 (DHCP) 和域名系统 (DNS) 设置。 在没有参数的情况下使用， ipconfig 显示 Internet 协议版本 4 (IPv4) 以及所有适配器的 IPv6 地址、子网掩码和默认网关。
ipconfig
```

## M

```shell
#1 创建目录或子目录。 默认情况下启用的命令扩展允许你使用单个 md 命令在指定路径中创建中间目录。
md
#2 一次显示输出的一个屏幕。
more
#3 一种命令行实用工具，它将网络文件系统 (NFS) 网络共享。 当不带选项或参数使用时， 装载 会显示有关所有已装载 NFS 文件系统的信息。
mount
#4 将一个或多个文件从一个目录移动到另一个目录。
move

```

## N

```shell
#1 显示处于活动状态的 TCP 连接、计算机正在侦听的端口、以太网统计信息、IP 路由表、用于 IP、ICMP、TCP 和 UDP 协议的 IPv4 统计信息 () 和 ipv6 统计信息 (ipv6、ICMPv6、TCP over IPv6 和 UDP over IPv6 协议) 。 使用没有参数的情况下，此命令显示活动 TCP 连接。
netstat
#2 网络 Shell 命令行脚本实用工具，可让你以本地或远程方式显示或修改当前正在运行的计算机的网络配置。
netsh
netsh wlan show profiles
netsh wlan show profile name=“连接名” key=clear #可查看密码
#3
net

nslookup
```

## P

```shell
#1 通过向另一台 TCP/IP 计算机发送 Internet 控制消息协议 (ICMP) 回响请求消息来验证 IP 级连接。
ping

```

## R

```shell
#1 记录脚本、批处理或 config.sys 文件中的注释。 如果未指定任何注释，则 rem 将增加垂直间距。
rem
#2 重命名文件或目录。
ren
#3 删除目录。
rd

```

## S

```shell
#1 显示、设置或删除 cmd.exe 环境变量。 如果不使用参数，则 set 将 显示当前环境变量设置。
set
#2 使你能够一次关闭或重新启动一台或多台本地或远程计算机。
shutdown
#3 启动单独的命令提示符窗口以运行指定的程序或命令。
# 可打开网页
start

```

## T

```shell
#1 结束一个或多个任务或进程。 可以通过进程 ID 或图像名称结束进程。 您可以使用 tasklist 命令 命令来确定进程 ID (PID) 以结束进程。
taskkill
taskkill /pid 1230 /pid 1231 /t
taskkill /im notepad.exe
taskkill /f /im cmd.exe /t
#2 显示本地计算机或远程计算机上当前正在运行的进程列表。 Tasklist 替换 tlist.exe 工具。
tasklist
tasklist # 查看计算机的进程
tasklist /svc
#3 显示或设置系统时间。 如果在没有参数的情况下使用， time 将显示当前系统时间，并提示您输入新时间。
time
#4 以图形方式显示驱动器路径或磁盘的目录结构。 此命令显示的结构取决于你在命令提示符处指定的参数。 如果未指定驱动器或路径，此命令将显示从当前驱动器的当前目录开始的树状结构。
tree
#8 在 Windows 命令行界面中， 键入 "内置命令"，其中显示文本文件的内容。 使用 type 命令查看文本文件，而不进行修改。
type

```



## W

```shell
#1 显示与给定的搜索模式匹配的文件的位置。
where
#2 显示当前登录到本地系统的用户的用户、组和特权信息。 如果在没有参数的情况下使用，则 whoami 将显示当前的域和用户名。
whoami
```

## X

```shell
#1 复制文件和目录，包括子目录。
xcopy

```

## #

```shell
#1 输出重定向
>
#2 追加
>>

```



# windows应用

```shell
eventvwr 事件查看器 # 6005/6006 开机/关机
control
msinfo32
sysdm.cpl 打开环境变量
explorer 打开资源管理器
notepad 打开记事本
calc 启动计算器
write 写字板
mspaint 画图板
gpedit.msc 本地组策略
Certmgr.msc	证书
```



# 常用命令

```bash
cd, dir, md, rd,      copy, xcopy, del, ren, more,      echo, find, help, set, tasklist, taskkill,      ipconfig, ping, net, netstat, nslookup
```

