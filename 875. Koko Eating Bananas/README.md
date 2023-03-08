# 875. Koko Eating Bananas
## Explanation
* Time Complexity: O(n*log(max(piles)))
* Space Complexity: O(1)

Some of the most common problems include:

* When to exit the loop? Should we use `left < right` or `left <= right` as the while loop condition?
```
In the problem, We only need to find minimum upper bound. We don't need to check when left equals to right.
```
* How to initialize the boundary variable left and right?
```
right = max(piles)
she eats all of them instead and will not eat any more bananas during this hour so the fastest way to finish eating bananas is max(piles).

left = 1
The slowest way to eat bananas is eating one banana per hour.

```
* How to update the boundary? How to choose the appropriate combination from `left = mid` , `left = mid + 1` and `right = mid`, `right = mid - 1`?
```
right = mid

In 875, we need to `Return the minimum integer k such that she can eat all the bananas within h hours.`
The upper bound (right) means that she can eat all. If we find a smaller number that can be feasible, we update the upper bound.
```
