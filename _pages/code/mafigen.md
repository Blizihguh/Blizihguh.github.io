---
layout: page
title: MafiGen
permalink: /code/mafigen/
---

<script>
	const ROLES = JSON.parse('[{ "Investigator": { "Type": "TI", "Value": 2 }, "Tracker": { "Type": "TI", "Value": 1 }, "Voyeur": { "Type": "TI", "Value": 1 }, "Gunsmith": { "Type": "TI", "Value": 2 }, "Doctor": { "Type": "TP", "Value": 2 }, "Bodyguard": { "Type": "TP", "Value": 1 }, "Wizard": { "Type": "TP", "Value": 1 }, "Jailor": { "Type": "TP", "Value": 1 }, "Socialite": { "Type": "TC", "Value": 1 }, "Lumberjack": { "Type": "TC", "Value": 2 }, "Psychic": { "Type": "TC", "Value": 2 }, "Hotelier": { "Type": "TC", "Value": 1 }, "Vigilante": { "Type": "TR", "Value": 2 }, "Grave Robber": { "Type": "TR", "Value": 1 }, "Motivator": { "Type": "TR", "Value": 1 }, "Annoying Child": { "Type": "TR", "Value": 2 }, "Coroner": { "Type": "TR", "Value": 1 }, "Journalist": { "Type": "TR", "Value": 2 }, "Enforcer": { "Type": "Scum", "Value": -1 }, "Roleblocker": { "Type": "Scum", "Value": -2 }, "Stalker": { "Type": "Scum", "Value": -2 }, "Bus Driver": { "Type": "Scum", "Value": -2 }, "Strongman": { "Type": "Scum", "Value": -2 }, "Spy": { "Type": "Scum", "Value": -1 }, "Capo": { "Type": "Scum", "Value": -1 }, "Shapeshifter": { "Type": "Scum", "Value": -2 }, "Poisoner": { "Type": "Scum", "Value": -1 }, "Oracle": { "Type": "Scum", "Value": -1 }, "Minion": { "Type": "Scum", "Value": 0 } }]')[0];
	const TI_ROLES = [];
	const TP_ROLES = [];
	const TC_ROLES = [];
	const TOWN_ROLES = [];
	const SCUM_ROLES = [];

	// Sort roles into their categories for ease of access
	for (let key in ROLES) {
		if (ROLES[key]["Type"] == "TI") {
			TI_ROLES.push(key);
			TOWN_ROLES.push(key);
		}
		else if (ROLES[key]["Type"] == "TP") {
			TP_ROLES.push(key);
			TOWN_ROLES.push(key);
		}
		else if (ROLES[key]["Type"] == "TC") {
			TC_ROLES.push(key);
			TOWN_ROLES.push(key);
		}
		else if (ROLES[key]["Type"] == "TR") {
			TOWN_ROLES.push(key);
		}
		else if (ROLES[key]["Type"] == "Scum" && key != "Minion") {
			SCUM_ROLES.push(key);
		}
	}

	function handle(e) {
		if (e.keyCode === 13) {
			generate();
		}
	}

	function shuffleArray(array) {
		for (var i = array.length - 1; i > 0; i--) {
			var j = Math.floor(Math.random() * (i + 1));
			var temp = array[i];
			array[i] = array[j];
			array[j] = temp;
		}
	}

	function choose(arr) {
		return arr[Math.floor(Math.random()*arr.length)];
	}

	function validateScores(setup) {
		let sum = 0;
		for (var i = 0; i < setup.length; i++) {
			sum = sum + ROLES[setup[i]]["Value"];
		}

		if ( (setup.length == 9 && sum > 6 && sum < 10) || (setup.length > 9 && sum > 7 && sum < 11) ) {
			return sum;
		}
		return 0;
	}

	function generate() {
		let playerList = document.getElementById("playerString").value.split(",");
		// Prune whitespace from start and end of player names
		for (var i = 0; i < playerList.length; i++) {
			playerList[i] = playerList[i].trim();
		}

		let playerCt = playerList.length;
		let foundSetup = false;

		if (playerCt < 9 || playerCt > 12) {
			console.log("Bad size");
			return
		}

		while (!foundSetup) {
			// Generate necessary town roles
			let setup = [];
			setup.push(choose(TI_ROLES));
			if (playerCt == 9) {
				setup.push(choose(TOWN_ROLES));
			}
			else {
				setup.push(choose(TI_ROLES));
				setup.push(choose(TP_ROLES));
				setup.push(choose(TC_ROLES));
			}
			// Get distinct scum roles
			let scum1 = choose(SCUM_ROLES);
			while (playerCt == 9 && scum1 == "Poisoner") {
				scum1 = choose(SCUM_ROLES);
			}

			let scum2 = choose(SCUM_ROLES);
			while (scum2 == scum1 || (playerCt == 9 && scum2 == "Poisoner")) {
				scum2 = choose(SCUM_ROLES);
			}
			setup.push(scum1);
			setup.push(scum2);
			if (playerCt > 11) {
				let scum3 = choose(SCUM_ROLES);
				while (scum3 == scum1 || scum3 == scum2) {
					scum3 = choose(SCUM_ROLES);
				}
				setup.push(scum3);
			}
			// If it's an 11 player game, add a minion
			if (playerCt == 11) {
				setup.push("Minion");
			}
			// Fill rest of town with random roles
			while (setup.length < playerCt) {
				setup.push(choose(TOWN_ROLES));
			}

			shuffleArray(setup);
			shuffleArray(playerList);

			let sum = validateScores(setup)
			if (sum > 0){
				// Log setup to console and end while loop
				foundSetup = true;

				// Sort setup for display
				let townRoles = [];
				let townPlayers = [];
				let scumRoles = [];
				let scumPlayers = [];

				// Get TI and full scum at the top
				for (var i = 0; i < setup.length; i++) {
					if (ROLES[setup[i]]["Type"] == "TI") {
						townRoles.push(setup[i]);
						townPlayers.push(playerList[i]);
					}
					else if (ROLES[setup[i]]["Type"] == "Scum" && setup[i] != "Minion") {
						scumRoles.push(setup[i]);
						scumPlayers.push(playerList[i]);
					}
				}
				// Get TP and Minion next
				for (var i = 0; i < setup.length; i++) {
					if (ROLES[setup[i]]["Type"] == "TP") {
						townRoles.push(setup[i]);
						townPlayers.push(playerList[i]);
					}
					else if (setup[i] == "Minion") {
						scumRoles.push(setup[i]);
						scumPlayers.push(playerList[i]);
					}
				}
				// Get TC
				for (var i = 0; i < setup.length; i++) {
					if (ROLES[setup[i]]["Type"] == "TC") {
						townRoles.push(setup[i]);
						townPlayers.push(playerList[i]);
					}
				}
				// Finally, get TR
				for (var i = 0; i < setup.length; i++) {
					if (ROLES[setup[i]]["Type"] == "TR") {
						townRoles.push(setup[i]);
						townPlayers.push(playerList[i]);
					}
				}

				// Display setup
				let townList = document.getElementById("townies");
				let scumList = document.getElementById("scummies");
				townList.innerHTML = "";
				scumList.innerHTML = "";
				
				for (var i = 0; i < townRoles.length; i++) {
					// Get color for role
					let openColor = '<div style="color:#119fef">'; // TR
					if (ROLES[townRoles[i]]["Type"] == "TI") { 
						openColor = '<div style="color:#f7dc13">'; 
					}
					else if (ROLES[townRoles[i]]["Type"] == "TP") { 
						openColor = '<div style="color:#68da0d">'; 
					}
					else if (ROLES[townRoles[i]]["Type"] == "TC") { 
						openColor = '<div style="color:#11efbd">';
					}
					// Display role
					townList.innerHTML += openColor + townPlayers[i] + " <small>(" + townRoles[i] + ") (" + ROLES[townRoles[i]]["Value"] + ")</small></div>";
				}

				for (var i = 0; i < scumRoles.length; i++) {
					let openColor = '<div style="color:red">';
					if (scumRoles[i] == "Minion") { openColor = '<div style="color:orange">'; }
					scumList.innerHTML += openColor + scumPlayers[i] + " <small>(" + scumRoles[i] + ") (" + ROLES[scumRoles[i]]["Value"] + ")</small></div>";
				}
			}
		}

		return false;
	}
</script>

Player List: <input type="text" id="playerString" style="width: 500px;"> <em>(Separate players with commas)</em>
<br/>
<input type="button" onclick="generate()" value="Generate Setup">
<script>document.getElementById("playerString").value = "Alice, Bob, Carol, David, Eve, Fazil, Grace, Horace, Ib, John, Kyoko, Larry";</script>

<div class="row">
  <div class="townColumn"><h2>Town:</h2><h4 id="townies"></h4></div>
  <div class="scumColumn"><h2>Scum:</h2><h4 id="scummies"></h4></div>
</div> 

<style>
	.townColumn {
	  float: left;
	  width: 50%;
	}

	.scumColumn {
		float: left;
		width: 50%;
	}

	/* Clear floats after the columns */
	.row:after {
	  content: "";
	  display: table;
	  clear: both;
	}
</style>