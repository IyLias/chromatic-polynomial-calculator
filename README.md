# Chromatic-Polynomial-Calculator

This is a Calculator that calculates chromatic polynomial of arbitrary graph $G$.

<br>

## Introduction 

The field of graph coloring is filled with NP-complete problems, which may seem simple and straightforward in the problems themselves, 
but proving them mathematically is extremely difficult. To understand deeply chromatic number and chromatic polynomial of graphs, 
I studied Fundamental Reduction Theorem: FRT and implemented chromatic calculator.




<br><br>

## Fundamental Reduction Theorem : FRT

Fundamental Reduction Theorem :FRT is one of methods for calculating chromatic polynomial of graph $G$. 
There exists two types of FRT: Extension version and Subtraction version. The first one is the Extension version. 

<img src="https://github.com/IyLias/chromatic-polynomial-calculator/assets/48081162/82b487c4-4e08-407d-b3d0-965877a3db07">
<br><br>

We can view the equation of FRT in a different way. Let $H = G + xy$. Then $G = H − xy$ and
$H • e = G • e$. Substituting $H$ to $G$ leads to new form of FRT : Subtraction version.


<br>
<img src="https://github.com/IyLias/chromatic-polynomial-calculator/assets/48081162/fbc43264-7360-4be1-a2fa-ba1f53e48f85" >


<br><br>

Since we know chromatic polynomial of $O_n$ and $K_n$, 
($P(O_n,\lambda)=\lambda^n$ and $P(K_n,\lambda) = \lambda(\lambda-1)(\lambda-2)...(\lambda-n+1) = \lambda^{\underline{n}}$), 
FRT makes possible to get chromatic polynomial of arbitrary graphs.




<br><br>

## Pseudocode of FRT 

Since the form of FRT is defined recursively, we can write it as codes. Here's the pseudocode of FRT to get $P(G,\lambda)$.

<br>
<img src="https://github.com/IyLias/chromatic-polynomial-calculator/assets/48081162/8fa4a791-b030-4a73-a74b-d9d38c9a7cb0" >

<br>

The FRT function has 3 inputs, target graph $G$, density and level. <br><br>

The density is a value which shows how dense graph G is, i.e, $density = \frac{2m}{n(n−1)}$ where $n = |V (G)|$ and $m = |E(G)|$. The level is current
level of FRT extension tree.

<br>

There are 2 ideas we should take a look. First one is the exit conditions. It has basically 2 conditions,
$O_n$ and $K_n$ in a naive way. To search faster we need more chromatic polynomial of specific graphs. In
this pseudocode, we added cycle graph $C_n$ and tree $T_n$. To improve its performance even better, we
may add more chromatic polynomial of G by using $K_r$-gluing ideas, which we will examine later.

<br>

The remaining idea is about density. In the pseudocode, we divided two cases based on whether density
value is greater than 0.5 or not. When density value is greater than 0.5, then it means $G$ is relatively
close to complete graph. Thus using extension version of FRT is definitely better than subtraction
version of FRT. On the other hand, when density value is less than 0.5, then $G$ is relatively close to
empty graph and it’s better to use subtraction version of FRT in this case.




<br><br>

## Implementation

Based on this psudocode, I implemented a program for calculating chromatic polynomial of arbitrary graph $G$ with python. 
This program has 2 major features, calculating chromatic polynomial of given graph G and show its process visually with a tree structure by using matplotlib.

<br>
<img src="https://github.com/IyLias/chromatic-polynomial-calculator/assets/48081162/1de7c297-4a1a-4cfc-90c4-e7ccc59aacf3" width="70%" height="70%">
<br>
Visualization of FRT process with tree structure

<br><br><br>
<img src="https://github.com/IyLias/chromatic-polynomial-calculator/assets/48081162/3644c76e-3dab-4acd-bf70-7a8a1344d309" width="75%" height="75%">

Calculation of chromatic polynomial of $G$



<br><br>

## References

[1] Russell Merris, Graph Theory (2001), 21-33. <br>

[2] Ronald C. Read, An Introduction to Chromatic Polynomials (1968), 1-20. <br>

[3] F. M. Dong, K. M. Koh, K. L. Teo, Chromatic Polynomials and Chromaticity of Graphs (2005),
1-13, 55-62.
