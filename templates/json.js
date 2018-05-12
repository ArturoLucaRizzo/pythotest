$(document).ready(function(){


$("button").click(function(e) {
    e.preventDefault();
    var name = document.getElementById("name").value;
    var surname = document.getElementById("surname").value;


    if (name == parseInt(name)){
    }
    else{
     alert("name is not an integer");
     return
    }
    if (surname == parseInt(name)){
    }
    else{
     alert("surname is not an integer");
     return
    }

    ActiveDTO= {
					"name" : name,
					"surname" : surname,
			   }
 $.ajax({
			type: "POST",
			contentType : 'application/json;',
			dataType : 'json',
			url: "/readj",
			data : JSON.stringify({'js':ActiveDTO}),
			success :function(data) {
			document.getElementById('box').innerHTML = "result "+data.result;
			document.getElementById('ibox').style.display="none";


			}
		});

});

})