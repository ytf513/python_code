<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" ><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" ><!-- InstanceBegin template="/Templates/t2.dwt.php" codeOutsideHTMLIsLocked="false" -->
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<meta name="keywords" content="思源电气" />
<meta name="description" content = "思源电气股份有限公司是上海市重点高新技术企业，是国内知名的专业电力设备制造商，也是一家知名的上市企业。" />
<meta name="copyright" content="思源电气股份有限公司" />
<title></title>
<script language=javascript src="../js/emethod.js"></script>
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
		
		function setAppraise()
		{
			var obj = document.getElementById("DivAppraise");
			if(obj.style.display == "none")
				obj.style.display = "block";
			else
				obj.style.display = "none";
		}
		
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
<!-- InstanceParam name="OptionalRegion1" type="boolean" value="true" -->
</head>
<body onload="oneHeight(['lcontent2','mcontent2','rcontent2'])">
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
          <param name="movie" value="../images/flash/index.swf" />
          <param name="quality" value="high" />
          <embed src="../images/flash/index.swf" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="990" height="200"></embed>
     </object>
	 <!-- InstanceEndEditable -->	</div> 
 <!--Flash结束-->
<!--新闻、产品和快速导航开始-->
<div class="midlines"></div>
<div>
	<!--<div class="lcontent1">&nbsp;</div> -->
	<div id="lcontent2" class="lcontent2">
    	<!-- InstanceBeginEditable name="lcontent" -->
		<div class="lmenu" style="cursor:pointer;" onclick="sy_nv('../cn/news.php',['ftype'],['0'],'')" onmouseover="this.className='lmenu2'" onmouseout="this.className='lmenu'">公司新闻</div>
		<!--<div class="lmenu" style="cursor:pointer;" onclick="sy_nv('../cn/news.php',['ftype'],['1'],'')" onmouseover="this.className='lmenu2'" onmouseout="this.className='lmenu'">行业新闻</div> -->
		<div class="lmenu" style="cursor:pointer;" onclick="sy_nv('../cn/news.php',['ftype'],['2'],'')" onmouseover="this.className='lmenu2'" onmouseout="this.className='lmenu'">饮水思源</div>
		<!-- InstanceEndEditable --></div>
	<div id="mcontent2" class="mcontent2">
	  <!-- InstanceBeginEditable name="mcontent" -->
	   <div class="cultrue">
		  	<a href="../cn/">首页</a>-><a href="../cn/news.php?fid=0">新闻中心</a>-><a>公司新闻</a>		</div>
		<div class="news">
			 <ul class="myul">
		  				<li class="list">
					14-07-23&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=202&ftype=0">国际化的脚步从未停歇——思源电气为2018俄罗斯世界杯两座举办城市提供供电保障</a>
				</li>
								<li class="list">
					14-07-07&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=201&ftype=0">思源电气为特高压电网建设贡献精品装备</a>
				</li>
								<li class="list">
					14-07-04&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=200&ftype=0">思源电气巴西世界杯项目引媒体高度关注</a>
				</li>
								<li class="list">
					14-07-03&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=199&ftype=0">思源电气GIS产品正式进入墨西哥市场</a>
				</li>
								<li class="list">
					14-07-02&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=198&ftype=0">思源电气应用项目获电力建设科学技术进步一等奖</a>
				</li>
								<li class="list">
					14-07-01&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=197&ftype=0">思源电气合作项目获吉林省科学技术奖</a>
				</li>
								<li class="list">
					14-06-27&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=194&ftype=0">祖国强大是开拓海外市场的有力支撑</a>
				</li>
								<li class="list">
					14-06-27&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=195&ftype=0">国产装备在全球市场占有率逐年攀升</a>
				</li>
								<li class="list">
					14-06-25&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=193&ftype=0">中国电力设备企业思源电气进入巴西球馆为世界杯电力供应保驾护航</a>
				</li>
								<li class="list">
					14-06-24&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=192&ftype=0">思源电气逆袭海外市场</a>
				</li>
								<li class="list">
					14-06-16&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=190&ftype=0">高效服务世界杯比赛——思源电气参与世界杯电力项目建设</a>
				</li>
								<li class="list">
					14-06-16&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=191&ftype=0">中国电力设备企业在巴西舞起精彩桑巴</a>
				</li>
								<li class="list">
					14-06-13&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=196&ftype=0">思源电气承担的上海市首批高新技术产业化重大项目通过专家组验收</a>
				</li>
								<li class="list">
					14-05-30&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=189&ftype=0">思源电气召开哈勃SAP实施项目启动大会</a>
				</li>
								<li class="list">
					14-05-19&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=188&ftype=0">沙钢集团考察访问思源电气</a>
				</li>
								<li class="list">
					14-05-12&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=187&ftype=0">泰国首都电力局考察访问思源电气</a>
				</li>
								<li class="list">
					14-05-08&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=186&ftype=0">思源电气在国网二批集采中斩获佳绩</a>
				</li>
								<li class="list">
					14-05-05&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=185&ftype=0">印度哈瑞亚娜邦副省长考察访问思源电气</a>
				</li>
								<li class="list">
					14-04-21&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=184&ftype=0">聚源断路器机座顺利通过万次寿命验证</a>
				</li>
								<li class="list">
					14-04-14&nbsp;&nbsp;&nbsp;
					<a href="../cn/newsdetail.php?fid=182&ftype=0">李福寿思源电气奖学金签约仪式举行</a>
				</li>
							</ul>
			<div>&nbsp;</div>
			&nbsp;1<a href="news.php?page=1&ftype=0&pt=2">&nbsp;2</a><a href="news.php?page=2&ftype=0&pt=2">&nbsp;3</a><a href="news.php?page=3&ftype=0&pt=2">&nbsp;4</a><a href="news.php?page=4&ftype=0&pt=2">&nbsp;5</a><a href="news.php?page=5&ftype=0&pt=2">&nbsp;6</a><a href="news.php?page=6&ftype=0&pt=2">&nbsp;7</a><a href="news.php?page=7&ftype=0&pt=2">&nbsp;8</a><a href="news.php?page=8&ftype=0">&nbsp;...</a>		</div>
	  <!-- InstanceEndEditable --></div>
  <div id="rcontent2" class="rcontent2">
		<div class="searchspan">
			 <input name="searchInput" id="searchInput" class="searchFor" type="text" size="10" value="搜索" onclick="setSearchValue(this)" onkeydown="if(event.keyCode == 13) location.href ='../cn/search.php?searchField=' + this.value"/>
			  <input name="goButton" class="goButton" type="button" value="OK" onclick="location.href ='../cn/search.php?searchField=' + searchInput.value" />
		</div>
		
		<div>
			<ul class="myul">
				<li><a href="contact.php">联系我们</a></li>
			</ul>
		</div>
		
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
<div style="float:top;height:15px; background-color:#FFFFFF; clear:both;">&nbsp;</div>
<!--页脚开始-->
<div id="footer">
<div style=" margin:2px;">Copyright@2009 www.sieyuan.com reserved 沪ICP备06005919号</div>
</div>
<!--页脚结束-->
</div> 
<!-- end container -->
</body>
<!-- InstanceEnd --></html>