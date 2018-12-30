#!/usr/bin/env nix-shell
#!nix-shell -I nixpkgs=/var/nixos-unstable -i python3 -p "python3.withPackages(ps: [ps.pycrypto])"

import secrets
import hashlib
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

g = 3
p = 0x00e1a540d72bb311db26ea6e58b7dc207cf55d0c3a90d7c1f74e7fcb67c7af097d99c73e002c9266e70cbdf735ebd864ea279a0a4d41dd6537837bfc07d84943a376d163ec20a51dd6073dbfc34cbdce9d88ad22a9bb72f5bb143b5c9e531ab100590b9f97d1e9c7a3dfe7961fd6e86078ad43918b47816925803db47862e5f69c90078c6dc287fc6cf7742a9f1717d828a610fe469c92f34783351b21ac1ec988eae0e16ff4ef89c1a19ccd7e3b5cb0c14e0424dfde338789923013aeb7791e19ba378cb2e0e0b318f46865d438ac53999f69f0ae8045d2ff40821b5fdcb0a3b9942f29a0cd8e55febd0ee9006d936d51335a2e63b6affbed6175e1228a53d6a9

# Not required:
#IV = "d724c349c2b28831"
#key = "313371337"

y_a = 17577019968135092891915317246036083578063875217491307011102321322815719709605741738459191569497548099944025771002530369133716621942963853230082186943938164591230020725702755002287589522851172217336150522367152517270250629688405924844750026155547199020780202996200555426652190631837288299999083335649923708175859594750237448640513280683859296367607523542293538555215282798100455110266565881599829107971869244773384413618546118850868579583095489023778055976570366853411496753062216229293710557686212314300848121614558806328788578096144576605248971916454783615989429937555579437307320472405217413938048149254574677430624
y_b = 15228628318558071728245462802366236848375416102820239825350329247148900182647243994904519787528142824353837070194785550898962097219309344881183948914850354340893035399529028331238911753358245357848436203268982345430735846016484221944423499956958406189854969330305125479065873712331269870135028162018087451460656203085824963123310757985362748654204595136594184636862693563510767025800252822776154986386637346156842972134635578534633722315375292616298410141343725683471387328655106920310236007034951004329720717533666052625540760911360823548318810161367913281234234193760867208897459774865037319252137821553407707977377

x_a = 15354042672206252628490224264690454581428691371145769559092814316529005534284986825328196215781584589569502108538299687671360602614840353757694181909133163897573492858461087503205334476595470229312365805497727162669571762705941038047806750508918673276003220409988850130107551639956795373407913778173166953425544410500723037568398426599926027445943026206335288371772534327534782843934568830300014348181115075724953280567387710366794375659264751027802164342021881082026175781378370505510594344477625073089451475079404319398766824697036100569366992915850876267412204007674638070052231495975910539370211916959396581341187
x_b = 24066281471841800571785391299478932393606604631570747719234190833563831323048560489985104647740851387294266059806507646219897489674141253655728222160591002847957983699630014448631913189076240766350109997173680095635888387625106200180587983566458682601437961932612371802135600762799155170194781386585747251887401158863229430417558252072400106864882568430006279252355777977506184622958178013792194286509863103653264609433956534344554272368257606911851761413444759489601816170266965831595460319509425604754911108260324785453521517633762757918007607941187867884576199454899178918198735935303355242532437674933545947054417

def calculate_key(x, y):
    return str((y * x) % p)

key_a = calculate_key(x_a, y_b)
key_b = calculate_key(x_b, y_a)

iv_a = key_a[0:16]
iv_b = key_b[0:16]

message = "jqMYIn4fzSqzIXArwJm/kPitNhf4lwhL0yPRKpF+NYXyPmhoEwNG/k2L5vCZqFWNPvTzisnu93/8uK/PZnnCGg=="
cipher_text_bytes = b64decode(message)

aes_key_a = bytes(hashlib.md5(bytes(key_a, "utf-8")).hexdigest(), "utf-8")
aes_key_b = bytes(hashlib.md5(bytes(key_b, "utf-8")).hexdigest(), "utf-8")

cipher_a = AES.new(aes_key_a, AES.MODE_CBC, iv=bytes(iv_a, "utf-8"))
cipher_b = AES.new(aes_key_b, AES.MODE_CBC, iv=bytes(iv_b, "utf-8"))

plaintext_a = cipher_a.decrypt(cipher_text_bytes)
plaintext_b = cipher_b.decrypt(cipher_text_bytes)

print(plaintext_a)
print(plaintext_b)