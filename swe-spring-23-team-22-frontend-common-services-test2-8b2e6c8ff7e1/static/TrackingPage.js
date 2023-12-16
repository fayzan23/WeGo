mapboxgl.accessToken = 'pk.eyJ1IjoibXNjeWhldiIsImEiOiJjbGRjZ2NxMWcwNHlqM3Ftdnk5bWxpNTA2In0.eVb9A1KnXMC8RXlJjetGpw';
var map
var carExists = false
// map creation function
function createMap() {
    // Define the route coordinates
    var start = [-97.754717, 30.22837];//st eds coordinates
    // Define the map
    map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: start,
        zoom: 12
    });

    // Add a source and layer for the car image
    map.loadImage('/static/vehicle.png', function(error, image) {
        if (error) throw error;
        if (!map.hasImage('car')) map.addImage('car', image);
        map.addSource('car', {
            type: 'geojson',
            data: {
                type: 'FeatureCollection',
                features: []
            }
        });
        map.addLayer({
            id: 'car',
            type: 'symbol',
            source: 'car',
            layout: {
                'icon-image': 'car',
                'icon-size': 0.2,
                'icon-rotate': ['get', 'bearing'],
                'icon-allow-overlap': true,
                'icon-ignore-placement': true
            }
        });
    });
}

// fn to add the route polyline to the map
function addRouteToMap(routeData) {
    // Extract the route coordinates from the data
    const routeCoords = routeData.route.map(coord => [coord[0], coord[1]]);
  
    // Add the route to the map
    map.getSource('route').setData({
      'type': 'FeatureCollection',
      'features': [{
        'type': 'Feature',
        'geometry': {
          'type': 'LineString',
          'coordinates': routeCoords
        }
      }]
    });
  }
// draw route polyline
  function drawPolyline(coordinates) {
    if (map.getSource('polyline')) {
      map.removeLayer('route');
      map.removeSource('polyline');
    }
  
    map.addSource('polyline', {
      'type': 'geojson',
      'data': {
        'type': 'Feature',
        'properties': {},
        'geometry': {
          'type': 'LineString',
          'coordinates': coordinates
        }
      }
    });
  
    map.addLayer({
      'id': 'route',
      'type': 'line',
      'source': 'polyline',
      'layout': {
        'line-join': 'round',
        'line-cap': 'round'
      },
      'paint': {
        'line-color': '#3887be',
        'line-width': 5,
        'line-opacity': 0.75
      }
    });
  }

function getRoute(orderData) {

    // get the destination from the order data
    var destination = orderData.destination;
  
    // geocode the destination using the Google Maps Geocoding API
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'address': destination }, function (results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            var lat = results[0].geometry.location.lat();
            var lng = results[0].geometry.location.lng();
            var coords = [lng, lat];
            console.log("Geocoded destination: ", coords);

            // make a call to the Demand API endpoint 
            var order = {
                orderID: orderData.orderID,
                destination: coords,
                suppliesNeeded: orderData.suppliesNeeded,
                quantity: orderData.quantity,
                pluginType: orderData.pluginType
            }
            var url = "https://swesupply2023team22.xyz/api/demandAPI/order"

            fetch(url, {
                method: 'POST',
                body: JSON.stringify(order),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Error retrieving data.');
                }
            })
            .then(data => {
                console.log(`Route to destination: ${data.route}`);
                console.log(`Optimal vehicle ID: ${data.vehicleID}`);
                drawPolyline(data.route);
            })
            .catch(error => {
                console.error(error);
            });
        } else {
            console.log("Geocoding failed: ", status);
            return null;
        }
    });
}



// fn to get current location of a Vehicle
async function getCurrentLocation(vehicleID) {
    // request to Heartbeat API endpoint
    const url = `/api/demandHeartBeat/${vehicleID}`;
    const response = await fetch(url);
    // error handling for bad response
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // return requested location
    const data = await response.json();
    return data.currLocation;
}

// fn to track location of Vehicle
async function trackVehicle(vehicleID, orderID, destination) {
    // create marker for the car on the map
    const carMarker = new mapboxgl.Marker({ color: 'red' }).setLngLat(route[0]).addTo(map);
  
    // start Heartbeat loop
    while (true) {
      const currLocation = await getCurrentLocation(vehicleID);
      // check if the vehicle has reached its destination
      if (currLocation === destination) {
        console.log("Vehicle has reached its destination!");
        // update order status to complete
        const url = `/orders/${orderID}`;
        const data = { 'orderStatus': 'Complete' };
        const response = await fetch(url, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        break;
      }
      // update car marker position to current location
      carMarker.setLngLat(currLocation);
      // wait for a few seconds before checking again
      await new Promise((resolve) => setTimeout(resolve, 5000));
    }
}