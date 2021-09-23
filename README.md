# Searching And Sorting
It's just the collections of Search Functions and Bubble Sort &amp; Selection Sort  

Searching
Searching means to find out whether a particular element is present in a given sequence or not. There are commonly two types of searching techniques:

● Linear search (We have studied about this in A​ rrays and Lists)​

● Binary search

In this module, we will be discussing binary search.
Binary Search
Binary Search is a searching algorithm for finding an element's position in a sorted array. In a nutshell, this search algorithm takes advantage of a collection of elements of being already sorted by ignoring half of the elements after just one comparison.
Prerequisite:​ 
Binary search has one pre-requisite; unlike the linear search where elements could be any order, the array in ​binary search​ must be sorted,

The algorithm works as follows:
1. Let the element we are searching for, in the given array/list is X.
2. Compare X with the middle element in the array.
3. If X matches with the middle element, we return the middle index.
4. If X is greater than the middle element, then X can only lie in the right (greater)
half subarray after the middle element, then we apply the algorithm again for
the right half.
5. If X is smaller than the middle element, then X must lie in the left (lower) half,
this is because the array is sorted. So we apply the algorithm for the left half.




