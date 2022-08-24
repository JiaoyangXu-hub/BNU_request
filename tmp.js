
var limitBookDate = '3';
var limitBookCount = '2';
var time_date = '2022-08-24';
var day_sable = '0';



	//验证码
	$(document).ready(function(){
		 $('#kaptchaImage').click(function() {  
	            $(this).attr('src', '/Kaptcha.jpg?' + Math.floor(Math.random() * 100));  
	        }); 
    });
    
    function checkCodeAjax(){
		var checkcodeusr = $('#checkcodeuser').val();
		var _url = "/front/frontAction.do?ms=checkCodeAjax&checkcodeuser=" +  checkcodeusr;
		$.ajax({
			type: "POST",
			url: _url,
			success: function(msg){//回调函数 
				if(msg == "success"){
				$('#msginfo').html("√");
				$('#msginfo').removeClass("redcolor");
				$('#msginfo').addClass("greencolor");
				}else if(msg == "failure"){			
					$('#msginfo').html("×");
					$('#msginfo').removeClass("greencolor");
					$('#msginfo').addClass("redcolor");
				}
			}
		});
	}

function viewBookTable() {
	var gymId = '2';
	var itemId = '5462';
	var timeDate='2022-08-24';
	var userTypeNum = '1';
	var url = "/gymsite/cacheAction.do?ms=viewBook&gymnasium_id="+gymId+"&item_id="+itemId+"&time_date="+timeDate+"&userType="+userTypeNum;
	$("#bookTableDiv").html("<iframe id=\"overlayView\" name=\"overlayView\" width=\"100%\" frameborder=no  src=\""+url+"\" onload=\"this.height=this.contentWindow.document.documentElement.scrollHeight\"></iframe>");
	if('1'=='1') {
		$("#overlayView").load(function() {
			$("th[can_see_student='1']",$(window.frames["overlayView"].document)).each(function() {
				$(this).hide();
			});
			$("td[can_see_student='1']",$(window.frames["overlayView"].document)).each(function() {
				$(this).hide();
			});
			$("th",$(window.frames["overlayView"].document)).each(function() {});
		});
		
	}

}


function highLightDate(time_date) {
	$(".datetime_").removeClass("red");
	$(".datetime_").each(function() {
		if ($(this).attr("value")==time_date) {
			$(this).addClass("red");
		}
	});
}
//退订
function unsubscribe(bookId) {
	if(!confirm("确认取消场地!")) {
		return;
	}
	$("#myWait").show();
	var gymId = '2';
	var itemId = '5462';
	var timeDate='2022-08-24';
	var userTypeNum = '1';
	var url = "gymbook/gymBookAction.do?ms=unsubscribe&gymnasium_id="+gymId+"&item_id="+itemId+"&time_date="+timeDate+"&userType="+userTypeNum+"&putongRes=putongRes";
	$.post(url,{bookId:bookId},function(msg){
		alert(msg);
		document.location.reload();
	});
}

function saveAttentionState() {
	var url = "gymbook/gymBookAction.do?ms=saveAttentionState";
	$.post(url,function(msg){
	});
}

function saveIntegrityModal() {
	var url = "gymbook/gymBookAction.do?ms=saveIntegrityModal";
	$.post(url,function(msg){
		$('#attentionModal').modal('show');
	});
}

function saveOdder() {
	//增加判断，是否已添加联系方式
	var url = "/gymbook/gymBookAction.do?ms=hadContactOrNot";
	$.post(url,{},function(msg){
		if("do_not" == msg){
			$('#contactModal').modal('show');
		}else{
			$("#book_person_phone").val(msg);
			showSelected();
		}
	});
}
function showSelected() {
	$("#selectedPayWay").val("1");
	$('#onlyNetPayWay_div').hide();
	$('#selectPayWay_div').hide();
	if(!checkSelected()){
		alert('没有选中的预约信息');
		return;
	}
	var time_date;
	var tSession;
	$.each($(".ckSelected"),function(i,o){
		if(o.checked){
				var time_date_tSession = $(this).parent().prev().prev().html();
			time_date = time_date_tSession.split(" ")[0];
			tSession = time_date_tSession.split(" ")[1];
			return;
		}
	});
	if(isLateForPay(time_date,tSession)) {
		$("#selectedPayWay").val("1");
		$('#onlyNetPayWay_div').show();
	}else {
		$('#selectPayWay_div').show();
	}
	/* var companion_number = $("#companion_number").val();
	if(companion_number != "" && companion_number != "0") { */
	$('#contactCompanion').modal('show');
	/* }else {
		saveBookFrmWithPay();
	} */
}

function isLateForPay(time_date,tSession) {
	var now = new Date();
    var sd=time_date.split("-");
    eval("sd[1]=" + sd[1] + "-1");
    var dNow = new Date(now.getFullYear(),now.getMonth(),now.getDate()).getTime();
    var dTarget = new Date(sd[0],sd[1],sd[2]).getTime();
    if(dTarget-dNow>24*3600*1000) {
    	return false;
    }
	if( dNow < dTarget ) {
		var endHour = tSession.substr(0,tSession.indexOf('-'));
		endHour = endHour.substring(0,endHour.indexOf(':'));
		eval("endHour="+endHour+";");
		return (24-now.getHours())+endHour<15;
	}
	
	return true;
}

function payLater() {
	$('#contactCompanion').modal('hide');
	window.location.href="/gymbook/payAction.do?ms=getOrdersForNopay";
}

function saveBookFrmWithPay(isPrintStub){
	var checkcodeuser = $("#checkcodeuser").val();
	if(!$.trim(checkcodeuser)){
		alert('验证码不能为空');
		return;
	}
	if(!checkSelected()){
		alert('没有选中的预约信息');
		return;
	}
	if($("#selectPayWay1").prop("checked")) {
		$("#selectedPayWay").val("1");
	}else {
		$("#selectedPayWay").val("0");
	}
	$("#selectedInfoPay").html("");
	
	ajaxSubmit('bookFrm', function(dataStr){
		submitFlag = false;
		var data = $.parseJSON(dataStr);
		if('预定成功' == data.msg) {
			if("yes"==data.freeMoney) {
				alert(data.msg);
				window.location.reload();
			}else {
				if("1"!=$("#selectedPayWay").val()) {
					alert("预订成功，请及时到现场交费,2小时内不缴费或不取消订单，系统将自动取消订单,并计入诚信记录");
					$('#contactCompanion').modal('hide');
					window.location.href="/gymbook/payAction.do?ms=getOrdersForNopay";
				}else {
					$("#selectedInfoPay").html($("#selectedInfo").html());
					$('#contactCompanion').modal('hide');
					$('#div_pay').modal('show');
					
				}
			}
		}else{
			alert(data.msg);
			window.location.reload();
		}

	});
}

function savePayFrmWithPay() {
	if(confirm("提示:支付完成后不能网上退订,确定继续支付? ")) {
		$("#payFrm").attr("action","/pay/payAction.do?ms=newPay").submit();
		/* ajaxSubmit('payFrm', function(msg){
			if(msg=="fail") {
				
				//alert("提交支付请求未授理，请检查您的网络连接情况，稍后再试");
			}else {
				var o = eval("("+msg+")");
				$("#stopForm").attr("action",o.req_url_web);
				$("#paycode").val(o.paycode);
				$("#payer").val(o.payer);
				$("#payertype").val(o.payertype);
				$("#payername").val(o.payername);
				$("#sn").val(o.sn);
				$("#amt").val(o.amt);
				$("#sno_id_name").val(o.sno_id_name);
				$("#sign").val(o.sign);	
				$("#stopForm").submit();
				$('#pay_process').modal('show');
			}
		}); */
	}
	
}

$(document).ready(function() {
	var companion_number = $("#companion_number").val();
	if(companion_number != "" && companion_number != "0") {
		$("#addCompanion").show();
		companion_number = parseInt(companion_number);
		for(var i=1;i<=companion_number;i++) {
			$("#companion_span_"+i).show();
		}
	}
});

function companionCheckNumLength(obj) {
	var $obj = $(obj);
	if(isEmpty($obj.val())) {
		return;
	}
	queryName1(obj,'fillUser');
}

function queryName1(iptId,callBack,panelTarget) {
	var name = $(iptId).val();
	if(!isNaN(name)) {
		if(name.length<4) {
			return;
		}
	}
	if(isNaN(name)) {
		var reg = /^[\u4E00-\u9FA5]+$/;   
	    if(!reg.test(name)){   
	        return;   
	    }else {
			if(name.length<2) {
				return;
			}
	    } 
	}
	$(iptId).hide();
	$(iptId).next().val("正在搜索'"+$(iptId).val()+"'");
	$(iptId).val("");
	$(iptId).next().show();
	$(iptId).next().focus();
	var thisId = $(iptId).attr("id");
	if(!isEmpty(name)) {
		$("#"+thisId+"3").html("<td>请稍后...</td>");
		/*if(panelTarget) {
			$("#"+panelTarget).append($("#teacherRecordDiv"));
		}*/
		$("#"+thisId+"2").show();
		var url = "/gymbook/gymBookAction.do?ms=queryName&name="+name;
		$.post(url,function(dataStr){
			$("#"+thisId+"3").html("");
			if(dataStr) {
				var allTeacherRecord = $.parseJSON(dataStr);
				if(allTeacherRecord.length > 0) {
					if(allTeacherRecord.length == 1){
						var o = allTeacherRecord[0];
						$(iptId).val(o.val1+"("+o.val2+")");
						$("#"+thisId+"2").hide();
					}else{
						$.each(allTeacherRecord,function(i,o){
							if (o.val7!=null && o.val7!="") {
								$("#"+thisId+"3").append("<tr style='background:\'lightyellow\'; color:\'red\''><td>"+o.val1+"</td><td><a href=\"javascript:setYHID('"+thisId+"','"+o.val1+"("+o.val2+")');\">"+o.val2+"</a></td><td>"+o.val3+"</td><td>"+o.val4+"</td><td>"+o.val5+"</td><td>"+o.val6+"</td><td><a target='_blank' href='/integrity/integrityAction.do?ms=getBlackList&searchCondition=" + o.val1 + "' style=\"font-color: \'red\'\">已记入黑名单</a></td></tr>");
							} else {
								$("#"+thisId+"3").append("<tr style='background:\'lightyellow\''><td>"+o.val1+"</td><td><a href=\"javascript:setYHID('"+thisId+"','"+o.val1+"("+o.val2+")');\">"+o.val2+"</a></td><td>"+o.val3+"</td><td>"+o.val4+"</td><td>"+o.val5+"</td><td>"+o.val6+"</td><td><a class='selUser' href=\"javascript:setYHID('"+thisId+"','"+o.val1+"("+o.val2+")');\">选择</a></td></tr>");
							}
						});
					}
				}else{
					$("#"+thisId+"3").append("<td>未找到姓名或证件号为"+name+"的信息</td>");
				}
				
				
			}
			$(iptId).show();
			$(iptId).focus();
			$(iptId).next().hide();
		});
		
	}
}
