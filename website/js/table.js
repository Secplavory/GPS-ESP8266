let tbody = document.getElementsByTagName("tbody")[0]
let tbodyCount = 0
function storeHistory(lat, lng, time, date){
    tbodyCount += 1
    let tr = document.createElement("tr")
    let td_num = document.createElement("td")
    let td_lat = document.createElement("td")
    let td_lng = document.createElement("td")
    let td_time = document.createElement("td")
    let td_date = document.createElement("td")
    
    td_num.innerHTML = tbodyCount
    td_lat.innerHTML = lat
    td_lng.innerHTML = lng
    td_time.innerHTML = time
    td_date.innerHTML = date
    
    tr.appendChild(td_num)
    tr.appendChild(td_lat)
    tr.appendChild(td_lng)
    tr.appendChild(td_time)
    tr.appendChild(td_date)

    tbody.appendChild(tr)
}