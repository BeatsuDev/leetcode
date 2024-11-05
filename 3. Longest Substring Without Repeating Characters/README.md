# Longest Substring Without Repeating Characters

## Learning take-aways

Hashmaps where all keys will be just a single character can instead be stored in a 255 length array - no hashing required!

Avoid resetting/clearing data if you don't have to.

## Solving the task

Assume the longest sequence of unique characters begins at the start of the string until we find a character at index $j$ that matches with a previous character in the string at index $i$. After that we check for a longer unique sequence starting at $i+1$. We know that any index before $i$ can not have a longer distinct sequence of characters than $j-i$ because any longer sequence than the one we have already found would include the characters at index $j$ and $i$ (which are duplicates) within them.

> ```
>  z a b c d e a f
>    i         j
> |---- L ----|
> ```
>
> If the range $L$ is any larger, the duplicates $i$ and $j$ will be included in the range and will not be valid. We have already checked for duplicates in all characters in the range $L$, so we know that there are no duplicates after $i$ up to and including $j$. That's why we can move the start of range $L$ to $i+1$ and then continue moving the end of $L$ from where it is.
