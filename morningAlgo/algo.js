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

// Given a dollar amount with change (an integer w/decimal) convert to change. Make sure to count the largest denomination first!

// Example: 3.21 --> 12 quarters, 2 dimes, 1 penny

function convertCoinChange(money) {
    // declare variables for different denominations (quarter, dime, nickel, penny)
    let q = 0 // each variable holds the count of each coin
    let d = 0
    let n = 0
    let p = 0

    money = money * 100
    q = Math.floor(money / 25)
    let rem = money - (q * 25)

    while (rem > 10) {
        rem -= 10;
        d += 1
    }

    if (rem > 5) {
        while (rem > 0) {
            rem -= 5;
            n += 1
        }
    }

    if (rem > 0) {
        while (rem > 0) {
            rem -= 1;
            p += 1;
        }
    }


    console.log("quarters: " + q)
    console.log("dimes: " + d)
    console.log("nickel: " + n)
    console.log("penny: " + p)
}

convertCoinChange(3.21)


// Write a function that given a sorted array of page numbers, return a string representing a book index. Combine consecutive pages to create ranges.

// Example: [1,3,4,5,6,7,8,10] --> "1, 3-8, 10"

function bookIndex(arr) {
    let str = ""
    let i = 0;
    let j = i + 1;

    while (j < arr.length) {

        if (arr[j] === arr[i] + 1) {
            str += arr[i]
            i++;
            j++;
        } else {
            i++;
            j++;
        }
    }
    return str[0] + "-" + (parseInt(str[str.length - 1]) + 1)
}

console.log(bookIndex([1, 2, 3, 4, 5, 6, 7, 8, 12, 10]))


class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class SLList {
    constructor() {
        this.head = null
    }

    addToFront(value) {
        var node = new Node(value);
        // node.next = this.head;
        // this.head = node;
        // return this;
        if (!this.head) {
            this.head = node
        } else {
            node.next = this.head;
            this.head = node;
        }
        return this
    }

    // given a value, add it to the back of your singly linked list
    // what if the list is empty?
    addToBack(value) {
        if (!this.head) {
            this.head = new Node(value)
        }
        let runner = this.head;
        while (runner.next) {
            runner = runner.next;
        }
        runner.next = new Node(value)
        return this
    }

    // given a value, print whether the list contains that value
    contains(value) {
        if (!this.head) {
            return null
        }
        let runner = this.head;
        while (runner) {
            if (runner.value === value) {
                return true
            }
            runner = runner.next
        }
        return false;
    }

    // remove the first node in the list
    removeFromFront() {
        if (!this.head) {
            return null
        }
        this.head = this.head.next
    }

    // remove the last node in the list
    removeFromBack() {
        if (!this.head) {
            return null
        }
        if (!this.head.next) {
            this.head === null
        }
        let r = this.head;
        while (r.next.next) {
            r = r.next
        }
        r.next = null
    }

    // print the singly linked list
    printValues() {
        let runner = this.head
        let list = ""
        while (runner) {
            list += runner.value + "->"
            runner = runner.next
        }
        list += runner
        return list
    }

    moveMinToFront() {
        if (!this.head) {
            return "Empty list"
        }
        let min = this.head.value;
        let run = this.head;

        while (run) {
            if (run.value < min) {
                min = run.value
            }
            run = run.next
        }
        // let runTwo = this.head;
        // let temp = this.head.value;
        // while(runTwo){
        //   if(runTwo.value === min){
        //     this.head.value = min;
        //     runTwo.value = temp;
        //   }
        //   runTwo = runTwo.next
        // }
        let minNode;
        if (this.head.value === min) {
            return this
        }
        let runTwo = this.head;
        while (runTwo.next.value != min) {
            runTwo = runTwo.next;
        }
        minNode = runTwo.next;
        runTwo.next = runTwo.next.next


        let temp = this.head
        this.head = minNode;
        this.head.next = temp

        return this
    }

    moveMaxToBack() {
            if (!this.head) {
                return "Empty list"
            }
            let max = this.head.value;
            let run = this.head;
            let temp;
            while (run.next) {
                if (run.value > max) {
                    max = run.value
                }
                run = run.next
            }

            let maxNode;
            if (max == this.head.value) {
                maxNode = this.head;
                this.head = this.head.next;
            } else {
                let runner = this.head;
                while (runner.next.value != max) {
                    runner = runner.next;
                }
                maxNode = runner.next;
                runner.next = runner.next.next
            }

            let final = this.head;
            while (final.next) {
                final = final.next;
            }

            final.next = maxNode;
            maxNode.next = null;

            return this


        }
        // takes in a value and a location, add a node to the list with the input value BEFORE the given location
    prependValue(value, location) {
        if (!this.head) {
            return "Empty list!"
        }
        let prev = null;
        let cur = this.head;
        let count = 1;

        let newNode = new Node(value)
        while (cur && count <= location) {
            if (count === location) {
                prev.next = newNode;
                newNode.next = cur;
            }
            prev = cur
            cur = cur.next
            count++
        }
        return this
    }

    // takes in a value and a location, add a node to the list with the input value AFTER the given location
    appendValue(value, location) {
        if (!this.head) {
            return "List is empty";
        }
        let cur = this.head;
        let next = cur.next;
        let newNode = new Node(value)
        let count = 1
        console.log(count)
        while (next && count <= location) {
            if (count === location) {
                console.log(count)
                cur.next = newNode;
                newNode.next = next;
            }
            cur = next;
            next = next.next
            count++
            console.log(count)
        }
        if (count === location) {
            cur.next = newNode;
            newNode.next = next;
        }

        return this
    }


}

const sll = new SLList();
console.log(sll.addToFront(3))
console.log(sll.addToFront(2))
sll.addToFront(1)
sll.addToBack(4)
console.log(sll.addToBack(5))
console.log(sll.contains(5)) // prints true
console.log(sll.contains(6)) // prints false
console.log("==========================================")
sll.printValues()