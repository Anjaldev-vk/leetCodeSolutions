/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let m=0;
    for (let sentence of sentences){
        let count=sentence.split(' ').length;
        m=Math.max(m,count);
    }
    return m;
};