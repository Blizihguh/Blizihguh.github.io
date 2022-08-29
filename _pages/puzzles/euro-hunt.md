---
layout: page
title: Puzzle Hunt - Escape from Europe
permalink: /puzzles/europe-hunt/
description: A puzzle hunt that I helped make. Do YOU have what it takes to escape from Europe?
embedimage: /img/embeds/hunt-penguin.png
---

This is a puzzle hunt that some friends and I made for a class we took. Created in April of 2020, it concerns the main thing that happened in April of 2020. To wit:

You were having a wonderful time in Europe, enjoying your nice rest after a long day of sightseeing, when all of a sudden, you received a ton of calls from your family. It turns out travel to and from Europe was banned... Well, now you must rush home at 3 A.M. before it’s too late.

<script>
	function hashCode(str) {
	    let hash = 0;
	    for (let i = 0, len = str.length; i < len; i++) {
	        	let chr = str.charCodeAt(i);
	        	hash = (hash << 5) - hash + chr;
	        	hash |= 0; // Convert to 32bit integer
	    	}
	    	return hash;
	}

	function check() {
		let guess = document.getElementById("answerBox").value.toUpperCase();
		let result = hashCode(guess);
		var answers = {
			2107639663: "Memories Are Tmporary",
			"-1650708450": "What Are Birds?",
			2066130074: "Nikoli Nonsense",
			"-1728924016": "Musical Mayhem",
			"-1929151380": "It's All Latin To Me",
			"-251332817": "Nerd Search",
			"-273684309": "More Nikoli Nonsense",
			2136327331: "RIT Recollections",
			"-2056535537": "Metapuzzle",
			2537619: "the bonus puzzle"
		};
		if (answers[result]) {
			document.getElementById("result").innerHTML = "Result: SUCCESS! You have solved " + answers[result] + "!";
		}
		else {
			document.getElementById("result").innerHTML = "Result: Invalid answer :(";
		}
	}
</script>

Answer Checker: <input type="text" id="answerBox" style="width: 100px;"> <input type="button" onclick="check()" value="Check answer"> <b id=result>Result: --</b>
<br/>
<em>(Type in the answer to a puzzle here to see if it's correct. Answers should contain no spaces or punctuation. You don't need to specify which puzzle it's for; the computer knows all.)</em>
<br/>


If you've given up on a puzzle and wish to spoil yourself, you can find individual solutions <a href="/puzzles/europe-hunt-solutions/">here</a>. Each solution is spoilered individually, so you shouldn't accidentally see the solutions for puzzles you're still working on.

<center>
<a href="/img/euro-puz-hunt/puz01.png"><h2 id="1">Memories Are Tmporary</h2></a>
<em>Unfortunately, the second half of this puzzle relies on you having access to RIT's CS lab servers, which is probably not the case, statistically speaking. Also, it relies on some files I put in the temp directories on those servers still being there, which is also unlikely. So, even though it was the coolest part of the puzzle, you'll have to skip it. Once you've solved the crossword, you can find the rest of the puzzle <a href="/downloads/euro-puz-hunt/">here</a>.

<center>
<a href="/img/euro-puz-hunt/puz02.png"><h2 id="2">What Are Birds?</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz03.png"><h2 id="3">Nikoli Nonsense</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz04.png"><h2 id="4">Musical Mayhem</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz05.png"><h2 id="5">It's All Latin To Me</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz06.png"><h2 id="6">Nerd Search</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz07.png"><h2 id="7">More Nikoli Nonsense</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz08.png"><h2 id="8">RIT Recollections</h2></a>
</center>
<em>Despite being RIT-themed, this one is completely solvable with public information; no need to access any lab computers or anything.</em>

<center>
<a href="/img/euro-puz-hunt/puz09.png"><h2 id="9">Metapuzzle</h2></a>
</center>

<center>
<a href="/img/euro-puz-hunt/puz-bonus.png"><h2 id="10">Bonus Puzzle</h2></a>
<em>This doesn't factor into the meta puzzle at all. Just another puzzle we thought of at the last minute, and, well, we couldn't help ourselves.</em>
</center>