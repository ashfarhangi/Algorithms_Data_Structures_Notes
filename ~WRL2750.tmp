Data Structures and Algorithms
==============================

The summary of **Data Structures and Algorithms** plus every **Interview step.**

I’ve included the code for each concept in Python in the code folder. I would
suggest to implement this short code for your projects or coding interviews..

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

Binary search (Middle …. Middle, O (log(n)).:
=============================================

![](media/393309480a114e09e85165f26cfdf15d.png)

**Algorithm:** Tricks to solve a problem

**Q:** How to find number 25 in this a sorted array?

**A:**

**1. Linear search: O(n)**

**2. Binary Search:** O(log(n)+1) ( Why it is called binary search? find a
postion of binary)

Middle, Middle, Middle.

Sorting:
========

**Bubble sort:**

Simplest and most inefficient one O(n\^2)

Merge Sort (divide, merge):
===========================

Using divide and conquer, first, we divide 2 by 2

![](media/d60404983770ccf9700e87bf00057d26.png)

Then we compare the elements

![](media/aedaa435d36c4f0f3cbf29d50034fdd2.png)

Efficiency:

O (n Log (n))

Why we are seeing log (n) in our efficiency? Hint: same as binary search problem

Quick Sort (divide, merge):
===========================

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

Heaps:
======

Dynamic programming:
====================

(Programming == tables)

Factorial problem in python:

![](media/c75f1ae6443175cde6bff55aaa014eda.png)

DP = **Recursion** + **Memo**-ization

Knapsack problem: Max value for weight limit

![](media/8772bf182b4a29b45fa854704118a58d.png)

Knapsack. Imagine the skyrim world where you can carry a certain weight (50kg)
in your bag, how can you gather the most valuable items (3w,500v) with you?

How you optimize which items with their weights to carry with you?

1.  Brute force: Check all the solutions and pick the best one: O (2\^n)
    possible combinations. “exponential time”

Can we have a polynomial time algorithm? O(n\^2)

1.  Smarter approach: Initiate with smallest item (2, 6) then (5, 9). Note that
    (4, 6) will not be placed since for index 4 value 6 is larger than 5.

>   Next look at index 6. By combining smallest value (2, 6) + (4, 5) we get
>   higher value (11).

![](media/fb4c847451ca46a38339e5be359320a9.png)

>   Figure: For each weight the maximum value we can hold.  
>   Runtime is O(nW).

![](media/979a59ecbdab5b700013dbe7875b4603.png)

1.  Dynamic programming: {can you break into sub problems}

Sub-problem: Max value for some smaller weight

We start by using Base case ( so trivial to compute)

**Base case:** Smallest computation (compute values for one object)

**+**

**Lookup table** to store the trivial cases.

![](media/5a7c7e913b6193df10c1bd43504915d2.png)

![](media/fea061ac8378d67ca943d89b8a692000.png)

Longest common subsequent

![](media/dab72f2bab27818a10403e79984d290a.png)

![](media/1f11fb9b2ed3eb432764db5635531f54.png)

Technical Interview
===================

======= Greedy Algorithm (Best option at each step):
====================================================

![](media/44d46f063fca4872104e6edb1a26e63d.png)

ATM machine : 1,2,10,20,50,100\<

Return: n\$ the number of bills should be minimized

21\$ = 20 +1

N= 365 – (3x100)- (1x50)-(1x10) – (1x 5)

What about Target = 8?

Example:

Min operations example {see code}: By using while, in dividing numbers in half
// == / and using

Graph algorithm (data structure that shows relation):
=====================================================

Graph(Tree is a subgroup of graph,Network) Nodes(Vertex) Edges

![](media/d5e6c36b1d10faaaf0d1ae40e3182cca.png)

Directed (non-directed), Acyclic, Connectivity

Connectivity: You friends (social circle)

As seen below, the right graph is stronger. In contrast, the left group can be
dissolved if one of the connections drops.

![](media/4c958b1e2b2f2c7a5c54dc66945872db.png)

![](media/426dc47adbe8aa35d9ca78e2e77905be.png)

Go through array reccursavley.

![](media/9475b959311dc362995bdb778c55234b.png)

Let’s define 3 variables

![](media/9beca1381c793944285f552ff3a4842c.png)

Final answer we be the best solution out of these both (A[i] B[i] )

Technical Interview (CIOT BRCD) (cute bird)
===========================================

What are the most important 7 steps?

{Memory Palace} Imagine a cute bird sees a giant worm that is shaped like a Q
{Question}. First the bird pour water on the worm (clarify). Then it find the
tail and head (I, O). Then it will taste the worm (Test). It will use its brain
to decide how to eat it (Brainstorm). Then a big white eagle comes and its needs
to calculate the runtime of eating the worm {Runtime analysis}. Then it will
start eating it with If, For, {Code} and Debugs it (No more bug).

![](media/4fe578f16ea7ad1e9fd04d71fdea444a.png)

The context should be asking questions and brainstorm at first. As you go on you
rather than asking question everystep you must make statements and justify them.

{so we can have null input like [] Is that right?} { I have a feeling that it
might be useful in future steps}

Example: So it contains integers right? So Null input is another input that we
can have.

Q:  
A: Thanks it’s a pleasure to do interview with you. {Positive mindset} {Don’t
give up}

1.  **Clarifying the question {To prove you wont dive into the problem without
    learning more about it}**

Q: Given a 2D matrix of m, Just 0 and 1. Count the number of islands in the
matrix [island is a group of 1 or just 1 by itself.]

A: ok so, we are given a 2D matrix which will look something like this.:

[[1,0,1],[1,1,1]]

So, our goal is find the number of islands. Is the outcome the number? Or X? So
if the are connected (I[1,0,0],[0,1,0],[0,0,1]) diagonally? Does that consider
an island?

So what we supposed to do is to find the number of

{Just want to check Im solving the right problem…}

1.  Generating inputs and outputs:

>   So my input is matrix of 0 s, 1 s (Integers, strings? No)

>   Output: Integer (\# of islands) (1s or group of ones)

1.  Generating test cases:

>   {So just to test some cases {Special}}

>   {Can we get Is it ok we have }? Yes

Q: number of island in a matrix 

**1.Clarify the question **

A[[1,0,0]],[1,1,0]]{Just to make sure I’m solving the right problem….}

**2.Generating input/output**

\<\<\<\<\<\<\< HEAD 1. Generating input/output

Input matrix of integers 

Output integers ( number of islands 0- max{n}) 

1.  {Trick \#1 you can always answer the null case to interviewer.}{ I have a
    feeling that it might be useful in future steps} **Test cases** [**Edge
    cases**] [ Possible weird inputs that we have to handle A or none object 

{Null - empty- Write a code that doesnt crash}

1.  **Brainstorming** So if we have null, for sure we have 0 so there would be
    no islands in this case. ======= Input matrix of integers.Output integers
    (number of islands 0- max{n}) 

**3.Test cases**: {Trick \#1 you can always answer the null case to
interviewer.}{ I have a feeling that it might be useful in future steps} **Test
cases** [**Edge cases**] [ Possible weird inputs that we have to handle A or
none object.

{Null - empty- Write a code that doesnt crash}

**4.Brainstorming:** {Variables that needs to initialized} {so I need to track
X} {And keep tracking} {Runtime error} {Data structure brainstorm algorithms and
data structures} {Represent graph DFS problem} So if we have null, for sure we
have 0 so there would be no islands in this case. \>\>\>\>\>\>\>
600e13278473db6cc40a022e79c37c0e0baa2b56

But also we can have this as input (the input she wants)   {So what I am
thinking here} is start at the first element . So i need a counter **variable**
and I **initialze** it there. And **increment** it by 1.

We get to Zero. Thats not part of any island so I need to keep track of X.
Hmmmm. Maybe I can look at the elements on top and bottom and check if they are
on the same island and keep track of it. Since there is no above that. We get a
run time error. Maybe it could a case of data structure we can solve this. {This
might be a breath first search problem. I can look at the elements around it.
**Set to mark** as **visited** and **keep going**

**If you are stuck?** This represent a type of data structure and algorithm .
Merge sort maybe… Keep talking

**5. Runtime anaylsis **

When I’m looking all the elements in matrix I’m looking at them atlease once so
I’m thinking the runtime would be nXm where N is the number of rows and M is the
number of columns. Well it seems like the optimal solution. So i think i start
and jump on coding now.

**6.Coding**

So I’m calling my mainfunction islandCounter():

Variable a,b,c If() While() For()

**7.Debugging**

Test cases: input None -\> return 0 so its working

So [[1,0,1],[1,1,0]]. Go ahead, that looks good. Now I’m adding both of these.
And I probably {} O looks like I forget to {add a return} Looks like it works.

Python programming:
===================

\<\<\<\<\<\<\< HEAD while(len(q)!= 0):

**6. Debug:**

And run it by

{oh looks like I forget to}

Looks like it works.

![](media/28a37a2c4d8794faa0b22686c21cbece.png)

\>\>\>\>\>\>\> 600e13278473db6cc40a022e79c37c0e0baa2b56
