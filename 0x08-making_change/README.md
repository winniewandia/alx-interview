Sort the array of coins in decreasing order.
Initialize ans vector as empty.
Find the largest denomination that is smaller than remaining amount and while it is smaller than the remaining amount:
Add found denomination to ans. Subtract value of found denomination from amount.
If amount becomes 0, then print ans.