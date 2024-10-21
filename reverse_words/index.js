/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let spplited = s.split(" ")
    let simpleArray = []

    for(item of spplited){
        simpleArray.push(item.split("").reverse().join(""))
    }

    return simpleArray.join(" ")
};


console.log(reverseWords("Let's take LeetCode contest"))