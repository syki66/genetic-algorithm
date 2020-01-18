var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

const xInitPos = 40; // 초기 위치
const yInitPos = 40;

const dnaLength = 50; //유전자 길이
const dnaCount = 10; //유전자 개수

let xPos = 40;
let yPos = 40;


let dnaArrayAll = new Array(dnaCount);
let rectArray = new Array(dnaCount);

function makeDnaArray() {
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
}

function makeRectangleFactory() {
    ctx.clearRect(0,0, canvas.width, canvas.height);

    for (let i = 0; i < dnaCount; i++) {
        rectArray[i] = new Path2D();
        rectArray[i].rect(xPos, yPos, 10, 10);
        ctx.fill(rectArray[i]);
    }

}



function decideDirection (inputDnaArray) {
    if (inputDnaArray === 0) {
        xPos--;
    } else if (inputDnaArray === 1) {
        xPos++;
    } else if (inputDnaArray === 2) {
        yPos--;
    } else {
        yPos++;
    }
}


function moveRect() {
    makeDnaArray();
    for (let i = 0; i < dnaCount; i++) {
        for (let j = 0; j < dnaLength; j++) {
            decideDirection(dnaArrayAll[i][j]);
            console.log(dnaArrayAll[i][j]);

            ctx.clearRect(0,0, canvas.width, canvas.height);
            rectArray[i].rect(xPos, yPos, 10, 10);
            ctx.fill(rectArray[i]);
        }
    }
}



let dnaArrayAll_i = 0;
let dnaArrayAll_j = 0;

function moveRect2() {
    ctx.clearRect(0,0, canvas.width, canvas.height); // 사각형 자취 제거

    decideDirection(dnaArrayAll, dnaArrayAll_i, dnaArrayAll_j);
/*
    ctx.beginPath();
    ctx.rect(xPos, yPos, 10,10);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
*/


    /* // 얘는 스킵용으로 쓰기
    for (let i = 0; i < dnaCount; i++){
        for (let j = 0; j < dnaLength; j++) {
            decideDirection(dnaArrayAll, i, j);
            //console.log(dnaArrayAll, i, j);
        }

    }
    */

    
    // setinterval 써야되서.. (for문용)
    if (dnaArrayAll_j > dnaLength-2) {
        dnaArrayAll_i++;
        dnaArrayAll_j = 0;

        xPos = xInitPos; //위치 초기화
        yPos = yInitPos;
    } else {
        dnaArrayAll_j++;
    }
    //console.log(dnaArrayAll_i, dnaArrayAll_j);
}


for (let i = 0; i < dnaCount; i++) {
    rectArray[i] = new Path2D();

}
jj = 0;
function test () {
    
    ctx.beginPath();
    for (let i = 0; i < 10; i++) {
        
        rectArray[i].rect(i*20, jj, 10, 10);
        ctx.fill(rectArray[i]);
    }
    jj++;
    }

function init () {
    
    
    //setInterval(moveRect,5);
    //setInterval(RectangleFactory,500);
    //moveRect();
    setInterval(test, 500);

}






init();