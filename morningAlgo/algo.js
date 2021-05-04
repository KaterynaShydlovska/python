// Create a function that, given a string, returns the string's acronym (first letter's only, capitalized).

// Example: "there's no free lunch - gotta pay yer way" --> "TNFL - GPYW""

function acronym(str) {
    let res = "";
    let newStr = str.split(" ");
    for (let i = 0; i < newStr.length; i++) {
        if (newStr[i][0] === "-") {
            res += " " + newStr[i][0] + " "
        } else {
            res += newStr[i][0];
        }
    }
    res = res.toUpperCase()
    return res
}
console.log(acronym("there's no free lunch - gotta pay yer way")); // "TNFL - GPYW"



// Implement reverseString(str) that takes in a String, and then returns the same string of the same length, but with the characters reversed.

// Example: "creature" ---> "erutaerc"

// ** Don't use the built-in reverse() method!

function reverseString(str) {
    let res = "";
    for (let i = str.length - 1; i >= 0; i--) {
        res += str[i]
    }
    return res;
}

console.log(reverseString("creature")); // "erutaerc"


// Create a function that, given an input string, returns a boolean whether parentheses in that string are valid.

// Example 1:"y(3(p)p(3)r)s" --> true
// Example 2: "n(0(p)3" --> false
// Example 3: "n)0(t(o)k" --> false

// hint: consider using an array or object to solve

function parensValid(str) {
    let arr = [];

    for (let i = 0; i < str.length; i++) {
        if (str[i] === "(") {
            arr.push(str[i])
        } else if (str[i] === ")") {
            if (arr.length === 0) {
                return false;
            }
            arr.pop()
        }
    }
    if (arr.length === 0) {
        return true;
    } else {
        return false;
    }
}

parensValid("()")


// Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid. 

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[]}}(){}{()}" --> true

// hint: consider using an array or object to solve

function bracesValid(str) {
    let arr = [];

    for (let i = 0; i < str.length; i++) {

        if (str[i] === "(" || str[i] === "[" || str[i] === "{") {
            arr.push(str[i])
        } else if (str[i] === ")" && arr[arr.length - 1] === "(" || str[i] === "}" && arr[arr.length - 1] === "{" || str[i] === "]" && arr[arr.length - 1] === "[") {
            arr.pop();
        } else {
            return false;
        }
    }

    if (arr.length === 0) {
        return true;
    } else {
        return false;
    }
}


bracesValid("d(i{a}l[t]o)n{e!")