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