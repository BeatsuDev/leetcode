int maxArea(int* height, int heightSize) {
    int i = 0;
    int j = heightSize-1;

    int largestSolution = 0;
    while (i < j) {
        int minHeight = height[i] < height[j] ? height[i] : height[j];
        int area = minHeight * (j-i);

        if (area > largestSolution) {
            largestSolution = area;
        }

        if (height[i] < height[j]) {
            i += 1;
        } else {
            j -= 1;
        }
    }

    return largestSolution;
}