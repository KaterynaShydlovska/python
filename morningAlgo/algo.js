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