class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int largestArea = 0;

        while (left < right) {
            int area = (right-left) * Math.min(height[left], height[right]);
            if (area > largestArea) largestArea = area;
            if (height[left] < height[right]) left++; else right--;
        }

        return largestArea;
    }
}
