var canvas = document.getElementById('myCanvas');
canvas.height = 1000; canvas.width = 1300;
var ctx = canvas.getContext('2d');
ctx.fillStyle = "black";

const rectheight = 10;
const rectwidth = 10;

const dnaLength = 500; //유전자 길이
const dnaCount = 2; //유전자 개수


var xInit = 100, yInit = 100;

let xPosition = new Array(dnaCount);
let yPosition = new Array(dnaCount);

let dnaArrayAll = new Array(dnaCount);
let rectArray = new Array(dnaCount);


(function makeDnaArray() {
    // 2차원 배열 초기화
    
    for (let i = 0; i < dnaCount; i++){
        dnaArrayAll[i] = new Array(dnaLength);
    }

    // DNA에 랜덤값 대입
    for (let i = 0; i < dnaCount; i++) {
        for (let j = 0; j < dnaLength; j++) {
            dnaArrayAll[i][j] = Math.floor(Math.random() * 4);
        }
    }
})();

(function makeRectangle() {
    for (let i = 0; i < dnaCount; i++) {
        //rectArray[i] = new Path2D();
        //rectArray[i].rect(xInit, yInit, rectwidth, rectheight);
        a = new Path2D();

        //ctx.fill(rectArray[i]);
    }
})();
/*
function decideAndSaveDirection(inputDnaArray, i, j) {
    if (j === 0) {
        xPosition[i] = xInit;
        yPosition[i] = yInit;
        console.log("init");
    } else {
        if (inputDnaArray === 0) {
            --xPosition[i];
            
        } else if (inputDnaArray === 1) {
            ++xPosition[i];
            
        } else if (inputDnaArray === 2) {
            --yPosition[i];
            
        } else { 
            ++yPosition[i];
        }
    }
}


let for_i = 0, for_j = 0;

function draw() {
    //ctx.clearRect(0,0,canvas.width,canvas.height);

    for (let i = 0; i < dnaCount; i++) {
        
        decideAndSaveDirection(dnaArrayAll[i][for_j], i, for_j);


        //console.log(xPosition,yPosition);

        rectArray[i].rect(xPosition[i], yPosition[i], rectwidth, rectheight);
        ctx.fill(rectArray[i]);
        ctx.fillStyle = "rgb(25, 25, 25)";
    
    }

    //ctx.beginPath();
    //ctx.rect(x, y, 20, 20);
    //ctx.fillStyle = 'rgba(250,0,0,0.4)';
    //ctx.fill();

    //x += 2;
    if (for_j > dnaLength) {
        for_j = 0;
        console.log("end");
    } else {
        for_j++;
    }
    
    
    // if (for_j > dnaLength -2) {
    //     for_i++;
    //     for_j = 0;
    // } else {
    //     for_j++;
    // }

    //ctx.fillStyle = "rgba(4,5,3,0.01)"; //배경색 및 투명도
    //ctx.fillRect(0, 0, canvas.width, canvas.height);
    //requestAnimationFrame(draw);
    
}
*/
//setInterval(draw, 100);