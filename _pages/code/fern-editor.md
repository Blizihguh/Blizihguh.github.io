---
layout: page
title: Fern Editor
permalink: /code/fern/
description: Pimp your glamour!
embedimage: /img/embeds/fern.png
---

<!-- HTML -->
<input type="button" onclick="render()" value="Generate Preview">
<div class="row">
  <div class="imgColumn"><canvas id="canvas" width="86" height="64"></canvas></div>
  <div class="buttonsColumn">
  	<div id="buttons-div">
  		Sleeve: <input type="text" id="color0" style="width: 500px;">
  	</div>
  </div>
</div> 
<canvas id="buffer" class="debug" width="86" height="64"></canvas>

<script>
	const MASKS = ["https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_00.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_01.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_02.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_03.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_04.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_05.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_06.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_07.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_08.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_09.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_10.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_11.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_12.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_13.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_14.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_15.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_16.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_17.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_18.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_19.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_20.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_21.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_22.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_23.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_24.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_25.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_26.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_27.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_28.png",
				   "https://github.com/Blizihguh/blizihguh.github.io/raw/master/img/fern/fern_mask_29.png"];

	const COLORS = ["#3E8084", "#FF9F26", "#C47922", "#315259", "#8A541E", "#CFA06B", "#0E050F", "#302722", "#0E050F", "#20303D", 
					"#431F19", "#DD8B36", "#FCC477", "#3F2C1C", "#A18F7B", "#F2E6BD", "#1B1716", "#315259", "#182126", "#626D60", 
					"#20303D", "#C0BEA7", "#502E1B", "#191919", "#7D4C27", "#DF8D2F", "#885326", "#1D0E18", "#000000", "#000000"];

	var canvas = null;
	var ctx = null;
	var buffer = null;
	var btx = null;

	var foo = 0;

	function init() {
		canvas = document.getElementById("canvas");
		ctx = canvas.getContext("2d");

		buffer = document.getElementById("buffer");
		buffer.width = canvas.width;
		buffer.height = canvas.height;
		btx = buffer.getContext("2d");

		render();
	}

	function render() {
		clear_canvas();
		for (var i=0; i<30; i++) {
			get_layer_in_buffer(i);
			draw_layer_from_buffer();
		}
	}

	function get_layer_in_buffer(idx) {
		// Create new image from the mask
		const img = new Image();
		img.src = MASKS[idx];

		// Draw the color
		btx.globalCompositeOperation = "source-over";
		btx.fillStyle = COLORS[idx];
		btx.fillRect(0, 0, buffer.width, buffer.height);

		// Mask the color
		btx.globalCompositeOperation = "darken";
		btx.drawImage(img, 0, 0);
	}

	function clear_canvas() {
		ctx.save();
		ctx.globalCompositeOperation = "source-over";
		ctx.fillStyle = "#000000";
		ctx.fillRect(0, 0, canvas.width, canvas.height);
		ctx.restore();
	}

	function draw_layer_from_buffer() {
		ctx.globalCompositeOperation = "lighten";
		ctx.drawImage(buffer, 0, 0);
	}


	// function render() {
	// 	// Get the output canvas
	// 	const canvas = document.getElementById("canvas");
	// 	const ctx = canvas.getContext("2d");

	// 	// Create a buffer canvas to do our recoloring
	// 	const buffer = document.createElement("canvas");
	// 	buffer.width = canvas.width;
	// 	buffer.height = canvas.height;
	// 	const btx = buffer.getContext("2d");

	// 	for (var i=0; i<1; i++) {
	// 		// Create new image from the mask
	// 		const img = new Image();
	// 		img.src = MASKS[i];

	// 		// Recolor the mask
	// 		btx.globalCompositeOperation = "source-over";
	// 		btx.drawImage(img, 0, 0);
	// 		btx.fillStyle = COLORS[i];
	// 		btx.globalCompositeOperation = "multiply";
	// 		btx.fillRect(0, 0, buffer.width, buffer.height);

 //   			ctx.globalCompositeOperation = "lighten";
	// 		ctx.drawImage(buffer, 0, 0);
	// 	}
	// }

</script>

<!-- Set default color values -->
<script>
	document.getElementById("color0").value = "FF0000";
	init();
</script>

<style>
	.imgColumn {
	  float: left;
	  width: 50%;
	}

	.buttonsColumn {
		float: left;
		width: 50%;
	}

	/* Clear floats after the columns */
	.row:after {
	  content: "";
	  display: table;
	  clear: both;
	}

	.debug {
		display: none;
	}
</style>