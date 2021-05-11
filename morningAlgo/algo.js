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

// Create a function that returns as boolean of true/false for whether or not an input string is a strict pallindrome. Do not ignore whitespaces!!

// Example 1: "racecar" --> true
// Example 2: "Dud" --> false
// Example 3: "oho!" --> false

function isPallindrome(str) {
    let i = 0;
    let j = str.length - 1;
    while (i < j) {
        if (str[i] !== str[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

console.log(isPallindrome("racecar"));
console.log(isPallindrome("Dud"));
console.log(isPallindrome("oho!"));


// Given a String, return the longest pallindromic substring. Given "hello dada", return "dad". Given "not much" return "n". Include spaces as well!

// Example 1: "my favorite racecar erupted" --> "e racecar e"
// Example 2: "nada" --> "ada"
// Example 3: "nothing to see" --> "ee"

function longestPallindrome(str) {
    let longest = 0;
    let k = 0;
    let z = 0;

    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j < str.length; j++) {
            if (helper(str, i, j)) {
                if (longest < (j - i)) {
                    longest = j - i;
                    k = i;
                    z = j;
                }
            }
        }
    }
    return str.slice(k, z + 1)
}

function helper(str, i, j) {
    while (i < j) {
        if (str[i] !== str[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}
console.log(longestPallindrome("my favorite racecar erupted"));
console.log(longestPallindrome("nada"));
console.log(longestPallindrome("nothing to see"));