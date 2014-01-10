var map,mapOptions, poly,marker,interval,mapFlag= false;
function maps(i){

	$('#geoMap #myModalLabel').html('GeoMy '+i.name)
	geomyride(i.id)
	interval = setInterval(function(){geomyride(i.id)},5000)

	$('#geoMap').on('shown.bs.modal', function () {
	    google.maps.event.trigger(map, "resize");
	});

	$('#geoMap').on('hide.bs.modal', function () {
     	clearInterval(interval);
     	map.set
     	mapFlag = false;
     	marker.setMap(null)
     	poly.setMap(null)
	})
}

function init_map(data) {
	if(!mapFlag){
		mapFlag = true;	
        var  latLng = new google.maps.LatLng(data[0].lat, data[0].lan)	

		mapOptions = {
		  center: latLng,
		  zoom: 14,
		  mapTypeId: google.maps.MapTypeId.ROADMAP
		};

		map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);

		var polyOptions = {
		  strokeColor: '#000000',
		  strokeOpacity: 0.8,
		  strokeWeight: 3
		};

		poly = new google.maps.Polyline(polyOptions);
		poly.setMap(map);

		marker = new google.maps.Marker({
			position: latLng,
		 	title: 'Geo My Ride' ,
		 	map: map,
		 	animation: google.maps.Animation.BOUNCE,
		});
		marker.setMap(map)
		addLatLng(data);

	}else{
		addLatLng(data);
	}


}

function geomyride(id){
	$.ajax({
	      type: "GET",
	      contentType: "application/json",
	      url: "/geomyride",
	      dataType: "json",
	      data:{
	      	'id': id,
	      	'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
	      },
	      success: function(data){
	      	init_map(data)     	
	      },
	      failure: function(data){
	      	console.log('error: ',data)
	      }
	});
}

function addLatLng(data){
    path = poly.getPath();

    $.each(data, function(key, val) {
    		var latLng = new google.maps.LatLng(val.lat, val.lan)
    		if(key === 0){
    	    	marker.setPosition(latLng)
    	    	map.setCenter(latLng);
    		}
            path.push(latLng);
    });

    poly.setPath(path);
    console.log(poly)
}

