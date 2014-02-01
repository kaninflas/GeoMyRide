var map, btn, infowindow,poly,polyOptions,marker,interval,mapFlag=false, geos=[];
function maps(i){
  geomyride(i)
	$('#geoMap #myModalLabel').html('GeoMy '+i.name)
  startGeo(i);

	$('#geoMap').on('shown.bs.modal', function () {
	    google.maps.event.trigger(map, "resize");
	});

	$('#geoMap').on('hide.bs.modal', function () {
     	clearInterval(interval);
     	map.set
     	mapFlag = false;
     	marker.setMap(null)
     	poly.setMap(null)
	});

  $('#pauseGeo').on('click', function(){pauseGeo()});
  $('#startGeo').on('click', function(){startGeo(i)});
}

function init_map(data) {
	if(!mapFlag){
		mapFlag = true;	
    var latLng = new google.maps.LatLng(data[0].lat, data[0].lan)	

		var mapOptions = {
		  center: latLng,
		  zoom: 16,
		  mapTypeId: google.maps.MapTypeId.ROADMAP
		};

		map = new google.maps.Map(document.getElementById("map_canvas"),mapOptions);

		google.maps.event.addListenerOnce(map, 'idle', function(){
  			
  			polyOptions = {        
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
          icon: BASE_PATH + 'img/fav.png'
  			});
  			marker.setMap(map)
  			addLatLng(data);

        map.setCenter(latLng);

        setInfowindow(data[0],marker); 

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
    deleteMarkers();
    poly.setMap(null)
    poly = new google.maps.Polyline(polyOptions);
    poly.setMap(map);    
    path = poly.getPath();

    $.each(data, function(key, val) {
    		var latLng = new google.maps.LatLng(val.lat, val.lan)
    		if(key === 0){
    	    	marker.setPosition(latLng)
    	    	map.setCenter(latLng);
            setInfowindow(val,marker)
    		}else{
    			var mark = new google.maps.Marker({
    				position: latLng,    				
    				icon: {
    				  url: BASE_PATH + 'img/fav.png'
    				},
    			 	title: 'Position' ,
    			 	map: map
    			});
          geos.push(mark)
          setInfowindow(val,mark)
    		}
            path.push(latLng);
    });

    poly.setPath(path);
    console.log(poly)
}

// Sets the map on all markers in the array.
function setAllMap(map) {
  for (var i = 0; i < geos.length; i++) {
    geos[i].setMap(map);
  }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
  setAllMap(null);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
  clearMarkers();
  geos = [];
}

function setInfowindow(data,me){
  console.log(me)
  var content = "<h4>"+ data.aprs+ "</h4>";
  content += "<p> <strong>Hora: </strong>"+ data.timestamp+"</p>"
  content += "<p> <strong>Velocidad: </strong>"+ data.speed+" kms/hra</p>"
  infowindow = new google.maps.InfoWindow({
      content: "<div id='infowindow'>" + content + "<div>",
  });

  google.maps.event.addListener(me, 'click', function () {
    infowindow.setContent(content);
    infowindow.open(map, me);
  });
}

function pauseGeo(){
  clearInterval(interval);
  console.log("pause");
}
function startGeo(i){  
  console.log(i);
  interval = setInterval(function(){geomyride(i)},5000)
  console.log("start");
}

