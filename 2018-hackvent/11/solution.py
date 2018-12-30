#! /usr/bin/env python
#! nix-shell -I nixpkgs=/var/nixos-unstable -i python3

import binascii
import re

x = 0x485631382D4288BB2CDF615FC4576B25BA2EE4C74F5E8598BA6BBDFAE8F
p = 95569680412274326120336555225544217009989759221981789160850199934150137

print("x = " + str(x))

for n in range(0, 10000):
    a = x + n * p
    a_hex = hex(a).lstrip("0x")
    if not a_hex.startswith("4856"): # HV
        continue
    if len(a_hex) % 2 != 0:
        a_hex = a_hex[:-1]
    print(binascii.unhexlify(a_hex))
