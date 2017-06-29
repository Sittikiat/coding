// // function Async
// function funcAsync(callback) {
//     callback();
// }

// // function ธรรมดา
// function funcCallBack() {
//     console.log("This is callback function");
// }

// funcAsync(funcCallBack);

//------------------------------------

const fn1 = function() {
    setTimeout(function() {
        console.log("fn1");
    }, 2000);
}
const fn2 = function() {
    fn1();
    setTimeout(function() {
        console.log("fn2");
    }, 1000);
}
const fn3 = function() {
    fn2();
}

fn3();
