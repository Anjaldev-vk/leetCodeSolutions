var removeDuplicates = function(nums) {
    const a = [...new Set(nums)];
    for (let i = 0; i < a.length; i++) {
        nums[i] = a[i];
    }
    return a.length;
};
