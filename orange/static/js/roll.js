$(document).ready(function(){
	$('#J_next span').click(function(){
		rgmove();
		
	});
	$('#J_prev span').click(function(){
		lfmove();
		
	});
	$('#J_next2 span').click(function(){
		rg();
		
	});
	$('#J_prev2 span').click(function(){
		lf();
		
	});
	$('#J_next3 span').click(function(){
		rgmove2();
		
	})
	$('#J_prev3 span').click(function(){
		lfmove2();
		
	})
})
function lfmove(){
	$('.ullist li:first').appendTo($('.ullist'));
	$('.ullist').css({'left':0+'px'}).animate({
				'left':228+'px'
	},2500,'easeInBack');
}
function rgmove(){
	  
            $('.ullist li:last').prependTo($('.ullist'));
           $('.ullist').css({'left' : -228 + 'px'}).stop(true,true).animate({'left' :0 +'px'},2000);

    
}
function lf(){
	$('.ullist2 li:first').appendTo($('.ullist2'));
	$('.ullist2').css({'left':0+'px'}).animate({
				'left':75+'px'
	},2500,'easeInBack');
}
function rg(){
	  
            $('.ullist2 li:last').prependTo($('.ullist2'));
           $('.ullist2').css({'left' : -75 + 'px'}).stop(true,true).animate({'left' :0 +'px'},2000);

    
}

function lfmove2(){
	$('.ulli li:first').appendTo($('.ulli'));
	$('.ulli').css({'left':0+'px'}).animate({
				'left':418+'px'
	},2500,'easeInBack');
}
function rgmove2(){
	  
            $('.ulli li:last').prependTo($('.ulli'));
           $('.ulli').css({'left' : -418 + 'px'}).stop(true,true).animate({'left' :0 +'px'},2000);

    
}