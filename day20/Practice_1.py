import operator

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",  
    "    Couldn't put Humpty together again."
]

stripped_lines = map(operator.methodcaller('strip'), humpty_dumpty)

for line in stripped_lines:
    print(line)
