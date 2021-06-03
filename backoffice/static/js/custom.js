// url of library https://jqueryui.com/datepicker/
$(function(){
    $("#id_valid_until").datepicker({ minDate:0 });
    });



function llenar(){ 
    alert('hola');
    var data='';
    var listarelaciones= [];
   
    var invoice_number = $("#id_invoice_number").val();
    var sold_item  = $("#id_sold_item").text();
    var code_item  = $("#id_sold_item").val();
    var customer  = $("#id_customer").text();
    var code_customer  = $("#id_customer").val();
    var quantity  = $("#id_quantity").val();    
    var subtotal =  $("#id_subtotal").val();
    var tax = $("#id_tax").val();
    var total = $("#id_total").val();
    var valid_until =  $("#id_valid_until").val();
    var code_courier =  $("#id_courier_name").val();
    var courier =  $("#id_courier_name").text();
    
    var invo = new relaciones(invoice_number,customer,code_customer,sold_item,code_item, quantity, subtotal,tax ,total ,valid_until,courier);
    listarelaciones.push(invo);
    data = JSON.stringify(listarelaciones);
    console.log(data);
    var tr ="<tr>";
    tr+="<td>"+invoice_number+"</td>";
    tr+="<td>"+customer+"</td>";  
    tr+="<td>"+sold_item+"</td>";
    tr+="<td>"+quantity+"</td>";  
    tr+="<td>"+subtotal+"</td>"; 
    tr+="<td>"+tax+"</td>"; 
    tr+="<td>"+total+"</td>"; 
    tr+="<td>"+valid_until+"</td>"; 
    tr+="<td>"+courier + "</td>"; 
    tr+="<td>"+"<input type=checkbox>"+"</td>";
    tr+="</tr>";
    var t = tr; 
    document.getElementById('invoice_table').innerHTML+=t;

    //cleaning the data

    document.getElementById('id_invoice_number').value="";
    document.getElementById('id_customer').value="";
    document.getElementById('id_sold_item').value="";
    document.getElementById('id_quantity').value="1";
    document.getElementById('id_subtotal').value="0.00";
    document.getElementById('id_tax').value="0.00";
    document.getElementById('id_total').value="0";
    document.getElementById('id_valid_until').value="";
    document.getElementById('id_courier_name').value="";
    
};

function relaciones(invoice_number,customer,code_customer,sold_item,code_item, quantity, subtotal,tax ,total ,valid_until,courier){
	this.invoice_number=invoice_number;
	this.customer=customer;
	this.code_customer=code_customer;
	this.sold_item=sold_item;
	this.code_item=code_item;
	this.quantity=quantity;
	this.subtotal=subtotal;
	this.tax=tax;
	this.total=total;
	this.valid_until=valid_until;
	this.courier=courier;

 };

/*
var ventas = { 
	items = {
    	invoice_number : '',
        sold_item : '',
        customer : '',
        quantity : '',    
        subtotal : 0.00 ,
        tax: 0.00,
        total : 0.00 ,
        valid_until: '' ,
        courier : '',
        item :[],
    }
}*/



$('input[name="search_box"]').autocomplete({

	source:function(request, response){

		alert(request.term);

		$.ajax({
			url:window.location.pathname,
			type: 'POST',
			data: {
				'action':'search_item',
			 	'term': request.term
			},
			dataType:'json',
        }).done(function(data){
        	response(data);
            console.log(data);
        }).fail(function (jqXHR,textStatus, errorTrown){
        	alert(errorTrown);
        }).always(function(data){

        });

	},
	delay: 500,
	minLength: 1,

	select: function(event, ui){
		
		console.log(data); 

	}
});

/*
$( function() {
    var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];
    $("#search_box").autocomplete({
      source: availableTags
    });
  } );

*/
