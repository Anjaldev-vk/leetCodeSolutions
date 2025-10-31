/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
let uniqueNums1 = [...new Set(nums1)];
let uniqueNums2 = [...new Set(nums2)];

let arr = [...uniqueNums1, ...uniqueNums2];
    let ans=[];
    for (let i=0; i<=arr.length;i++){
        for (let j=i+1; j<=arr.length;j++){
            if(arr[i]==arr[j]){
                ans.push(arr[i])
            }
        }
    }
    return ans;
    
};