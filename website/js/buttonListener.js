let startButton = document.getElementById("StartButton")
let stopButton = document.getElementById("StopButton")
let timer = undefined;

startButton.addEventListener("click", ()=>{
    changeMap()
    timer = setInterval(changeMap, 3000)
})

stopButton.addEventListener("click", ()=>{
    clearInterval(timer)
    resetMapInfo()
})