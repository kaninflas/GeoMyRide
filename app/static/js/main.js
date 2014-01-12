var map,mapOptions, poly,marker,interval,mapFlag= false;
function maps(i){

	$('#geoMap #myModalLabel').html('GeoMy '+i.name)
	interval = setInterval(function(){geomyride(i)},5000)

	geomyride(i)
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

		google.maps.event.addListenerOnce(map, 'idle', function(){
  			
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

		});

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
	      	'id': id.id,
	      	'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
	      },
	      success: function(data){
	      	init_map(data)     	
	      	$('#geoMap #myModalLabel').html('GEO MY '+ id.name + ' - ' + data[0].timestamp)
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
    		}else{
    			var mark = new google.maps.Marker({
    				position: latLng,    				
    				icon: {
    				  path: google.maps.SymbolPath.CIRCLE,
    				  scale: 3
    				},
    			 	title: 'Position' ,
    			 	map: map
    			});
    			mark.setMap(map)
    		}
            path.push(latLng);
    });

    poly.setPath(path);
    console.log(poly)
}

