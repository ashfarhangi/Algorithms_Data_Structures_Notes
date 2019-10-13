Data Structures and Algorithms
==============================

This is the summary of multiple materials on **Data Structures and Algorithms**.

I’ve included the code for each concept in Python. I would suggest to implement
this short code for your projects or coding interviews..

I highly recommend the following materials by the order of importance:

1.  [Udacity nano degree: Data Structures and
    Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256)

2.  Youtube playlist

3.  Data Structure in C book

4.  CLRS book [If you are an academic].

TLDR Objectives: Understanding of various types of techniques for algorithms
design and (run time) analysis in detail. Also, a gentle introduction to several
advanced data structures.

TLDR Overview: Review of mathematical background, sorting and searching,
algorithm design techniques such as divide and conquer, greedy approach, dynamic
programming, worst case and average case analysis techniques, data structures
such as binary search trees and various heaps, graph algorithms, string
algorithms and geometric data structures, advanced topics (P, NP, NP-Complete,
etc) if time permits.

Solving any algorithm problem:
==============================

![](media/807b5c8aee182baaa1713c01e98994f9.png)

Think in simple term:

1.  Don’t panic

2.  What are the inputs

3.  What are the outputs

4.  Solve the problem

**Next:**

Do some examples on paper/mind, find **relationship** between input and output,
finally, test some cases.

Try solve the problem **On paper first**.

Write algorithm. Pseudocode.

Example 1 [Code included]: Write an algorithm /code that counts the difference
of two dates.

Ask yourself:

Dates, DF, are all the inputs are valid? 1st data 2nd Second date must not be
older than 1: invalid input

How input are encoded? (yyyy,mm,dd)

Output return a number because we can do things with return value rather
printing it

![](media/aafcce2fa1d4355bed1f9c7f5850c437.png)

First code: writing a block that makes the solution to work. Solve with a single
simple case.

Break into simple parts so that we can see our progress.

Write simple small codes that work

No need to figure out all the details. Consider that you will procrastinate
later

Comparison
==========

Finding the smallest of n numbers:(n-1)  
Finding the biggest of n numbers:(n-1)  
Finding the smallest and the biggest of n numbers:(2n-3)

Big O Notion:
=============

As the input to an algorithm increases, the time required to run the algorithm
may also increase.

For example in **Nested Loops**:

For I in range:

For j in range:

>   Print(“hello World”)

Will increases the lines dramatically

The *rate of increase* of an algorithm is also referred to as the **order** of
the algorithm

For example, instead of saying "this relationship has a linear rate of
increase", we could instead say, "The *order* of this relationship is linear".

*O Notation*, and you'll see that the "O" in the name refers to the **o**rder of
the rate of increase.

Length of input to my function

O(2n+2) \> n=10 -\> 22

 In n\^2 + 5*n*2+5, the 55 has very little impact on the total
efficiency—especially as the input size gets larger and larger. Asking the
computer to do 10,005 operations vs. 10,000 operations makes little difference.
Thus, it is the n\^2*n*2 that we really care about the most, and the + 5+5 makes
little difference

Efficiency is actually about O(n) Interviewer wants us to think about
efficiency.

Run time analysis

O(3N) space efficiency (copying code)

Int , float 4 bytes

char 1 byte

TLDR: Binary search (Middle, Middle, O (log(n)).:
=================================================

![](media/393309480a114e09e85165f26cfdf15d.png)

**Algorithm:** Tricks to solve a problem

**Q:** How to find number 25 in this stack?

**A:**

**1. Linear search: O(n)**

**2. Binary Search:** O(log(n)+1) ( Why it is called binary search? find a
postion of binary)

Middle, Middle, Middle.

Sorting:
========

**Bubble sort:**

Simplest and most inefficient one O(n\^2)

Merge Sort(divide, merge):
==========================

Using divide and conquer, first, we divide 2 by 2

![](media/d60404983770ccf9700e87bf00057d26.png)

Then we compare the elements

![](media/aedaa435d36c4f0f3cbf29d50034fdd2.png)

Efficiency:

O (n Log (n))

Why we are seeing log (n) in our efficiency? Hint: same as binary search problem

QuickSort(divide, merge):
=========================

Pick one and move it around

![](media/efb964d97b2648ca21e04162697e01e1.png)

Why it can be chosen as the most efficient algorithm?

Because on average it will outperform merge sort.

On each step we are performing two moving around.

![](media/2aab5b68c0b0e7ea62486cfe66e08caa.png)

(Pivot = Last element) First move we move

1.  Select right P

2.  PL LS SP (Shift Pivot to left , Swap start and left)

3.  Compare Start with pivot. If (Start \> Pivot repeat step 2)

4.  Else move to second start

![](media/b41c1c2d2548c9e6940e3506ec84f34f.png)

![](media/4def5b724f6f15c6b099ce425f8c4e09.png)

I advise to practice this for cementing the algorithm.

![](media/4a3923fde43ff67cc4066b14626677b0.png)

**Great no need to move the original pivot anymore (2 is at the right place)**

![](media/c018057d901372ab5b57e93742036550.png)

Check 2 with lefts

New pivot on right. Compare

Moving phase

Everything less than 8 and 10 sweap results in:  
Everythin less than 8 are already below 8 so cemented

![](media/c018057d901372ab5b57e93742036550.png)

**Efficiency:**

**O(n2) if it’s already sorted. Why? Wasting time**

Technical Interview

![](media/4fe578f16ea7ad1e9fd04d71fdea444a.png)

What are 7 steps in every technical interview?

Heaps:
======
