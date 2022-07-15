let pointer_map
let pointer_marker
let oldMapData = undefined
let oldMapCenter = undefined
async function changeMap(){
  mapData = await getLocation()
  if(oldMapData===undefined || onloadedmetadata===undefined){
      oldMapData = mapData
      oldMapCenter = mapData
      pointer_map.setCenter(mapData)
      pointer_map.setZoom(18)
      pointer_marker.setPosition(mapData)
  }
  if(Math.abs(mapData.lat - oldMapData.lat)>0.0001 || Math.abs(mapData.lng - oldMapData.lng)>0.0001){
      pointer_marker.setPosition(mapData)
      oldMapData = mapData
  }
  if(Math.abs(mapData.lat - oldMapCenter.lat)>0.001 || Math.abs(mapData.lng - oldMapCenter.lng)>0.001){
      pointer_map.setCenter(mapData)
      oldMapCenter = mapData
  }
  storeHistory(mapData.lat, mapData.lng, mapData.time, mapData.date)
}
async function resetMapInfo(){
    const uluru = {lat:23.9037, lng:121.0794}
    pointer_map.setCenter(uluru)
    pointer_map.setZoom(5)
    pointer_marker.setPosition(uluru)
    oldMapData = undefined
    oldMapCenter = undefined
}
async function initMap() {
  // The location of Uluru
  const uluru = {lat:23.9037, lng:121.0794}
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 5,
    center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
  pointer_map = map
  pointer_marker = marker
}
async function getLocation(){ 
  // get location from ESP8266
  var mapData = await fetch("http://34.67.135.20/getLocation").then(res=>{
      return res.json()
  })
  mapData.lat = parseFloat(mapData.lat)
  mapData.lng = parseFloat(mapData.long)
  delete mapData.long
  return mapData
}
