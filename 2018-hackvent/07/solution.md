# Day 07: flappy.pl

## Challenge text

```
Time for a little game. It's hardy obfuscated, i promise ... ;-)
get flappy (https://hackvent.hacking-lab.com/flappy.pl.txt)
```

## Solution

Idea: Execute the code and try to read it.
`->` Refactor the code to make it more readable.

Failed attempt: HV18-faLL-D33p-INT0-H3ll and HV18-faLL-D33p-INT0-PERL-H3ll (was
in the source-code but would've been too easy and didn't make much sense).

Turned out to be a bit difficult (I don't know Perl) but it didn't take too
long.

By playing a bit I figured that the horizontal lines contain the characters for
the flag.

New idea: Rewrite the code to avoid exits `->` replace `last` with `(true || last)`
(`->` worked, 2x occurrences (alternative: simply remove `last`)).

Flag: `HV18-bMnF-racH-XdMC-xSJJ-I2fL`
