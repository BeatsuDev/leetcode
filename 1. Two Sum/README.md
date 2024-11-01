# Two sum

## Learning take-aways

Identify when your code iterates over the same elements several times. In this case, using a hash map to store the elements we already have iterated over once allows us to perform constant time lookups instead of linear searches with repeated accesses every time.

## Solving the task

For any number `x` there exists a corresponding number `c` that together sums up to the target value `target`. This value is `c = target - x`, (re-arranged from `x + c = target`). Stated in the task description, there exists exactly one such pair `(x, c)` where `x ∈ input_array` and `c ∈ input_array` that sums up to `target`.

One solution to find this pair would be to iterate over the whole array. For each number `x` in the array, iterate over the previous numbers up to the index of `x`, `xᵢ`. For every number `c` up to `xᵢ`, check if `x + c = target`. If it does, we have found the pair.

For every value `x` at index `xᵢ` up to the length of the input array `n`, this solution performs `xᵢ` operations, linearly searching through the previously seen numbers. This totals to $\frac{n(n-1)}{2}$ operations, or a total time complexity of $O(n^2)$.

Instead of linearly searching through the previously seen numbers, we can add the numbers we see to a hash map as we go along. The benefit of this is that hash maps offer constant $O(1)$ lookup times, as well as constant time to add elements. We use a hash map instead of a hash set so that we can store the index at which the number occurs, since the task asks us to return the indices of the two elements that sum to target, not the values.

Initialize a hash map `seen`, then iterate over the input array. For each number `x`, check if the complement number `c` has already been added to `seen`. If it has, then we have found the pair. Finally set the value at key `x` of `seen` to the current index (`seen[x] = index`).
