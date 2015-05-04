// JavaScript Document
function sy_nv(url,params,values,ach)
{
	var str = url;
	if(params != "" && params.length > 0)
	{
		for(var i = 0; i < params.length; i++)
		{
			if(i == 0)
				str += "?" + params[i] + "=" + values[i];
			else
				str += "&" + params[i] + "=" + values[i];
		}
	}
	if(ach != "")
		str += ach;
	location.href= str;
}

function sy_new(url,params,values,ach)
{
	var str = url;
	if(params != "" && params.length > 0)
	{
		for(var i = 0; i < params.length; i++)
		{
			if(i == 0)
				str += "?" + params[i] + "=" + values[i];
			else
				str += "&" + params[i] + "=" + values[i];
		}
	}
	if(ach != "")
		str += ach;
	window.open(str,"_blank","'height=650, width=800, top=10, left=10, toolbar=no, menubar=no, scrollbars=yes, resizable=no,location=no, status=no'");
}

function sy_open(url,params,values,ach)
{
	var str = url;
	if(params != "" && params.length > 0)
	{
		for(var i = 0; i < params.length; i++)
		{
			if(i == 0)
				str += "?" + params[i] + "=" + values[i];
			else
				str += "&" + params[i] + "=" + values[i];
		}
	}
	if(ach != "")
		str += ach;
	window.open(str,"_blank","'height=650, width=800, top=10, left=10, toolbar=yes, menubar=yes, scrollbars=yes, resizable=yes,location=yes, status=yes'");
}

function sy_validate(fName,fType,fNeed,fVal)
{
    var patrn;
	if(fNeed == "1" && fVal == "")
	{
		alert(fName + "字段必填");
		event.returnValue = false;
		return;
	}
	if(fType == "int")
	{
		patrn = /^[0-9]{1,20}$/;
		if(!sy_check(patrn,fVal))
	    {
	        alert(fName + ":必须是数字!");
		    event.returnValue = false;
		    return;
	    }
	}
	if(fType == "datetime")
	{
		patrn = /^((((1[6-9]|[2-9]d)d{2})-(0?[13578]|1[02])-(0?[1-9]|[12]d|3[01]))|(((1[6-9]|[2-9]d)d{2})-(0?[13456789]|1[012])-(0?[1-9]|[12]d|30))|(((1[6-9]|[2-9]d)d{2})-0?2-(0?[1-9]|1d|2[0-8]))|(((1[6-9]|[2-9]d)(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))-0?2-29-))$/;
		if(!sy_check(patrn,fVal))
	    {
	        alert(fName + ":必须是日期格式(yyyy-mm-dd)!");
		    event.returnValue = false;
		    return;
	    }
	}
}

function sy_check(patrn,str)
{
    if (!patrn.exec(str)) 
        return false  
    return true  
}

function setMenu2See(menu)
{
	var obj,parent,num,obj_menu,objlist,spans;
	obj_menu = document.getElementById(menu);
	//所有的菜单
	master = document.getElementById("menu");
	objlist = master.getElementsByTagName("span");
	num = objlist.length;
	for (var i=0; i < num; i++)
	{
		objlist[i].style.color = '#FFFFFF';
		objlist[i].style.backgroundColor = '#969696';
	}
	
	obj_menu.style.color = '#000066';
	obj_menu.style.backgroundColor = '#EEEEEE';
	
	parent = document.getElementById("menu2");
	parent.style.display="block";
	//获得所有的子菜单
	spans = parent.getElementsByTagName("span");
	num = spans.length;
	for (var i=0; i < num; i++)
	{
		spans[i].style.display = 'none';
	}
	obj = document.getElementById(menu + "_sub");
	if(obj)
		obj.style.display="block";
}

function setSearchValue(obj)
{
	if(obj.value == "搜索" || obj.value == "Search" || obj.value=="Ingresa su búsqueda" || obj.value=="Поиск")
		obj.value = "";
}
function setLinkShow()
{
	var obj = document.getElementById("sublink");
	if(obj.style.display == 'none' || obj.style.display == '')
		obj.style.display = 'block';
	else 
		obj.style.display = 'none';
}
function InitAjax()
{
　var ajax=false; 
　try { 
　　ajax = new ActiveXObject("Msxml2.XMLHTTP"); 
　} catch (e) { 
　　try { 
　　　ajax = new ActiveXObject("Microsoft.XMLHTTP"); 
　　} catch (E) { 
　　　ajax = false; 
　　} 
　}
　if (!ajax && typeof XMLHttpRequest!='undefined') { 
　　ajax = new XMLHttpRequest(); 
　} 
　return ajax;
}

function toEn(objId)
{
	
	var obj = document.getElementById(objId);
	if(obj.value == "us")
		location.href = '/en';
	if(obj.value == "zh")
		location.href = '/cn';
	if(obj.value == "es")
		location.href = '/es';
	if(obj.value == "ru")
		location.href = '/ru';
	//alert('英文网站还没有开通');
}

function sy_new2(url,params,values,ach)
{
	var str = url;
	if(params != "" && params.length > 0)
	{
		for(var i = 0; i < params.length; i++)
		{
			if(i == 0)
				str += "?" + params[i] + "=" + values[i];
			else
				str += "&" + params[i] + "=" + values[i];
		}
	}
	if(ach != "")
		str += ach;
	window.open(str,"_blank");
}

