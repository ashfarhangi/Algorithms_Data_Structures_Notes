Data-Structures-and-Algorithms
==============================

This is the TLDR summary of two courses on Data Structures and Algorithms. I
summarized everything I learned from these materials.

I’ve included the code for each concept in Python. I would suggest to implement
this short code for your projects.

I highly recommend the following materials:

[Udacity nano degree: Data Structures and
Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256)

University of Central Florida Course: DESIGN & ANALYSIS ALGORITHMS 2019

Udacity nano degree notes for job interview

CLRS book for more in depth

UCF course for solving different challenges

Data Structures & Algorithms Nanodegree Program from Udacity A repository for
notes and projects

Course Objectives: Understanding of various types of techniques for algorithms
design and (run time) analysis in detail. Also, a gentle introduction to several
advanced data structures.

Course Overview: Review of mathematical background, sorting and searching,
algorithm design techniques such as divide and conquer, greedy approach, dynamic
programming, worst case and average case analysis techniques, data structures
such as binary search trees and various heaps, graph algorithms, string
algorithms and geometric data structures, advanced topics (P, NP, NP-Complete,
etc) if time permits.

Comparison
==========

Finding the smallest of n numbers:(n-1)  
Finding the biggest of n numbers:(n-1)  
Finding the smallest and the biggest of n numbers:(2n-3)

Problem Solving 101:
====================

![](media/807b5c8aee182baaa1713c01e98994f9.png)

Think in simple term:

1.  Don’t panic

2.  What are the inputs

3.  What are the outputs

4.  Solve the problem

Next :

Workout some examples, **relationship** between input, output, test cases.

How to solve the problem as a human. Then move to code. **On paper**.

Write algorithm. Pseudocode.

Dates, df, are all the inputs are valid?1st data 2nd Second date must not be
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

Big O Notion:
=============

As the input to an algorithm increases, the time required to run the algorithm
may also increase.

For example in Nested Loops:

For I in range:

For j in range:

Print(“hello World”)

Will increases the lines dramatically

The *rate of increase* of an algorithm is also referred to as the **order** of
the algorithm

For example, instead of saying "this relationship has a linear rate of
increase", we could instead say, "the *order* of this relationship is linear".

* O Notation*, and you'll see that the "O" in the name refers to the **o**rder
of the rate of increase.

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

**2. Binary Search:** O(log(n)+1) ( Why Name ? find a postion of binary)

Middle, Middle, Middle.
