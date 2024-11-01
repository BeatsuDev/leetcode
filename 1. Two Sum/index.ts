function twoSum(nums: number[], target: number): number[] {
    const seen = {};

    for (let i = 0; i < nums.length; i++) {
        const value = nums[i];
        if (target - value in seen) {
            return [seen[target - value], i];
        }
        seen[value] = i;
    }

    return [-1, -1];
}
