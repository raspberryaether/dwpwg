Introduction
============
**dwpwg**, the **d**ice**w**are **p**ass**w**ord **g**enerator...

...is a Diceware-inspired passphrase/keyphrase construction utility.

TL;DR
=====
If you don't quite understand this section, skip to the next section,
and *read the whole page*. More detailed instructions follow.

You will need at least one d20. Run:

    sudo pip install dwpwg
    dwpwg --help

Do not use fewer than 4 words for anything.
Do not use fewer than 8 words for an encryption key.
Do not use fewer than 12 words for anything involving cryptocurrency.
***NEVER LOSE A CRYPTOGRAPHIC KEYPHRASE,*** or everything will be gone forever.
You have been warned.

Why?
====

First, read:
    <https://xkcd.com/936/>

It is easy for humans to think up terrible passwords. As a matter of fact, it
is reasonable to assume that humans are incredibly lousy at thinking up anything
that is meant to be random and unguessable. Because of an illogical yet
near universal misconception that "hard to remember == hard to guess", we use
weaker passwords than we should, and to add insult to injury, we forget them.

Diceware is a method invented by one Arnold G. Reinhold for generating 
easy-to-remember passwords which are also extremely difficult for even a
powerful supercomputing cluster to guess.

More required reading:
    <http://world.std.com/~reinhold/diceware.html>

About
=====

Despite its name, this program is not intended to generate random passwords.
It is designed, instead, to generate random word lists, and create passwords
from a very small, randomised subset of those wordlists using entropy generated
using 20-sided dice normally used for tabletop gaming.

Note that in this modern age, it no longer makes (and maybe never did make) you
a crazy person to believe that you may be being watched. In such a case, from 
a security perspective, dwpwg does as good or only slightly better than an 
ordinary random password generator; all of its utility will manifest in the 
easy-to-remember passwords it will help you generate.

dwpwg thrives, however, in the art of cryptographic keyphrase generation. In a
case where an adversary has purposefully debilitated the pseudorandom number 
generating software on your computer, they can theoretically weaken any
encryption keys generated therewith. However, assuming that:

 - your machine is offline and/or free of keyloggers/rootkits, and
 - dwpwg itself is intact, and 
 - the Python interpreter on your machine, its operating system, or the machine
   itself has not been compromised in a way more or less *specifically 
   targeting dwpwg*, 

an attacker would have to compromise *both* your computer's pseudorandom number
generation routines AND your dice in order to effectively mount a reduced 
keyspace attack against you.

A "super paranoid" mode is in development to tackle the remaining concerns
above by allowing a list to be printed and used offline (albeit with much of
the convenience understandably lost). This mode is superior to simply using an
already-constructed wordlist because an attacker necessarily must compromise
both your dice and your list in order to have an easier time guessing your 
passphrase. Using a publicly-available list hands them half of the puzzle for
free.

Installing
==========

Prerequisites:
- Python 2.7.x
- pip
- an Internet connection

dwpwg is available from PyPI using ```pip install dwpwg```. Depending on your
environment, you will probably need to be root (on GNU/Linux) or running as
Administrator (on Windows). Run:

    pip install dwpwg

If you prefer to run the development version of dwpwg, or to run it in-place
rather than installing, that is possible too:

    git clone https://github.com/raspberryaether/dwpwg.git
    cd dwpwg
    python -m dwpwg --help

It is also possible to manually create and install the dwpwg package locally.
Perform the steps above to get the development version, then, as root or
Administrator:

    python setup.py install


Detailed usage instructions
===========================

This is a command-line utility. If you are this concerned with security, we will
assume you have at least general knowledge of how to execute one. If you do not,
we strongly suggest you get familiar with it. In today's political climate, 
things are only going to get worse for those who rely on cushy UIs for 
everything.

You'll need to have at least one 20-sided die, though the more you can roll
at once, the faster entropy generation will go. Using a dice cup will improve
your speed (faster rolls), convenience (no "cleanup" or "runaways"), and 
security (smaller viewing angle for eavesdroppers and an arguably 
harder-to-analyse acoustic profile). Just be sure to actually shake the dice,
not just swirl them around.

Clone the repository from GitHub or otherwise. Get your shell/prompt inside the
root directory of the project. From there, run:

    python -m dwpwg #

replacing # with the number of words you would like in your password. 

Follow onscreen instructions. Press ENTER after entering each individual die
roll. A counter will count down to completion.

Your password will be displayed in plaintext on the last line. Physically 
secure your device as necessary. When in doubt, close your shades, lock your 
door, wear a tinfoil hat (that one is a joke, but we are sure it won't hurt 
anything if you insist), and do it all over again.

Do not use fewer than 4 words for anything.
Do not use fewer than 8 words for an encryption key.
Do not user fewer than 12 words for anything involving cryptocurrency.
***NEVER LOSE A CRYPTOGRAPHIC KEYPHRASE,*** or everything will be gone forever.

DO NOT LOSE YOUR PASSWORD; **ESPECIALLY IF IT IS FOR ENCRYPTION OR 
CRYPTOCURRENCY**. If in doubt, **write it down** and put it somewhere **safe**
from prying eyes, fire, and flood alike. Make an hourly habit of reciting your 
passphrase inside your head.

REMEMBER: **If you lose an encryption or cryptocurrency keyphrase, all your
data and/or money will be gone forever**. There's only so many times we can
warn you. ***DO NOT LOSE YOUR KEYPHRASE.***

Legal
=====

dwpwg
-----

dwpwg - (d)ice(w)are (p)ass(w)ord (g)enerator
Copyright (C) 2017 Raspberry Aether

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Word lists
----------

Though the copyright status of word lists is dubious at best, the author of the
wordlists used by dwpwg releases it under the terms of the GNU GPLv2, and we do
not wish to ruffle any feathers. Therefore, to simplify things, we released this
application, and the heavily-modified wordlists within, under the same licence.

Copyright information for the word source(s):

    Copyright (c) Frank Richter <frank.richter@hrz.tu-chemnitz.de> 1995-2016
    GNU General Public License, see COPYING for details
    It comes with ABSOLUTELY NO WARRANTY.

At the time of this writing, the master word list was available at:

    <http://ftp.tu-chemnitz.de/pub/Local/urz/ding/de-en/>

Note that the master word list is a German-to-English translation dictionary
and, therefore, had to be processed beyond recognition in order to create the
wordlists distributed with this application. Of course, you may use our modified
lists under the terms of the same licence as the source material.

Support us
==========

We accept donations in cryptocurrency.

| Currency | Address | QR |
| -------- | ------- | --- |
| Monero |  45DmoRGs9wLUXNBvHo7pS6Wg1VuVQJHsg1<br>eCRrNCgGxSf6n6oep1daE2eo3wNUZAoyDz<br>y94HNFRUogn2oAVup7WCAqDJmHp | ![Monero QR](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=45DmoRGs9wLUXNBvHo7pS6Wg1VuVQJHsg1eCRrNCgGxSf6n6oep1daE2eo3wNUZAoyDzy94HNFRUogn2oAVup7WCAqDJmHp) |
| Bitcoin | 144PQPFa2sVm7mGHdSayk8VjzFVzSbBMCM | ![Bitcoin QR](http://api.qrserver.com/v1/create-qr-code/?size=150x150&data=144PQPFa2sVm7mGHdSayk8VjzFVzSbBMCM) |


Thank you for your generosity.
