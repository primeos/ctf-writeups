# Day 02

This was probably the most difficult challenge for me (took me forever...) as I
just didn't realize that 8s and 9s are missing.

I started by converting the decimal numbers to ASCII which didn't work out very
well (the result didn't make much sense). I then continued by trying out
different transformations on the decimal numbers and ASCII text (at some point I
even thought it could be a monoalphabetic cipher).

After I noticed a hint in the chat that there are no 8s and 9s, which I
completely missed, I instantly realized that these are octal numbers and not
decimal numbers.

I used the following tool to convert them to ASCII characters:
[https://www.browserling.com/tools/octal-to-text](https://www.browserling.com/tools/octal-to-text)

And the result looked way better:
```
MJRWKZTHGFTTEIDEMVTCAYTDNIQGCYTDMRSWMZZRM4ZCAZZRM4ZCAYLKNQQGCYTDMRSWM3JAMFUWYIDC
MNSWMZZRM4ZCAZZRM4ZCAYLCMNSGKIDBMRVGWIDCMNVCAZLGM4YWU3JAM4YWOMRAMFRGGZDFEBSWMZZR
NJWSAYLDMRTTE2BAMFRGGZDJNQQGOMLHGIQGCY3EMVTGOMRAMFRGKZTHGFTTEIDBMRSWMZZRM4ZCAYLC
MNSGOMTJNQQGOMLHGIQGCY3EMVTGOMRAMFRGGZDFEBQWEZLGM4YWOMRAMJRWIZLGEA======
```

Due to the `======` at the end and the missing lowercase characters I assumed
it's Base32 encoded and used `base32 -d` to decode it:
```
bcefg1g2 def bcj abcdefg1g2 g1g2 ajl abcdefm ail bcefg1g2 g1g2 abcde adjk bcj efg1jm g1g2 abcde efg1jm acdg2h abcdil g1g2 acdefg2 abefg1g2 adefg1g2 abcdg2il g1g2 acdefg2 abcde abefg1g2 bcdef
```

And this lead me to the most difficult part of the challenge.
I've never seen something like it so I assumed it was encrypted but didn't
manage to decrypt it.

But due to the given flag format: HV18-xxxx-xxxx-xxxx-xxxx-xxxx (29 characters)
I made the following guesses:

- Every word of the Base32 decoded result must map to a single character
- "g1g2" -> "-"
- "bcefg1g2" -> "H"
- "def" -> "V" (or "L", according to the chat)
- "bcj" -> "1"
- "abcdefg1g2" -> "8"
- Often "g1g2" as suffix

But this didn't really help me...

Due to very helpful hints in the chat (Nixie tubes replacement / old
calculators) I finally came upon the following link:
[https://en.wikipedia.org/wiki/Seven-segment_display](https://en.wikipedia.org/wiki/Seven-segment_display)
Which explained a lot :)

I initially assumed it would be the encoding scheme for a 7-segment display,
then for a 17-segment display until I finally landed at the 14-segment display:

- a,b,c,d,e,f,g1,g2,h,i,j,k,l,m `->` 14 segments

Decoding: https://blog.wika.com/knowhow/characteristics-display-digital-indicator/
Reference: https://upload.wikimedia.org/wikipedia/en/0/0a/14_Segment_LCD_characters.jpg

Decoded result:

- H = bcefg1g2
- L = def
- 1 = bcj
- 8 = abcdefg1g2
- - = g1g2
- 7 = ajl
- Q = abcdefm
- T = ail
- H = bcefg1g2
- - = g1g2
- = abcde (Problem!)
- Z = adjk
- 1 = bcj
- K = efg1jm
- - = g1g2
- = abcde (Problem!)
- K = efg1jm
- s = acdg2h
- D = abcdil
- - = g1g2
- G = acdefg2
- P = abefg1g2
- E = adefg1g2
- B = abcdg2il
- - = g1g2
- G = acdefg2
- = abcde (Problem!)
- P = abefg1g2
- U = bcdef

Most difficult: abcde

- https://commons.wikimedia.org/wiki/File:7-segment_abcde.svg
- https://en.wikiversity.org/wiki/Segment_display/Seven-segment_display/D

I didn't really manage to find the flag:

- HL18-7QTH-=Z1K-=KsD-GPEB-G=PU
- HL18-7QTH-DZ1K-DKsD-GPEB-GDPU -> invalid
- HL18-7QTH-bZ1K-bKsD-GPEB-GbPU

So I asked in the chat:
```
[15:34:10] <primeos> Any hints for "abcde" (day 2)? I can't figure it out... :o
[15:34:22] <REDACTED> read back here....
[15:50:30] <primeos> @Illuminated thanks, but just to clarify: I'm only missing
the mapping for "abcde" (already have the rest). Just re-read the history, but
seems like I'm still missing something (I assume it's the one "character" that's
different). Anyway, I guess I'll figure it out eventually or "guess" it
(assuming the rest is correct)
[16:08:13] <REDACTED> @primeos.. in this ^^ history there is a link to github...
that shall help you
[10:22:48] <REDACTED> https://github.com/dmadison/LED-Segment-ASCII
```

That GitHub link was actually pretty helpful. I wrote a Python program to verify
my solution and noticed there was a mistake in it:

- HL18-7QTH-=Z1K-=KSD-GPEB-G=PU (s -> S)

But I still couldn't figure out the last character so I wrote a simple Bash
script to brute-force it (simple for loop + curl)...
Since there where only 10+26 possibilities left this seemed ok.

The correct flag: HL18-7QTH-JZ1K-JKSD-GPEB-GJPU
