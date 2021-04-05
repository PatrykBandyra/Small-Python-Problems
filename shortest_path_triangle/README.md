
It finds the shortest path in a triangle (between highest level node and lowest level nodes) stored in a .txt file in format as follows:
<pre>
     2
    4 9
   4 9 6
  7 7 8 9
 3 4 1 1 7
 </pre>
 
 You can only move down-left or down-right.
 
 I am using Dijsktra algorithm (not the most optimal way to do it). Its implementation is also not optimal - you have to specify destination node so our algorithm has to run
 as many times as there are nodes in the lowest level of a triangle.
