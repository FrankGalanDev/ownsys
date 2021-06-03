
function updateMsg(){
	console.log('Requesting JSON')
	$.getJSON('chat_messages', function(rowz) {
		console.log(JSON, rowz);
		$('#chatcontent').empty();
		for(var i=0; i<rowz.length; i++){
			arow =rowz[i];
			console.log(arow);
			$('#chatcontent').append('<p>' + arow[0].message+
				'<br/>'+ arow[0].created_at+'<br/>'+
				'By: '+ arow[0].owner.username+"</p>\n");
			
		}
		setTimeout('updateMsg()',4000);
	});
}

//Making sure JSON request is not cached
$(document).ready(function(){
	$.ajaxSetup({cache : false});
	updateMsg();
	
});


