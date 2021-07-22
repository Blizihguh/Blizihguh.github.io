---
layout: page
title: Microsoft IME Hotkey Fix
permalink: /code/ime-fixes/
---

<b>TL;DR: Microsoft IME is bad. This AutoHotKey script makes it better.</b><br/>
<a href="/code/ime-fixes#1">Skip to the good part</a>

<h2>Everybody Hates Microsoft IME</h2>

Windows' native input method editor (IME) is not the most user-friendly program I've ever used. In fact, I think it might genuinely be the least. It's generally slow and buggy, even on my Mtn Dew-cooled pro gamer laptop. Switching between English and Japanese input is guaranteed to lag your computer out, and if you happen to be a Firefox user, causes a massive memory spike, which has been an outstanding bug for several years at time of writing. 

The best thing to do is to leave it on Japanese all the time, and switch between Alphanumeric (QWERTY) input and Kana input, but this introduces its own issues. Specifically, the issue of keybinds: the default keybinds for IME are <em>awful</em>. There are about a dozen of them, all mapped to weird, counterintuitive inputs. When was the last time you mapped a key command to CapsLock? If you're a human being, the answer is probably "never." In fact, I'm pretty sure that's an automatic disqualification on the Turing Test. Sadly, the people who work on Microsoft IME are more machine than man, so we cannot count on their choice of keybinds.

So, why not remap the keys then? Well, here we run into a separate issue. Being the cyber-man space mutants that they are, the Microsoft IME team have designed the configuration dialog <em>of the future!</em> Unfortunately, it's a bad future, one in which all user interfaces are designed by throwing magnets against a CRT monitor until the interference patterns produce something that vaguely resembles a TV remote.

Behold, the Microsoft IME key config dialog:

<img src="/img/ime-fixes/ui-design-for-satans.png">

Already, we know this is bad, because it's buried under two separate buttons that say "Advanced." When a UI designer labels a button "Advanced," it's because they don't want you to click it. If they hide a dialog under <em>two</em> "Advanced" buttons, they're deeply ashamed of it. Legally, three "Advanced" buttons carries an implication of guilt in most jurisdictions, but thankfully we haven't stooped that low.

More concerningly, we see the key config window is woefully small for its contents. This is the default size. It is also the only size. I tried using Sizer; it did not work. This is what you get; you'll take your microscopic configuration spreadsheet and you'll <em>like it</em>, goddammit. Even worse, can you honestly tell me you have <em>any</em> idea what <em>any</em> of this means?! No Input? How can you have a hotkey with no input? Convert? Showing? Changing? <em>Char In???</em>

The real cardinal sin here, though, is the leftmost column: Key. In every other program on the planet, remapping keys is fairly simple: You have a list of every function that can be bound to a key combo, and the user inputs their key(s) of choice. Not so here. If you want to set up a new hotkey, first you must select the key combination you want from a drop-down list, and then you must set what it does in every single possible state that the IME can have.

Yes, you read that right. <em>From a drop-down list.</em>

No, you don't get to input your own keys. You must pick from Microsoft's pre-ordained selection.

No, you can't use function keys.

Yes, CapsLock is an option.

<h2 id="1">Is There No Hope?</h2>

Thankfully, there is hope.

<b>Introducing ime-fix.ahk: an elegant script, for a more civilized age.</b>

F1 cycles between Variable-Width Alphanumeric, Hiragana, and Katakana input. F2 cycles between Variable-Width Alphanumeric and Full-Width Alphanumeric. (But F2 is a little buggy).

<a href="https://www.autohotkey.com/">[Download AutoHotKey to install ime-fix]</a><br/>
<a href="/download/ime-fix.ahk">[Download ime-fix.ahk]</a>

<center>
<img src="/img/ime-fixes/the-only-keys-you-need.png"><br/>
<em>The only keys you need.</em></center>