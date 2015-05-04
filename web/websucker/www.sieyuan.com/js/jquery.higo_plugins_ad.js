/*!
jquery.higo_plugins_ad.js(v0.1)
http://www.higosoft.cn
mailto:wdong0472@gmail.com

Copyright (c) 2011 wdong
Dual licensed under the MIT and GPL licenses.
*/

/*
 * ͼƬ棨Generate a dock AD image
 *
 * USAGE: 
 *    $(selector).higo_plugins_ad({
 *        src:null,                    // ͼƬ·
 *        closeSrc:null,               // رͼƬ·
 *        href:"#",                    // ͼƬӵַ
 *        autoHide:true,               // ǷԶ
 *        hideSecond:10,               // ӳ
 *        top:20,                      // 붥ƫƸ߶
 *        layout:"left",               // ͼƬλãleft  ,right , center , 
 *        width:100,                   // 
 *        height:100,                  // ߶
 *        opacity:0.5                     // ͸opacity:0.5(firefox), filter:alpha(opacity=50)(IE)
 *        setPosition:function(left, top){ // ԤԶʾλõķδʵ֣
 *            return;
 *        }    
 *    })
 */
 
(function($){
    $.fn.lastScrollY= 0;
    $.fn.higo_plugins_ad = function(options){
        $(this).addClass("higo_plugins_ad");
        var settings = $.extend({
            src:null,                    
            closeSrc:null,               
            href:"#",
            autoHide:true,               
            hideSecond:10,               
            top:20,                      
            layout:"left",               
            width:100,                   
            height:100,                  
            opacity:0.5,
            setPosition:function(left, top){
                return;
            }
        },options || {});
		
        
        if(settings.src && settings.closeSrc){        
            var imgEl = "<a href='" + settings.href + "' target='_self'><img border=0 width='" + settings.width + "px' height='" + settings.height + "px' src='" + settings.src + "' alt='人才招聘'/> <br></a>";
            var closeImgEl = "<a href=\"#\"; onclick=\"this.parentElement.style.visibility='hidden'\"><img border=0 src='" + settings.closeSrc +"'/></a>";
            
            $(this).append(imgEl + closeImgEl);
            
            $(this).css("position","absolute");
            $(this).css("top",settings.top + "px");
            $(this).css("opacity",settings.opacity);
            $(this).css("filter","alpha(opacity=" + parseInt(settings.opacity * 100)  + ")");
			$(this).css("height","210px");
			$(this).css("width","220px");
			$(this).css("background-color","#CCCCCC");
            
            switch(settings.layout) {
                case "left":
                    $(this).css("left","150px");
                    break;
                case "right":
                    $(this).css("right","150px");
                    break;
                case "center":
                    var left = (parseInt(window.screen.availWidth) - parseInt(settings.width))/2 + "px";
                    $(this).css("left",left);
                    break;
                default:
                    $(this).css("left","22px");
                    break;
            }
        } else {
            return;
        }
        
        if(settings.autoHide) {
            setTimeout("(function(){$('" + $(this).selector +  "').hide();})();",parseInt(settings.hideSecond) * 1000);
        }
        
        window.onscroll = function(){
            var diffY;
            if (document.documentElement && document.documentElement.scrollTop)
                diffY = document.documentElement.scrollTop;
            else if (document.body)
                diffY = document.body.scrollTop
            else {
                /*Netscape stuff*/
            }
            
            percent= 1 * (diffY - $.fn.lastScrollY);
            if(percent>0)
                percent=Math.ceil(percent);
            else 
                percent=Math.floor(percent);
            
            var top = $('.higo_plugins_ad').css("top");
            
            $('.higo_plugins_ad').css("top", parseInt(top) + percent + "px");
            $.fn.lastScrollY += percent;
        }
    }
})(jQuery);