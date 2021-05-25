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
        // remove the second to last item in the list
    removeSecondToLast() {
        if (!this.head || !this.head.next) {
            return "Nothimg to remove"
        }

        let counter = 0;
        let cur = this.head;
        while (cur) {
            cur = cur.next;
            counter++
        }
        let run = this.head;
        counter = counter - 2 - 1;
        while (counter > 0) {
            counter--
            run = run.next
        }
        run.next = run.next.next;
        return this
    }

    // remove all nodes that have a negative value
    removeNegatives() {
        if (!this.head) {
            return "Empty"
        }
        let cur = this.head;
        let next = cur.next
        while (this.head && this.head.value < 0) {
            this.head = this.head.next;
        }
        while (next) {
            if (next.value < 0) {
                cur.next = next.next;
                if (cur.next) {
                    next = cur.next.next;
                } else {
                    next = null;
                }
            } else {
                cur = next;
                next = next.next;
            }
        }
        if (cur.next.value < 0) {
            this.removeFromBack()
        }
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


class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

// a queue operates on the principal of "First In, First Out" like waiting in line for something
class SLQueue {
    constructor() {
        this.head = null
        this.tail = null
    }

    // add a node with the given value to the queue
    enqueue(value) {
        let newNode = new Node(value)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode;
            this.tail = this.tail.next;
        }
        return this
    }

    // remove and return the front value from the queue
    dequeue() {
        if (!this.head) {
            return "queue is empty, nothing to remove!!!"
        } else {
            let oldHead = this.head.value;
            this.head = this.head.next;
            return oldHead
        }


    }

    //return true/false based on whether you find the given value in a queue
    contains(value) {
        if (!this.head) {
            return "queue is empty!!!"
        }
        let runner = this.head;
        while (runner) {
            if (runner.value === value) {
                return true;
            }
            runner = runner.next
        }
        return false;
    }

    // remove the minimum value in the queue (remember your edgecases and pointers!)
    removeMin() {
        if (!this.head) {
            return "queue is empty, nothing to remove!!!"
        } else {
            let min = this.head.value;
            let runner = this.head;
            while (runner) {
                // console.log(min)
                if (runner.value < min) {
                    min = runner.value;
                }
                runner = runner.next;
            }
            if (this.head.value === min) {
                this.head = this.head.next;
            } else {
                let first = this.head;
                let next = first.next
                while (next.value !== min) {
                    first = next;
                    next = next.next;
                }
                first.next = next.next;
                this.tail = next.next;
            }

        }
        return this
    }

    printQ() {
        let str = "";
        let r = this.head;
        while (r) {
            str += " " + r.value + " "
            r = r.next;
        }
        return str
    }
    interleaveQueue(queue) {
            if (!this.head) {
                return "Empty"
            }
            let len = 0;
            let runner = this.head
            while (runner) {
                runner = runner.next;
                len++;
            }
            let counter = len
            let arr = []
            let r = this.head;
            while (r && counter != 0) {
                arr.push(r.value)
                r = r.next;
                counter--
            }

            let mid = Math.ceil(len / 2)
            let first = 0;
            let second = mid
            let node = this.head;
            while (first <= mid && second < arr.length || node) {
                if (second === arr.length && first < mid) {
                    node.value = arr[first]
                    break
                }
                node.value = arr[first]
                node.next.value = arr[second];
                node = node.next.next;
                first++
                second++
            }
            // console.log(this.head.value)
            // console.log(this.tail.value)
            return this
        }
        // given a queue, determine whether or not the values therein are a pallindrome 
        // Ex: 1 --> 2 --> 3 --> 2 --> 1 --> null
        // any values that are in the same order going forwards as backwards is a pallindrome, doesn't need to just be letters
    isPallindromeWithArr() {
        let arr = []
        let run = this.head;
        while (run) {
            arr.push(run.value)
            run = run.next
        }
        let i = 0;
        let j = arr.length - 1;
        while (i < j) {
            if (arr[i] != arr[j]) {
                return false
            }
            i++;
            j--;
        }
        return true;
    }

    size() {
        if (!this.head) {
            return 0
        }
        let s = 0;
        let r = this.head;
        while (r) {
            s++;
            r = r.next;
        }
        return s;
    }

    isPallindrome() {
        let arr = [];
        let r = this.head;
        let counter = Math.ceil(this.size() / 2)
        while (counter) {
            arr.push(r.value);
            this.dequeue()
            r = r.next;
            counter--;

        }
        let node = this.head;
        let j = 0;
        while (node && j < arr.length) {
            // console.log(arr[j], node.value)
            if (arr[j] != node.value) {
                return false;
            }
            j++;
            node = node.next;
        }
        return true;



    }


}

const queue = new SLQueue();
queue.enqueue(5)

queue.enqueue(15)
queue.enqueue(3)
    // queue.contains(5)
    // queue.dequeue()

queue.removeMin()
queue.printQ()

class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

// a stack operates on the principal of "First In, Last Out" like waiting in line for something
class SLStack {
    constructor() {
        this.top = null
    }

    // add a given value to your stack
    push(value) {
            if (!this.top) {
                this.top = new Node(value)
            } else {
                let newNode = new Node(value)
                newNode.next = this.top;
                this.top = newNode
            }
        }
        // remove and return the top value
    pop() {
        this.top = this.top.next
    }

    // return (don't remove) the top value of a stack
    topValue() {
        return this.top.value
    }

}

let stack = new SLStack()
stack.push(1)
stack.push(2)
stack.push(3)
console.log(stack)
stack.pop()
console.log(stack)
stack.topValue()


function n(num) {
    if (num === 1) {
        return 1
    }
    return num + n(num - 1)
}

console.log(n(5))

// Write a drecursive function that, given a number, returns the product of integers up to a given number
// Ex: given 4 would return 1*2*3*4 == 24
// Ex: given 2.5 would return 1*2 == 2 

function recursiveFactorial(num) {
    if (num === 1) {
        return 1
    }

    return num * recursiveFactorial(num - 1)
}

console.log(recursiveFactorial(2, 5))