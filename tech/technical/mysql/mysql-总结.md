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



# 经验



## 特殊用法

```mysql
select 'CA20181110683' % 4;
select null % 4;
select now();
select '2' + 1;
select substr('FA2019071001-2022-02', 4, 9);

select 
project_no, @n:=@n+1 
-- *
from sync_project_info, (select @n:=0) a;

# 联表更新
update tech_develop_basic dev inner join tech_develop_technical_achievements am on dev.pro_code = am.project_id
set am.project_id = dev.id;
```



## sql注入

```mysql
# sql注入
(select*from(select+sleep(5)union/**/select+1)a);
select*from(select+sleep(5)union/**/select+1)a;
select+sleep(5) union 1;
(select+concat("q",sleep(3)));
```



## 流程控制

```mysql
select * from cooperation_projects_clean 
where 
project_code = case substr(project_code, 4, 9) % 4
when 0 then project_code
end;

# 更新指定行的数据；优化方案：在set的时候就判断
update cooperation_projects_clean
set project_manager = '钟马俊', project_manager_id = 'zwx996578', partner_manager = '钟马俊', partner_manager_id = 'zwx996578'
where
project_code = case substr(project_code, 4, 9) % 4
when 3 then project_code
end;
```



```mysql
select * 
from coop_resource_tech_domain_config 
where 
case `level` regexp '~'
when 0 then `level` = 'L1'
when 1 then 'L1' between left(`level`, 2) and right(`level`, 2)
end 
order by `level`;

select * 
from coop_resource_tech_domain_config 
where 'L1' between left(`level`, 2) and right(`level`, 2)
order by `level`;
```





## 事件

```mysql
# 事件
SHOW VARIABLES LIKE 'event_scheduler';
SET GLOBAL event_scheduler = ON;

begin
	update sync_project_info
	set prj_manager = 'gaojuanjuan WX1209019'
	where 
	project_no = case project_no % 4
	when 0 then project_no
	end;

	update sync_project_info
	set prj_manager = 'liaoxiaobo WX1208242'
	where 
	project_no = case project_no % 4
	when 1 then project_no
	end;

	update sync_project_info
	set prj_manager = 'taoxingyu WX1123125'
	where 
	project_no = case project_no % 4
	when 2 then project_no
	end;

	update sync_project_info
	set prj_manager = 'zhongmajun WX996578'
	where 
	project_no = case project_no % 4
	when 3 then project_no
	when null then project_no
	end;
	
	update clear_project_info
	set prj_manager = 'gaojuanjuan WX1209019', prj_manager_cn = '高娟娟 WX1209019'
	where 
	project_no = case project_no % 4
	when 0 then project_no
	end;

	update clear_project_info
	set prj_manager = 'liaoxiaobo WX1208242', prj_manager_cn = '廖小波 WX1208242'
	where 
	project_no = case project_no % 4
	when 1 then project_no
	end;

	update clear_project_info
	set prj_manager = 'taoxingyu WX1123125', prj_manager_cn = '陶星宇 WX1123125'
	where 
	project_no = case project_no % 4
	when 2 then project_no
	end;

	update clear_project_info
	set prj_manager = 'zhongmajun WX996578', prj_manager_cn = '钟马俊 WX996578'
	where 
	project_no = case project_no % 4
	when 3 then project_no
	when null then project_no
	end;
end


```



## 存储过程

```mysql

create procedure permission(in uid1 varchar(50), in uid2 varchar(50), in uid3 varchar(50), in uid4 varchar(50), in line varchar(10))
begin

-- 超管
declare a int;
-- 技术项目规划-管理员
declare b1 int;
declare b2 int;
-- 技术合作项目-管理员
declare c1 int;
declare c2 int;
-- 技术开发项目-管理员
declare d1 int;
declare d2 int;
-- 根技术
declare e1 int;
declare e2 int;
-- 个人中心
declare f1 int;
declare f2 int;

-- 超管
select id into a from person_role_relation where role_id = 10 and huawei_id regexp uid1 and project_id = 'all' and module = 'idea' and product_line = line;
if a then 
	update person_role_relation set huawei_id = uid2, product_line = line where id = a;
else 
	insert into person_role_relation(role_id, huawei_id, project_id, module, product_line) values (10, uid2, 'all', 'idea', line);
end if;

-- 技术项目规划-管理员
select id into b1 from personnel_config where huawei_id regexp uid1 and project_id = 'pre_tpp_1000000001' and module = 'technology_project_planing' and product_line = line;
if b1 then 
	update personnel_config set huawei_id = uid2, product_line = line where id = b1;
else 
	insert into personnel_config(huawei_id, project_id, module, product_line, is_hand, account, cn, department_tree, source, is_show) values 
	(uid2, 'pre_tpp_1000000001', 'technology_project_planing', line, 1, uid3, uid4, '计算可信使能与IT装备部', '手工录入', 0);
end if;
select id into b2 from person_role_relation where role_id = 94 and huawei_id regexp uid1 and project_id = 'pre_tpp_1000000001' and module = 'technology_project_planing' and product_line = line;
if b2 then 
	update person_role_relation set huawei_id = uid2, product_line = line where id = b2;
else 
	insert into person_role_relation(role_id, huawei_id, project_id, module, product_line) values (94, uid2, 'pre_tpp_1000000001', 'technology_project_planing', line);
end if;

-- 技术合作项目-管理员
select id into c1 from personnel_config where huawei_id regexp uid1 and project_id = 'pre_tcp_1000000003' and module = 'technology_cooperation_project' and product_line = line;
if c1 then 
	update personnel_config set huawei_id = uid2, product_line = line where id = c1;
else 
	insert into personnel_config(huawei_id, project_id, module, product_line, is_hand, account, cn, department_tree, source, is_show) values 
	(uid2, 'pre_tcp_1000000003', 'technology_cooperation_project', line, 1, uid3, uid4, '计算可信使能与IT装备部', '手工录入', 0);
end if;
select id into c2 from person_role_relation where role_id = 61 and huawei_id regexp uid1 and project_id = 'pre_tcp_1000000003' and module = 'technology_cooperation_project' and product_line = line;
if c2 then 
	update person_role_relation set huawei_id = uid2, product_line = line where id = c2;
else 
	insert into person_role_relation(role_id, huawei_id, project_id, module, product_line) values (61, uid2, 'pre_tcp_1000000003', 'technology_cooperation_project', line);
end if;

-- 技术开发项目-管理员
select id into d1 from personnel_config where huawei_id regexp uid1 and project_id = '1000000010' and module = 'tech_project_module' and product_line = line;
if d1 then 
	update personnel_config set huawei_id = uid2, product_line = line where id = d1;
else 
	insert into personnel_config(huawei_id, project_id, module, product_line, is_hand, account, cn, department_tree, source, is_show) values 
	(uid2, '1000000010', 'tech_project_module', line, 1, uid3, uid4, '计算可信使能与IT装备部', '手工录入', 0);
end if;
select id into d2 from person_role_relation where role_id = 95 and huawei_id regexp uid1 and project_id = '1000000010' and module = 'tech_project_module' and product_line = line;
if d2 then 
	update person_role_relation set huawei_id = uid2, product_line = line where id = d2;
else 
	insert into person_role_relation(role_id, huawei_id, project_id, module, product_line) values (95, uid2, '1000000010', 'tech_project_module', line);
end if;

-- 根技术-管理员
select id into e1 from personnel_config where huawei_id regexp uid1 and project_id = '1000000021' and module = 'root_tech' and product_line = line;
if e1 then 
	update personnel_config set huawei_id = uid2, product_line = line where id = e1;
else 
	insert into personnel_config(huawei_id, project_id, module, product_line, is_hand, account, cn, department_tree, source, is_show) values 
	(uid2, '1000000021', 'root_tech', line, 1, uid3, uid4, '计算可信使能与IT装备部', '手工录入', 0);
end if;
select id into e2 from person_role_relation where role_id = 2101 and huawei_id regexp uid1 and project_id = '1000000021' and module = 'root_tech' and product_line = line;
if e2 then 
	update person_role_relation set huawei_id = uid2, product_line = line where id = e2;
else 
	insert into person_role_relation(role_id, huawei_id, project_id, module, product_line) values (2101, uid2, '1000000021', 'root_tech', line);
end if;

-- 个人中心-领导
select id into f1 from personnel_config where huawei_id regexp uid1 and project_id = '1000000061' and module = 'innovation_personal_center' and product_line = line;
if f1 then 
	update personnel_config set huawei_id = uid2, product_line = line where id = f1;
else 
	insert into personnel_config(huawei_id, project_id, module, product_line, is_hand, account, cn, department_tree, source, is_show) values 
	(uid2, '1000000061', 'innovation_personal_center', line, 1, uid3, uid4, '计算可信使能与IT装备部', '手工录入', 0);
end if;
select id into f2 from person_role_relation where role_id = 2101 and huawei_id regexp uid1 and project_id = '1000000061' and module = 'innovation_personal_center' and product_line = line;
if f2 then 
	update person_role_relation set huawei_id = uid2, product_line = line where id = f2;
else 
	insert into person_role_relation(role_id, huawei_id, project_id, module, product_line) values (2101, uid2, '1000000061', 'innovation_personal_center', line);
end if;

-- 示例
-- call permission('wx996578', 'zhongmajun wx996578', 'zwx996578', '钟马俊 wx996578', '045969');
end
```



