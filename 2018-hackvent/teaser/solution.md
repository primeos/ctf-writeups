# Day -10 (Teaser.png)

Given was the following image:
![Teaser.png](teaser/Teaser.png)

I've ignored the teaser challenges at first, but when I did some research for
another challenge I stumbled upon Braille (the tactile writing system for blind
people with the bumps / raised dots) and remembered that the image from the
teaser looks like this. So I gave it a try.

The first 4 characters where HTTP so it seemed like the correct solution, but I
had a few problems decoding some special characters:

- `HTTP|||B9T|LY|#2|T|0VX|8T`
- `http.//b9t.ly/#2|t|0vx|8t`
- `http.//b9t.ly/#2't'0vx'8t`

After this I assumed that the first part should be `http://bit.ly` but I had to
do some more research to figure out the shortened link.

The following tool turned out to be pretty helpful (I've used the Unicode
symbols as input):
https://www.dcode.fr/braille-alphabet

This lead me to the following text: `HTTP.//BIT.LY/2?T?JVX?HT`
And with the help of Wikipedia I found out that the last character (`?`) means
"capital follows".
The solution: `http://bit.ly/2TJvxHt`

Opening this link in a browser will lead to the following page:
https://hackvent.hacking-lab.com/T34s3r_MMXVIII/Flag_Stage_1.png

Which displays the following image:
![Flag_Stage_1.png](teaser/Flag_Stage_1.png)

Since it looked similar enough to a QR code I tried to decode it with
[Barcode Scanner](https://f-droid.org/en/packages/com.google.zxing.client.android/reader)
which resulted in the following hint: "rushed by ...".

Given that hint I assumed that I've missed an HTTP redirect and this turned out
to be the case:
https://hackvent.hacking-lab.com/T34s3r_MMXVIII/index.php?flag=UI18-GAUa-lXhq-htyV-w2Wr-0yiV

I've then tried to submit the flag `UI18-GAUa-lXhq-htyV-w2Wr-0yiV` (just in
case), but it didn't work as expected (the prefix isn't `HV18-`).
As it looked like a simple ROT cipher I've started with ROT13 and it gave me the
flag: `HV18-TNHn-yKud-uglI-j2Je-0lvI`.

# Next step (finding the other teaser challenges)

I've continued by providing the correct flag to the URL:
https://hackvent.hacking-lab.com/T34s3r_MMXVIII/index.php?flag=HV18-TNHn-yKud-uglI-j2Je-0lvI

Which results in another redirect to a PDF document:
https://hackvent.hacking-lab.com/T34s3r_MMXVIII/ZOoxjUSe1OVB7OPoVrsX.pdf

With `file`:

ZOoxjUSe1OVB7OPoVrsX.pdf: PDF document, version 1.7

With `strings`:

- old_school.jpg
- QR3C.png
- Santa.txt
- teaser.pls
- Embedded RDF document?

# Day -09 (Morse code)

As I wasn't yet aware of tools like `binwalk` I've tried different online tools
but that didn't work out very well.
But at least it gave me one flag for day -09 via the following tool:
https://www.pdf-online.com/osa/extract.aspx

```
  X Pos   Y Pos Text
  70.94  796.08
  70.94   38.40
 537.84  264.74
 211.49  749.02 HACKvent 2018
 383.83  749.02
  70.94  254.66 .... ...- .---- ---.. -....- --. --- .-. .. -....- --.. .-. ... -... -....- ..- ..-. .- . -....- - ... -.... -.-. -....- -.-. ...- - -
 512.74  254.66
  70.94  227.54
  70.94  205.10
 525.84  279.77
```

The text in the middle seemed to be Morse code:
```
.... ...- .---- ---.. -....- --. --- .-. .. -....- --.. .-. ... -... -....- ..-
..-. .- . -....- - ... -.... -.-. -....- -.-. ...- - -
```

As I'm lazy I tried the following online tool to decode it:
https://morsecode.scphillips.com/translator.html

Which gave me the following flag: `HV18-GORI-ZRSB-UFAE-TS6C-CVTT`

# Other files

After the success with various online tools was pretty limited (not really their
fault as it isn't really a PDF) I tried to find some other Linux tools for this
challenge. I finally managed to extract the embedded files with
`binwalk -e ZOoxjUSe1OVB7OPoVrsX.pdf`.

The files are located in the `files` directory but I didn't have enough time to
extract the other flags.

## teaser.pls

PL/SQL (stored procedure)

## old_school.jpg

Links:

- http://homepage.divms.uiowa.edu/~jones/cards/codes.html
- https://gist.github.com/Pozo/1004284
- http://www.columbia.edu/cu/computinghistory/029.html
- https://www.masswerk.at/cardreader/
- https://gist.github.com/lrvick/ee859af135b3432015e063307eed8ea1

```
029  &-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@'="¢.<(+|!$*);¬ ,%_>?
IBME ¹-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#²'="].<(+|[$*);¬³,%_>?
EBCD &-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ:#@'="[.<(+|]$*);^\,%_>?
     ________________________________________________________________
    /&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZb#@'>V?.¤[<§!$*];^±,%v\¶
12 / O           OOOOOOOOO                        OOOOOO
11|   O                   OOOOOOOOO                     OOOOOO
 0|    O                           OOOOOOOOO                  OOOOOO
 1|     O        O        O        O
 2|      O        O        O        O       O     O     O     O
 3|       O        O        O        O       O     O     O     O
 4|        O        O        O        O       O     O     O     O
 5|         O        O        O        O       O     O     O     O
 6|          O        O        O        O       O     O     O     O
 7|           O        O        O        O       O     O     O     O
 8|            O        O        O        O OOOOOOOOOOOOOOOOOOOOOOOO
 9|             O        O        O        O
  |__________________________________________________________________
    /&-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZb#@'>V?.¤[<§!$*];^±,%v\¶
```

Decoded: TODO
