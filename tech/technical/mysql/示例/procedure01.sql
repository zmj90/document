
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