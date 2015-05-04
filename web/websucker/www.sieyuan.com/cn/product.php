<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" ><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" ><!-- InstanceBegin template="/Templates/t4.dwt.php" codeOutsideHTMLIsLocked="false" -->
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<meta name="keywords" content="思源电气" />
<meta name="description" content = "思源电气股份有限公司是上海市重点高新技术企业，是国内知名的专业电力设备制造商，也是一家知名的上市企业。" />
<meta name="copyright" content="思源电气股份有限公司" />
<title></title>
<script language=javascript src="../js/emethod.js"></script>
<script language=javascript src="../js/jquery-1.5.2.min.js"></script>
<script type="text/javascript" src="../js/jquery.json-2.3.min.js"></script>
<script language="JavaScript" type="text/javascript">
<!--
		
		function setAppraise()
		{
			var obj = document.getElementById("DivAppraise");
			if(obj.style.display == "none")
				obj.style.display = "block";
			else
				obj.style.display = "none";
		}
		/*
		function setMessage()
		{
			var obj = document.getElementById("DivMessage");
			if(obj.style.display == "none")
				obj.style.display = "block";
			else
				obj.style.display = "none";
		}*/
		
		function setRateThisPageValue(obj,val)
		{
			var temp = obj.id.substring(0,obj.id.length - 1);
			for(var i = 1; i <6; i++)
			{
				var objt = document.getElementById(temp + i);
				objt.style.color = "#000000";
			}
			for(var i = 1; i <=val; i++)
			{
				var objt = document.getElementById(temp + i);
				objt.style.color = "#FF0000";
			}
			var hrate = document.getElementById("hrate");
			hrate.value = val;
		}
		
		function doComments(hrate,comment)
		{
			var url = "../cn/submitco.php";
			
			var host = window.location.host;
			var param = "lc=" + location + "&hr=" + hrate + "&co=" + comment;
			var ajax = InitAjax();
			ajax.open("POST", url, true);
			ajax.setrequestheader("content-length",param.length);//post提交设置项
			ajax.setrequestheader("content-type","application/x-www-form-urlencoded");//post提交设置项
			ajax.onreadystatechange = function() { 
				if (ajax.readyState == 4 && ajax.status == 200) { 
					alert(ajax.responseText);
					setAppraise();
				}
　　			}
			ajax.send(param);
			ajax.send(null); 
		}
		/*
		function doMessage(name,email,title,message,type)
		{
			if(name == "")
			{
				alert("请输入您的称呼!");
				return false;
			}
			
			if(email == "")
			{
				alert("请输入您的Email!");
				return false;
			}
			else
			{
				var reg = "/\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)";
				var result =  reg.exec(email);
				if(!result)
				{
					alert("请输入正确的Email格式!");
					return false;
				}
			}
			
			if(title == "")
			{
				alert("请输入您的标题!");
				return false;
			}
			
			if(message == "")
			{
				alert("请输入您的留言!");
				return false;
			}
			
			var url = "../cn/submitqa.php";
			
			var param = "name=" + name + "&mail=" + email + "&subject=" + title + "&body=" + message + "&type=" + type;
			var ajax = InitAjax();
			ajax.open("POST", url, true);
			ajax.setrequestheader("content-length",param.length);//post提交设置项
			ajax.setrequestheader("content-type","application/x-www-form-urlencoded");//post提交设置项
			ajax.onreadystatechange = function() { 
				if (ajax.readyState == 4 && ajax.status == 200) { 
					alert(ajax.responseText);
					setMessage();
				}
　　			}
			ajax.send(param);
			ajax.send(null); 
		}*/
		
		function setONMouseOver(obj)
		{
			obj.style.color= "#FFFFFF";
			obj.style.backgroundColor = "#000000";
		}
		
		function setONMouseOut(obj)
		{
			obj.style.color= "#000000";
			obj.style.backgroundColor = "#EEEEEE";
		}
		
		function oneHeight(arguments)
		{
			var maxHeight=0;
		   	var a=[];
		   	for(var i=0,n=arguments.length;i<n;i++){
			 a[i]=document.getElementById(arguments[i]);
			 if(a[i].scrollHeight>maxHeight)
			   maxHeight=a[i].scrollHeight;
		   	}
		   	for(i=0;i<n;i++)
			 a[i].style.height=maxHeight+'px';
		}
//-->
</script>
<link rel="stylesheet" href="../css/style.css" type="text/css" />
<!-- InstanceParam name="OptionalRegion1" type="boolean" value="true" --><!-- InstanceParam name="OptionalRegion2" type="boolean" value="true" --><!-- InstanceParam name="OptionalRegion3" type="boolean" value="true" -->
</head>
<body  onload="oneHeight(['mcontent4','rcontent3'])">
<!--Begin container-->
<div id="container" >
	<div id="tbanner">&nbsp;</div>
	<div id="banner" ><span style="padding-right:85px;"><img src="../images/background/logo.jpg" name="logo" width="200px" height="70" id="logo" /></span>
        <!--网站地图及字体大小开始-->
        <div class="mapdiv">
				<!--<table>
					<tr>
						<td><a href="../cn/webmap.php">网站地图</a></td>
					</tr>
				</table> -->
      	</div>
		<!--网站地图及字体大小结束-->
	    <span>
						<span><img src="../images/button/home.gif" width="80" height="28" style="cursor:pointer;" onclick="sy_nv('../cn/index.php','','','')"/></span>
						<span><img src="../images/button/aboutus.gif" width="80" height="28" style="cursor:pointer;" onclick="sy_nv('../cn/aboutus.php','','','')"/></span>
						<span><img src="../images/button/news.gif" width="80" height="28" style="cursor:pointer;" onclick="sy_nv('../cn/news.php','','','')"/></span>
						<span><img src="../images/button/product.gif" width="80" height="28" style="cursor:pointer;" onclick="sy_nv('../cn/product.php','','','')"/></span>
						<span><img src="../images/button/investor.gif" width="80" height="28" style="cursor:pointer;" onclick="sy_nv('../cn/listing.php','','','')"/></span>
						<span><img src="../images/button/employ.gif" width="80" height="28" style="cursor:pointer;" onclick="sy_nv('../cn/hr.php','','','')"/></span>
					</span>
        <!--菜单结束-->
  </div>

	<!--Flash开始-->
	<div class="flashbar">
     <!-- InstanceBeginEditable name="banner" -->
	  <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="990" height="200">
              <param name="movie" value="../images/flash/product.swf" />
              <param name="quality" value="high" />
              <embed src="../images/flash/product.swf" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="990" height="200"></embed>
	    </object>
	 <!-- InstanceEndEditable -->	</div> 
 <!--Flash结束-->
<!--新闻、产品和快速导航开始-->
<div class="midlines"></div>
<div>
	<div id="mcontent4" class="mcontent4">
	  <!-- InstanceBeginEditable name="mcontent" -->
	   <div class="pdchead">
	  		产品指南
	  </div>
	  <div class="pclass">
			<script type="text/javascript">
			<!--
					function pdsearch()
					{
						var clsid,psid;
						var pclass = document.getElementById("pclass");
						var psclass = document.getElementById("psclass");
						var url = '';

						if(null != pclass)
						{
							clsid = pclass.value;
						}
						if(null != psclass)
						{
							psid = psclass.value;
						}
						
						if(null != clsid && clsid != 0)
						{
							url += '../cn/plist.php?fid=' + clsid;
						}

						if(null != psid && psid != 0)
						{
							url += '&fsubclass=' + psid;
						}
						
						if(url != "")
						{
							location.href = url;
						}
						return false;
					}

					function loadData()
					{
						var fid = $('#pclass').find("option:selected").val();
						var dataParam = "fId=" + fid;
						var ary;
						$.ajax({
							type: 'GET',
							url: '../cn/subclass.php',
							data: dataParam,
							dataType: 'html',
							success: function(html){
								ary = $.evalJSON(html);
								$('#psclass').children().remove();
								$('#psclass').append('<option value="0">选择电压等级</option>');
								for(i = 0; i < ary.length; i++)
								{
									$('#psclass').append('<option value="' + ary[i]["fId"] + '">' + ary[i]["fName"] + '</option>');
								}
							}
						})
					}
			//-->
			</script>
			<span>产品类别</span>
				<select id="pclass" name="pclass" onchange="loadData()">
					<option value="0">选择产品类别</option><option value="1">气体绝缘组合电器</option><option value="2">中高压断路器</option><option value="3">中高压隔离开关</option><option value="5">电力电容器</option><option value="6">电能质量设备</option><option value="7">电力电抗器</option><option value="9">电力自动化设备</option><option value="10">在线监测设备</option><option value="4">互感器及套管</option><option value="11">电力测试设备</option><option value="12">变电站自动化系统</option>				</select>
			<span>电压等级</span>
				<select id="psclass" name="psclass">
					<option value="0">选择电压等级</option>
									</select>
			&nbsp;<input type="button" id="butSreach" name="butSreach" class="goButton" value="OK" onclick="pdsearch()">
	  </div>
	  <div class="pdcbody">
						  			<div style="float:left; width:350; padding-right:15px;">	
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=1">气体绝缘组合电器</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=25">ZFW28-72.5/126/145型SF6气体绝缘组合电器</a></li><li><a href="../cn/pdetail.php?fid=162">ZF28-252型SF6气体绝缘组合电器</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=2">中高压断路器</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=41">LW36/72.5kV自能式高压交流六氟化硫断路器</a></li><li><a href="../cn/pdetail.php?fid=42">ZW39型高压真空断路器</a></li><li><a href="../cn/pdetail.php?fid=44">LW36-126(W)/T3150-40交流高压六氟化硫断路器</a></li><li><a href="../cn/pdetail.php?fid=45">LW36-40.5(W)/T2500-31.5自能式高压六氟化硫断路器</a></li><li><a href="../cn/pdetail.php?fid=47">ZW39-40.5(W)/T2000-31.5交流高压真空断路器</a></li><li><a href="../cn/pdetail.php?fid=134">LW58-252/T4000-50 高压六氟化硫断路器</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=3">中高压隔离开关</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=48">GW22-126D(W)型高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=49">GW5A/5D系列户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=50">JW10-252（G）252kV户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=133">JW10-550D(W),JW10-363D(G-W) 型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=51">GW23B系列户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=52">GW22B系列户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=53">GW7B-252D(G)252kV户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=54">GW4C-252D(G)252kV户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=55">GW4-126(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=56">GW23-126/252(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=57">GW4-40.5(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=58">GW4A-126(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=59">GW4A-40.5(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=60">GW5-40.5/126(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=61">GW5A-40.5/126(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=62">GW7-252(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=63">GW8系列户外高压交流中性点隔离开关</a></li><li><a href="../cn/pdetail.php?fid=64">JW2系列户外高压交流接地开关</a></li><li><a href="../cn/pdetail.php?fid=65">GW22-126/252(D)(W)型户外高压交流隔离开关</a></li><li><a href="../cn/pdetail.php?fid=66">GW13系列户外高压交流中性点隔离开关</a></li><li><a href="../cn/pdetail.php?fid=67">GW4-27.5(D)(W)型户外高压交流隔离开关</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=5">电力电容器</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=68">并联电容器</a></li><li><a href="../cn/pdetail.php?fid=69">滤波电容器</a></li><li><a href="../cn/pdetail.php?fid=70">串联电容器</a></li><li><a href="../cn/pdetail.php?fid=72">集合式并联电容器</a></li><li><a href="../cn/pdetail.php?fid=73">串联补偿装置用串联电容器组</a></li><li><a href="../cn/pdetail.php?fid=74">高压并联电容器装置</a></li><li><a href="../cn/pdetail.php?fid=131">滤波电容器成套装置</a></li><li><a href="../cn/pdetail.php?fid=132">集合式并联电容器成套装置</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=6">电能质量设备</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=36">高压静止无功发生器(SVG)</a></li><li><a href="../cn/pdetail.php?fid=121">低压静止无功发生器(SVG)</a></li><li><a href="../cn/pdetail.php?fid=39">低压有源电力滤波装置(APF)</a></li><li><a href="../cn/pdetail.php?fid=38">高压变频调速装置</a></li><li><a href="../cn/pdetail.php?fid=40">动态电压调节装置－DVR(QNDVR100)</a></li><li><a href="../cn/pdetail.php?fid=37">磁控电抗器(MCR)型-SVC</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=7">电力电抗器</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=29">BKS--系列油浸式铁心并联电抗器</a></li><li><a href="../cn/pdetail.php?fid=30">BKSC--系列环氧浇注铁心并联电抗器</a></li><li><a href="../cn/pdetail.php?fid=31">CKSC--系列环氧浇注铁心串联电抗器</a></li>						</ul>
									</div>
				<div style="float:left; width:350;padding-right:15px;">
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=9">电力自动化设备</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=26">消弧线圈自动调谐及接地选线成套装置</a></li><li><a href="../cn/pdetail.php?fid=27">微机小电流接地选线成套设备</a></li><li><a href="../cn/pdetail.php?fid=28">中性点接地电阻</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=10">在线监测设备</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=157">SEM5000变电站状态(在线)监测系统</a></li><li><a href="../cn/pdetail.php?fid=158">SEM-T主变状态监测系统</a></li><li><a href="../cn/pdetail.php?fid=33">TROM-600变压器油色谱在线监测系统</a></li><li><a href="../cn/pdetail.php?fid=34">JC1MOA在线监测仪</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=4">互感器及套管</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=85">TYD220-220kV电容式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=86">TYD110-110kV电容式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=95">LVQB(T)-500W2(W3)-500kVSF6气体绝缘倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=96">LVQB(T)-330W2(W3)-330kVSF6气体绝缘倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=97">LVQB(T)-220W2(W3)-220kVSF6气体绝缘倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=98">LVQB-110W3-110kVSF6气体绝缘倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=100">LVB(T)-500W2(W3)500kV油浸倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=101">LVB(T)-330W2(W3)330kV油浸倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=102">LVB(T)-220W2(W3)220kV油浸倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=103">LVB-110W2(W3)110kV油浸倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=104">LVB-66W2(W3)66kV油浸倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=105">LVB(T)-35W2(W3)35kV油浸倒立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=107">LB型油浸正立式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=89">JED(S)H系列配GIS用SF6气体绝缘电子式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=129">LEDH系列配GIS用SF6气体绝缘电子式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=130">JLED(S)H系列配GIS用SF6气体绝缘电子式组合互感器</a></li><li><a href="../cn/pdetail.php?fid=127">JD(S)QXFH系列配GIS用SF6气体绝缘电磁式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=128">JD(S)QXFH系列配GIS用SF6气体绝缘带隔离装置电磁式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=125">JDQXFH-220-220kV配GIS用SF6气体绝缘小型化电磁式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=126">JDQXFH-500-500kV配GIS用SF6气体绝缘电磁式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=90">JDQXF-110W3-110kVSF6气体绝缘独立式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=123">JDQXF-220W3-220kVSF6气体绝缘独立式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=122">BRLDW-126/630-4-126kV油纸绝缘电容式变压器套管</a></li><li><a href="../cn/pdetail.php?fid=124">BRLDW-252/1250-4-252kV油纸绝缘电容式变压器套管</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=11">电力测试设备</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=75">GZF-I型GIS工频耐压及局放测试系统</a></li><li><a href="../cn/pdetail.php?fid=76">变压器感应耐压及局放测试系统</a></li><li><a href="../cn/pdetail.php?fid=77">便携式高电压变频谐振耐压试验装置</a></li><li><a href="../cn/pdetail.php?fid=78">便携式6kV-110kV电缆耐压试验装置</a></li><li><a href="../cn/pdetail.php?fid=79">110kV-500kV长距离交联电缆（海底电缆）耐压试验系统</a></li><li><a href="../cn/pdetail.php?fid=80">220kV～1200kV GIS特高压设备耐压试验系统</a></li>						</ul>
											<div class="pdcbodyh">
							<a href="../cn/plist.php?fid=12">变电站自动化系统</a>						</div>
						<ul class="myul">
						<li><a href="../cn/pdetail.php?fid=118">SHR5000变电站自动化系统</a></li><li><a href="../cn/pdetail.php?fid=140">LDTVB电子式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=119">110kV解决方案</a></li><li><a href="../cn/pdetail.php?fid=120">220kV解决方案</a></li><li><a href="../cn/pdetail.php?fid=135">SUPER 5000变电站监控及高级应用系统</a></li><li><a href="../cn/pdetail.php?fid=136">UDD-501远动通信装置</a></li><li><a href="../cn/pdetail.php?fid=137">UDD-501远动通信装置</a></li><li><a href="../cn/pdetail.php?fid=138">UDN-501通信规约转换装置</a></li><li><a href="../cn/pdetail.php?fid=139">JDFD系列电子式电压互感器</a></li><li><a href="../cn/pdetail.php?fid=141">LDTVB电子式电流互感器</a></li><li><a href="../cn/pdetail.php?fid=142">UDM-501智能组件</a></li><li><a href="../cn/pdetail.php?fid=143">UDM-502合并单元</a></li><li><a href="../cn/pdetail.php?fid=144">UDA-501变电站自动控制装置</a></li><li><a href="../cn/pdetail.php?fid=145">UDL-551线路保护测控装置</a></li><li><a href="../cn/pdetail.php?fid=146">UDL-551线路保护测控装置</a></li><li><a href="../cn/pdetail.php?fid=147">UDC-501综合测控装置</a></li><li><a href="../cn/pdetail.php?fid=148">UDT-531变压器保护装置</a></li><li><a href="../cn/pdetail.php?fid=149">UDL-531线路保护测控装置</a></li><li><a href="../cn/pdetail.php?fid=151">UDQ-551电容器保护测控装置</a></li><li><a href="../cn/pdetail.php?fid=152">EASY50配置工具</a></li><li><a href="../cn/pdetail.php?fid=153">UDR-501网络报文记录分析装置</a></li><li><a href="../cn/pdetail.php?fid=154">UDR-502故障录波装置</a></li><li><a href="../cn/pdetail.php?fid=155">UDR-503网络记录和故障录波装置</a></li><li><a href="../cn/pdetail.php?fid=156">UDR-508 IEC 61850规约分析仪</a></li>						</ul>
									</div>
	  </div>
	  <!-- InstanceEndEditable --></div>
  <div id="rcontent3" class="rcontent3">
		<div class="searchspan">
			 <input name="searchInput" id="searchInput" class="searchFor" type="text" size="10" value="搜索" onclick="setSearchValue(this)" onkeypress="if(event.keyCode == 13) location.href ='../cn/search.php?searchField=' + this.value"/>
			  <input name="goButton" class="goButton" type="button" value="OK" onclick="location.href ='../cn/search.php?searchField=' + searchInput.value"/>
		</div>
	
		<div>
			<ul class="myul">
				<li><a href="contact.php">联系我们</a></li>
			</ul>
		</div>
		
		<!-- InstanceBeginEditable name="EditRegion4" -->
		<div class="formMessage">
			<ul style="margin:0;padding:0;height:25px;"><li><a href="../cn/pmsg.php"><span style="font-size:13px">产品留言</span></a></li></ul>
		</div>
		<!-- InstanceEndEditable -->
		<div class="formAppraise">
			<ul style="margin:0;padding:0;height:25px;"><li onclick="setAppraise()"><a><span>评价这个网页</span></a></li></ul>
			<div id="DivAppraise" style="display:none;">
				 <!--<ul style="margin:0;padding:0;height:20px;">
					选择评定等级
					<li id="ratePage1" onclick="setRateThisPageValue(this, 1)">☆</li>
					<li id="ratePage2" onclick="setRateThisPageValue(this, 2)">☆</li>
					<li id="ratePage3" onclick="setRateThisPageValue(this, 3)">☆</li>
					<li id="ratePage4" onclick="setRateThisPageValue(this, 4)">☆</li>
					<li id="ratePage5" onclick="setRateThisPageValue(this, 5)">☆</li>
				 </ul> -->
				<span style="padding-left:15px;">选择评定等级:</span>
				 <span id="ratePage1" class="ratePage" onclick="setRateThisPageValue(this, 1)">☆</span>
				 <span id="ratePage2" class="ratePage" onclick="setRateThisPageValue(this, 2)">☆</span>
				 <span id="ratePage3" class="ratePage" onclick="setRateThisPageValue(this, 3)">☆</span>
				 <span id="ratePage4" class="ratePage" onclick="setRateThisPageValue(this, 4)">☆</span>
				 <span id="ratePage5" class="ratePage" onclick="setRateThisPageValue(this, 5)">☆</span>
				 <input type="hidden" id="hrate" name="hrate" value="" />
				 <div style="padding-left:15px;">
				 	<span>您的意见：</span>
				 </div>
				 <div style="padding-left:15px;">
				 		<textarea id="comment" cols="" rows="6"></textarea>
				 </div>
				 <div style="padding-left:90px; padding-top:10px;">
				 		<input name="search" type="button" value="OK"
							class="goButton" onclick="doComments(hrate.value,comment.value)"/>
				 </div>
			</div>
   		</div>
	   
	    <div id="lan1">改变语言</div>
	  <div class="languagespan">
		  <select name="select" id="select" class="dropDownList">
             <!--<option selected="selected" value="zh">Chinese</option>
            <option value="us">English</option>
            <option value="es">Spanish</option>-->
            <option selected="selected" value="zh">Chinese</option><option value="us">English</option><option value="es">Spanish</option><option value="ru">Russian</option>          </select>
		  <input name="goButton" class="goButton" type="button" value="OK" onclick="toEn('select')"/>
	  </div>
	  <div style="border-bottom:1px solid #C8C8C8; padding-bottom: 10px;"></div>
      <!-- InstanceBeginEditable name="rbottom" --><!-- InstanceEndEditable --></div>
<!--关闭数据库连接-->
<!--新闻、产品和快速导航结束-->
<div style="float:top;height:15px; background-color:#FFFFFF;clear:both;">&nbsp;</div>
<!--页脚开始-->
<div id="footer">
<div style=" margin:2px;">Copyright@2009 www.sieyuan.com reserved 沪ICP备06005919号</div>
</div>
<!--页脚结束-->
</div> 
<!-- end container -->
</body>
<!-- InstanceEnd --></html>