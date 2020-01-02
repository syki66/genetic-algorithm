var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

const xInitPos = 40;
const yInitPos = 40;

var xPos = 40;
var yPos = 40;

const lengthOfDna = 500; //유전자 길이
const countOfDna = 100; //유전자 개수

var allDnaArray = new Array(countOfDna);


function dnaArray() {
    // 2차원 배열 초기화
    for (var i = 0; i < countOfDna; i++){
        allDnaArray[i] = new Array(lengthOfDna);
    }

    // DNA에 랜덤값 대입
    for (var i = 0; i < countOfDna; i++) {
        for (var j = 0; j < lengthOfDna; j++) {
            allDnaArray[i][j] = Math.floor(Math.random() * 4);
        }
    }
}

dnaArray();


function decideDirection (inputDnaArray, i, j) {
    if (inputDnaArray[i][j] === 0) {
        xPos--;
    } else if (inputDnaArray[i][j] === 1) {
        xPos++;
    } else if (inputDnaArray[i][j] === 2) {
        yPos--;
    } else {
        yPos++;
    }
}


var allDnaArray_i = 0;
var allDnaArray_j = 0;

function moveRect() {
    ctx.clearRect(0,0, canvas.width, canvas.height); // 사각형 자취 제거

    decideDirection(allDnaArray, allDnaArray_i, allDnaArray_j);

    ctx.beginPath();
    ctx.rect(xPos, yPos, 10,10);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();

    // for문처럼 쓸라고
    if (allDnaArray_j > lengthOfDna-2) {
        allDnaArray_i++;
        allDnaArray_j = 0;

        xPos = xInitPos; //위치 초기화
        yPos = yInitPos;
    } else {
        allDnaArray_j++;
    }
    //console.log(allDnaArray_i, allDnaArray_j);
}










setInterval(moveRect,0.0000001);