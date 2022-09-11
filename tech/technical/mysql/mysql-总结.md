# admin

## mysql

```mysql
mysql --help
mysql -?
mysql --version
mysql -V
mysql -h[host] -uroot -p -P[port]

```



## mysqld

```mysql
mysqld --verbose --help
mysqld --version
mysqld -V

```

## mysqladmin

```mysql
mysqladmin --help
```

## mysqldump

```mysql
mysqldump -uroot -p database > database.sql
mysql -uroot -p database < database.sql

```



# mysql

```mysql
help
status;
use databases
show databases;
show tables;
desc table; 
/* 
describe table;
show columns from table;
*/
show status;
show create database;
show create table;
show grants;
show errors;
show warnings;
help show;
show variables like pattern
```

```mysql
3中注释方法
# select
-- select
/* 
select
*/

```

```mysql
# 函数
1 select version();
2 select database();


```



# information_schema

```mysql
# 事务表
innodb_trx
# 进程表
processlist

```





# Chapter 3 Tutorial

## 3.5在批处理模式下使用mysql



在前面的部分中，您以 交互方式使用[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)输入语句并查看结果。您也可以以批处理模式运行[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)。为此，将要运行的语句放在文件中，然后告诉 [**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)从文件中读取其输入：

```terminal
shell> mysql < batch-file
```

如果您在Windows下运行[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)并在文件中包含一些导致问题的特殊字符，则可以执行以下操作：

```terminal
C:\> mysql -e "source batch-file"
```

如果需要在命令行上指定连接参数，则命令可能如下所示：

```terminal
shell> mysql -h host -u user -p < batch-file
Enter password: ********
```

当您以这种方式使用[**mysql时**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)，您将创建一个脚本文件，然后执行该脚本。

如果您希望脚本继续运行，即使其中的某些语句产生错误，也应使用 [`--force`](https://dev.mysql.com/doc/refman/8.0/en/mysql-command-options.html#option_mysql_force)命令行选项。

为什么要使用脚本？原因如下：

- 如果您反复（例如每天或每周）运行查询，将其设置为脚本可以避免每次执行时都重新键入查询。

- 您可以通过复制和编辑脚本文件从相似的现有查询中生成新查询。

- 在开发查询时，批处理模式也很有用，特别是对于多行语句或多语句序列。如果输入有误，则无需重新输入所有内容。只需编辑脚本以更正错误，然后告诉[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)重新执行即可。

- 如果您的查询产生大量输出，则可以通过寻呼机运行输出，而不用看着它滚动到屏幕顶部之外：

  ```terminal
  shell> mysql < batch-file | more
  ```

- 您可以将输出捕获到文件中以进行进一步处理：

  ```terminal
  shell> mysql < batch-file > mysql.out
  ```

- 您可以将脚本分发给其他人，以便他们也可以运行这些语句。

- 在某些情况下，例如，当您从**cron**作业运行查询时，不允许进行交互使用。在这种情况下，您必须使用批处理模式。

在批处理模式下 运行[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)时，与以交互方式使用时，默认输出格式不同（更简洁） 。例如，以交互方式运行[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)`SELECT DISTINCT species FROM pet`时，输出如下所示 ：

```none
+---------+
| species |
+---------+
| bird    |
| cat     |
| dog     |
| hamster |
| snake   |
+---------+
```

在批处理模式下，输出看起来像这样：

```none
species
bird
cat
dog
hamster
snake
```

如果要以批处理方式获取交互式输出格式，请使用[**mysql -t**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)。要将执行的语句回显到输出，请使用[**mysql -v**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)。



您还可以通过使用以下命令， 从[**mysql**](https://dev.mysql.com/doc/refman/8.0/en/mysql.html)提示符中使用脚本： `source``\.`

```sql
mysql> source filename;
mysql> \. filename
```

有关更多信息[，](https://dev.mysql.com/doc/refman/8.0/en/mysql-batch-commands.html)请参见[第4.5.1.5节“从文本文件执行SQL语句”](https://dev.mysql.com/doc/refman/8.0/en/mysql-batch-commands.html)。