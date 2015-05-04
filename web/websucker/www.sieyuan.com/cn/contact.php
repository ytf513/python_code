<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" ><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en" ><!-- InstanceBegin template="/Templates/t4.dwt.php" codeOutsideHTMLIsLocked="false" -->
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
<!-- InstanceParam name="OptionalRegion1" type="boolean" value="false" -->
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
            <param name="movie" value="../images/flash/services.swf" />
            <param name="quality" value="high" />
			<param name="wmode" value="transparent">
            <embed src="../images/flash/services.swf" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="990" height="200"></embed>
        </object>
	 <!-- InstanceEndEditable -->	</div> 
 <!--Flash结束-->
<!--新闻、产品和快速导航开始-->
<div class="midlines"></div>
<div>
	<div id="mcontent4" class="mcontent4">
	  <!-- InstanceBeginEditable name="mcontent" -->
	   <div class="cultrue">
		  <a href="../cn/">首页</a>-&gt;联系我们
		</div>
		<div class="conbody">
			<p>
<table border="0" cellspacing="0" cellpadding="0" width="80%">
    <tbody>
        <tr>
            <td width="50%">
            <div><span>思源电气股份有限公司</span></div>
            <div><span>地址:</span> <span>上海市闵行区华宁路3399号</span></div>
            <div><span>电话:</span> <span>021-61610502&nbsp;</span></div>
            <div><span>传真:</span> <span>021-61610900</span></div>
            <div><span>EMail:</span> <span><a href="mailto:webmaster@sieyuan.com">webmaster@sieyuan.com</a></span></div>
            <div><span>邮编:</span> <span>201108</span></div>
            <div><span>销售热线:</span> <span>021-61610977</span></div>
            <div><span>投资热线:</span> <span>021-61610958</span></div>
            <div>&nbsp;</div>
            <div><span>思源电气第一分公司</span></div>
            <div><span>地址:</span> <span>上海市闵行区金都路4399号</span></div>
            <div><span>电话:</span> <span>021-54830909</span></div>
            <div><span>传真:</span> <span>021-64420808</span></div>
            <div><span>邮编:</span> <span>201108</span></div>
            <div><span>销售热线:</span> <span>021-64420088</span></div>
            <div><span>&nbsp;</span></div>
            <div><span>江苏如高高压电器有限公司</span></div>
            <div><span>地址:</span> <span>江苏省如皋市经济技术开发区惠民西路1号</span></div>
            <div><span>电话:</span> <span>0513-87531599</span></div>
            <div><span>传真:</span> <span>0513-87527300</span></div>
            <div><span>邮编:</span> <span>226572</span></div>
            <div><span>销售热线:</span> <span>0513-87512453</span></div>
            <div>&nbsp;</div>
            <div><span>思源清能电气电子有限公司</span></div>
            <div><span>地址:</span> <span>上海市闵行区华宁路3399号</span></div>
            <div><span>电话:</span> <span>021-61610101</span></div>
            <div><span>传真:</span> <span>021-61610798</span></div>
            <div><span>邮编:</span> <span>201108</span></div>
            <div><span>销售热线:</span> 021-61610767</div>
            <div><span>&nbsp;</span></div>
            </td>
            <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
            <td width="50%">
            <div><span>&nbsp;</span></div>
            <div><span>上海思源高压开关有限公司</span></div>
            <div><span>地址:</span> <span>上海市闵行区华宁路3399号</span></div>
            <div><span>电话:</span> <span>021-61610909</span></div>
            <div><span>传真:</span> <span>021-61610900</span></div>
            <div><span>邮编:</span> <span>201108</span></div>
            <div><span>销售热线:</span> <span>021-61610335</span></div>
            <div><span>&nbsp;</span></div>
            <div><span>&nbsp;</span></div>
            <div><span>&nbsp;</span></div>
            <div><span>江苏思源赫兹互感器有限公司</span></div>
            <div><span>地址:</span> <span>江苏省如皋市经济开发区惠民西路5号</span></div>
            <div><span>电话:</span> <span>0513－87303629</span></div>
            <div><span>传真:</span> <span>0513－87530056</span></div>
            <div><span>邮编:</span> <span>226500</span></div>
            <div><span>销售热线:</span> <span>0513-87303636</span></div>
            <div><span>&nbsp;</span></div>
            <div><span>上海思源电力电容器有限公司</span></div>
            <div><span>地址:</span> <span>上海市闵行区申富路1199号</span></div>
            <div><span>电话:</span> <span>021-54831616</span></div>
            <div><span>传真:</span> <span>021-54831620</span></div>
            <div><span>邮编:</span> <span>201108</span></div>
            <div><span>销售热线:</span> <span>021-54831616</span></div>
            <div>&nbsp;</div>
            <div><span>上海思源弘瑞自动化有限公司</span></div>
            <div><span>地址：</span> <span>上海市闵行区华宁路3399号</span></div>
            <div><span>电话：</span> <span>021-61610701</span></div>
            <div><span>传真：</span>&nbsp;021-61610707</div>
            <div><span>邮编:</span> <span>201108</span></div>
            <div><span>销售热线：</span> <span>021-61610701</span></div>
            <p>&nbsp;</p>
            </td>
        </tr>
    </tbody>
</table>
</p>		</div>
	  <!-- InstanceEndEditable --></div>
  <div id="rcontent3" class="rcontent3">
		<div class="searchspan">
			 <input name="searchInput" id="searchInput" class="searchFor" type="text" size="10" value="搜索" onclick="setSearchValue(this)" onkeypress="if(event.keyCode == 13) location.href ='../cn/search.php?searchField=' + this.value"/>
			  <input name="goButton" class="goButton" type="button" value="OK" onclick="location.href ='../cn/search.php?searchField=' + searchInput.value"/>
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