---
layout: contentspage
title: Nikoli-Style Puzzles
permalink: /puzzles/oc-nikoli/
---

<a href="https://www.nikoli.co.jp/en/puzzles/">Nikoli</a> is a Japanese company that publishes pencil puzzles (Sudoku, Fillomino, Slitherlink, and Kakuro, to name a few of very many). Their logic puzzles have a worldwide audience, owing partly to their culture-independence: if you know how to count, you can understand the rules of pretty much any Nikoli puzzle (and sometimes you don't even need that!)

Nikoli-style puzzles are also very fun to design. Here I've collected some Nikoli-style puzzles that I've created.

<!--more-->

<h2 id="1">Hikkosu</h2>
Probably my favorite thing that I created for my CS Puzzles class -- Hikkosu is a brain-bending fusion of Shikaku and Numberlink style puzzles!

<center>
<b>Example Puzzles</b><br/>
<img src="/img/nikoli/Hikkosu-Example.png"><br/>
<a href="/img/nikoli/Hikkosu-Example-Solved.png">[Solution]</a>
<a href="/img/nikoli/Hikkosu-Joke.png">[For pros who don't need no stinkin' instructions]</a>*
</center>

<br/>

<center>
<b>Assets</b><br/>
<img src="/img/nikoli/Hikkosu-Assets.png"><br/>
If you'd like to make your own Hikkosu puzzles, here are the assets I used to make these.
</center>

<br/>

\*<small><em>You see, one of the lessons in our class involved us solving Nikoli puzzles whose instructions were in Japanese -- but since I know a fair amount of Japanese, the professor had to redact them... so, I decided to give him a taste of his own medicine :)</em></small>

<h2 id="2">Hikkosu Solver & Generator</h2>
If I didn't write a Hikkosu solver, nobody was going to.

<a href="/downloads/nikoli/Hikkosu-Solver.zip">[Download]</a>

Included in the download is:
<ul>
	<li>A portable installation of PyPy 3 for Windows (Mac and Linux distributions can be found at pypy.org). Running with PyPy is completely unnecessary, but probably advisable if you value your time.</li>
	<li>HikkosuSolver.py, a Python 3 program. Run with the command “HikkosuSolver.py filename.txt solve” to solve a puzzle, or “HikkosuSolver.py filename.txt generate” to generate a puzzle. Note that the file format is different for solving and generating.</li>
	<li>Three puzzle files containing the program-compatible versions of the included puzzles: easy.txt, medium.txt, and hard.txt</li>
	<li>Three generator files containing the input used to generate those files: gen_easy.txt, gen_medium.txt, and gen_hard.txt</li>
</ul>

<h2 id="3">Pillars</h2>
<em>Unfortunately, I can't seem to find who invented this style of puzzle -- it was somebody else in my Spring 2020 CS Puzzles class, I know that much! If you know who invented these, please get in touch.</em>

The rules of Pillars puzzles are as follows:
<ol>
	<li>Mark some tiles, leaving the rest empty.</li>
	<li>Some tiles have numbers in them. This corresponds to the number of marked tiles that tile can see (ie, the number of marked tiles in that tile's row or column).</li>
	<li>Tiles can see through marked and unmarked tiles, but cannot see through numbered tiles.</li>
	<li>You cannot mark tiles with a number in them.</li>
</ol>

<center>
<b>Example Puzzles</b><br/>
<em>(Note: These example puzzles were created by the inventor of Pillars, not by me!)</em>
<img src="/img/nikoli/Pillars-Example.png"><br/>
<a href="/img/nikoli/Pillars-Example-Solved.png">[Solution]</a>
</center>

<br/>

<center>
<b>Friendly Puzzles</b><br/>
<img src="/img/nikoli/Pillars-1.png"><br/>
<a href="/img/nikoli/Pillars-1-Solved.png">[Solution]</a>
</center>