var variable_1 = 10; // GLOBAL
console.log(variable_1);

console.log(variable_2);  // undefined
var variable_2 = 223  // GLOBAL
console.log(variable_2); // 223
var variable_2
// In JS, there is the concept of "hoisting" where all var declarations will be "hoisted" to the top of the scope
// in which the variable was declared
// Hoisting only applies to var and NOT let or const

// No hoisting occures for let
let variable_3 // GLOBAL
console.log(variable_3);

// For loop in JS vs. Python
// having our variable go from 0 - 9
for (let i = 0; i < 10; i = i + 1) {  // i is block scoped (scoped to the loop)
    console.log(i);
}
// for i in range(10) => in python
//     print(i)
//--------------------------------------------------------------------------

// Realistic case of why let is important
// We have 1 variable in this example:
// 1. global scoped j
var j = 100;  // Developer 1 creates variable j with a value of 100

// Developer 2 creates a for loop using v j as well
for (var j = 0; j < 10; j++) {  // j is global scoped
    console.log(j);
}

console.log("End of loop")
console.log(" var j value: " + j); //10

// Developer 1 writes if statement expecting it to be true (they are not aware of developer 2's for loop)
if (j == 100) {
    console.log("Doing something...");
}
// Developer 1 is confused why Doing something... is not printed out

/*=======================================================================*/

// we have 2 variables in this example:
// 1. Global scoped k
// 2. Block scoped k
let k = 100;  // Global scoped k

for (let k = 0; k < 10; k++) {  // Block scoped k
    console.log(k);
}

console.log(" let k value: " + k)  //100

/*
==========================================================================
 */

var a = 100; //global scoped

function some_func() {
    var a = 1000; //function scoped (we are "shadowing" global scoped a, so we cannot access global scope a anymore)
    //variable_4 is function scoped
    if (true) {
        var variable_4 = 10;
    }

    console.log(variable_4); // 10
    console.log(a); //1000
}
// NOTE: SHADOWING IS AN IMPORTANT PROGRAMMING CONCEPT!!!
some_func();
console.log(a) //100