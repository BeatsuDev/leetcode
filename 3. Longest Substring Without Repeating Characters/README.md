# Longest Substring Without Repeating Characters

## Learning take-aways

Hashmaps where all keys will be just a single character can instead be stored in a 255 length array - no hashing required!

Avoid resetting/clearing data if you don't have to.

## Solving the task

Initialize an array of size $255$ with all values set to $-1$. This will be used as a lookup table where the value at index $char_{int}$ equal to the integer value of a character $char$ is the index at which $char$ last occurs.

> ![Visualization of a simple input and the state of the lookup table](media/image.png)
>
> Here is an example of how the lookup table looks like after adding all characters of the input into the lookup table.

We need two pointers (variables tracking indices of the input string). One ($left$) will denote the beginning index of a potential sequence of distinct characters and the other ($right$) that will iterate over all characters and check if they have been seen within the interval $[left,  right)$ of the input string. If the character at index $right$ lies outside of the interval $[left, right)$, we simply set the value at the index equal to the integer value of the character at $right$ to be the $right$ (see the figure drawing above) and then increment $right$. If the we have seen the character within the interval, we can move the left pointer to the index _after_ the index at which the duplicate character occured.
