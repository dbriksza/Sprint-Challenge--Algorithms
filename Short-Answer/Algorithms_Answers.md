#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n) the function only has to run once to determine the value of a

b)
0(n^2) the function has to run n^2 number of times because of the nested loops

c)
O(n) the function only has to run once to determine the amount bunny ears

## Exercise II

To find how tall an egg could be dropped from a building, you can start at the first floor, drop an egg, if it breaks, you found the answer. If it doesn't break, you move up to the next floor and drop it. Repeat until it breaks. I suspect this would be the best method since eggs probably can't be dropped from too high. This would have a runtime of O(n). If for some reason you expected the eggs to survive a fall from many stories, you could start from the middle floor, drop, and move halfway up or down from there depending on the result. This would have a runtime of O(log n).
