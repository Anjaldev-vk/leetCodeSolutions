var canAliceWin = function(nums) {
    let sum1 = 0 , sum2 = 0;
    for(let i =0;i<nums.length;i++){
        if(nums[i] < 10){
           sum1 += nums[i];
        }else{
            sum2 += nums[i];
        }
    }
    if(sum1 !== sum2) return true;
    else return false;
};