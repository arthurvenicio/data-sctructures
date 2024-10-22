/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    if(nums.length <= 0){
        return false;
    }

    var hashMap = new Map()

    for(let i = 0; i < nums.length; i++){
        if(hashMap.has(nums[i])){ // validate if numbers already is in hashmap
            var prevIdx =  hashMap.get(nums[i]) // get last value of times occurences
            if(i - prevIdx <= k){
                return true;
            }
        }

        hashMap.set(nums[i], i)
    }

    return false
    
};