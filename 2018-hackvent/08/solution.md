# Day 08: Advent Snail

## Challenge text

```
In cyberstan there is a big tradition to backe advents snails during advent.
```

![4dv3ntSn4il.png](08/4dv3ntSn4il.png)

## Solution

- Image: 160x160 Pixels
- Data: 25x25
- Downscaled with GIMP: Interpolation "None" (important)

From reading the chat I figured out that "snail" is the hint.
I first tried to find the `HV18` prefix (assuming the binary data can be
converted into ASCII) but that didn't work out.

- Center of image: 12x12 -> Black
- First up and then clockwise?
- With Black=0, White=1: 00000001101111001100000000
- -> Doesn't seem right
- ASCII -> Binary: HV18 -> 01001000 01010110 00110001 00111000
- Can't find this pattern
- ASCII -> Binary: - -> 00101101

To decode it I wrote a Python program (`solution.py`) but the code isn't really
nice due to frequent changes (tried different approaches).

Solution: solution.png (QR-Code)
![solution.png](08/solution.png)

Flag: `HV18-$$nn-@@11-LLr0-B1ne`
