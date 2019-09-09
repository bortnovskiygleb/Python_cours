st = "I've been dying lately"
sl = st[5:9], st[10:15]
print(sl[1])


my_dict = {
	"musicians" : "Green day",
	"movies" : "Konstantin"
}
print(my_dict)
d = dict(a = 2, b = 2000, c = "fff")
for i, k in d.items():
	print("key = {}, value = {}".format(i,k))