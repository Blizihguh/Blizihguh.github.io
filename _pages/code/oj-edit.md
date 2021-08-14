---
layout: contentspage
title: OJ Edit
permalink: /code/oj-edit/
description: A tool for editing map files and graphics for the game 100% Orange Juice.
embedimage: /img/embeds/oj-edit.png
---

<em>(Warning: This program is not actively maintained, and has not been since the advent of official graphics modding. I do not intend to maintain it much, at least in the foreseeable future. If your goal is to make a graphics mod through the official modding feature, you probably don't need OJ Edit to do so!)</em>

Way back in the halcyon days of 2017, 100% Orange Juice had no official modding support. Fruitbat Factory had long since announced plans to add custom stages, but that was years prior, and nothing had come out about it in a long time. What's more, there was no official word about support for graphics modding. Clearly, something needed to be done! (Or, more likely: I just felt like doing it myself.)

Enter OJ Edit. 

<!--more-->

<h2 id="1">What is OJ Edit?</h2>

OJ Edit is a desktop tool to import, export, decrypt, encrypt, and view map and image files for 100% Orange Juice. Any map you can dream, you can put into Orange Juice! OJ Edit allows you to draw a map in your image editor of choice, then turn it into an OJ map file and put it into the game! Not feeling creative? It also comes with a selection of custom maps: installing them is as easy as dragging and dropping the included fields.pak file into your OJ install! And of course, if there are any ingame textures you want to replace, OJ Edit will let you convert your files to the proper format!

<div class="image-gallery">
<div class="box"><a href="/img/oj-edit/1.png">
  <img src="/img/oj-edit/1.png" class="img-gallery" />
</a></div>
<div class="box"><a href="/img/oj-edit/2.png">
  <img src="/img/oj-edit/2.png" class="img-gallery" />
</a></div>
<div class="box"><a href="/img/oj-edit/3.png">
  <img src="/img/oj-edit/3.png" class="img-gallery" />
</a></div>
</div>

<h2 id="2">Where can I get OJ Edit?</h2>

Releases can be found on <a href="https://gamebanana.com/tools/6227">OJ Edit's GameBanana page</a>. Source code (requires Python 2.7.x) can be found on <a href="https://github.com/Blizihguh/OJ-Edit">its Github page</a>.

<h2 id="3">How do I use OJ Edit?</h2>

Included with every OJ Edit release is a Readme.txt and an Examples folder, which should help with understanding the general workflow. In order to make a custom map, you'll want to create a map image in an image editor like MS Paint, Paint.NET, or Photoshop; use the example maps and the included OJ Palette.png file as a reference. Once you've created this image, convert it to a .fld file with OJ Edit, then include the .fld file in a fields.pak file, which OJ Edit can export as well. If you get stuck, feel free to join the <a href="https://discord.gg/VQfDFxm">100% OJ Modding Discord server</a>, which is full of people who would be happy to help.

<div class="image-gallery">
<div class="box"><a href="/img/oj-edit/4.png">
  <img src="/img/oj-edit/4.png" class="img-gallery" />
</a></div>
<div class="box"><a href="/img/oj-edit/5.png">
  <img src="/img/oj-edit/5.png" class="img-gallery" />
</a></div>
</div>

<style>
  /*! div style */
  .image-gallery {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill,minmax(200px, 1fr));
    justify-content: center;
    padding: 4px;
  }

  .box {
      flex-basis: 25%;
      width: 100%;
      padding: 10px;
      margin: 2px;
  }

  .img-gallery {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transform: scale(1);
  transition: all 0.3s ease-in-out;
  &:hover {
    transform: scale(1.05);
  }
</style>