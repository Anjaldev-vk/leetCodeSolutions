let returnToBoundaryCount = function(nums) {
    let position=0;
    let count=0;
    for (let move of nums) {
        position += move;
        if (position === 0) {
            count++;
        }
    }

    return count;
};