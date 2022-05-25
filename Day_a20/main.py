from operator import methodcaller

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

print(*map(methodcaller("strip"), humpty_dumpty), sep="\n")

from operator import methodcaller

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
names_title = map(methodcaller("title"), filter(lambda name: len(name) < 8, names))

print(*filter(lambda number: number >= 0, range(-5, 11)))