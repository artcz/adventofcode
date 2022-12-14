"""
This is a random script to generate a template, that you can later use to fit a
oneliner. In this example it builds a Christmas Tree (which is close enough to
both advent and the topic of today's challange, and then fits oneliner that
solves today's challange to that template.
"""

width = 100
center = width // 2

top = 6
rows = []

star = """
#
#  #  #
###
#####
## ##### ##
#####
###
#  #  #
#
""".strip().splitlines()

padd = "x"
center = "xxxxxx"
rows = []
for row in star:
    rows.append(row)
rows.append(center)

x = [7, 19, 31, 49]     # hand crafted, fine tuned, for that artisanal chrismas tree look

for i in range(max(x) + 1):
    if i in x:
        divider = ("." * (6 + 2 * x.index(i))).center(len(rows[-1]), "#")
        rows.append(divider)
        row = padd * ((i//5) * 3) + center + padd * ((i//5) * 3)
        rows.append(row)
        continue

    row = padd + rows[-1] + padd
    rows.append(row)


for i in range(len(rows)):
    rows[i] = rows[i].center(width)
    if i == len(star):
        rows[i] = "(" + rows[i][1:]


# This is useful to check if the snippet will fit in the template.
cnt = 0
for row in rows:
    cnt += row.count("x")


template = "\n".join("".join(row) for row in rows)

# now slowly replace template with characters.
replaceWith = """
lambda s,ft,i:(getattr(s,"setrecurs""ionlimit")(  2500), print( [ len([v for k, v in ft.reduce(   lambda prev, b: { **prev, "G": {**prev ["G"],  (lambda a:lambda v:a(a,v))(lambda s,arg:((((arg[0],arg[1])if(arg!=(500,0))else None) if prev["p2"]else((arg[0],arg[1])if arg[1]<prev["maxy"]else None))if((arg[0],arg[1]+1)in prev['G']and(arg[0]-1,arg[1]+1)in prev['G']and(arg[0]+1,arg[1]+1)in prev['G'])or arg[1]>=prev["maxy"]+1 else(s(s,(arg[0]+0,arg[1]+1))if(arg[0]+0,arg[1]+1)not in prev['G']else(s(s,(arg[0]-1,arg[1]+1))if(arg[0]-1,arg[1]+1)not in prev['G']else(s(s,(arg[0]+1,arg[1]+1))if(arg[0]+1, arg[1]+1)not in prev['G']  else(None,print(arg)))))))((500, 0)) if None not in prev["G"]else None:"o"},},range(5*10000),ft.reduce(lambda a,b:{**a,"maxy":max(k[1]for k in a["G"].keys())},range(1),{"G":{(x,y):"#"for item in[[ tuple( map( int,  pos.split(',')))  for pos in item]  for item in[line.strip().split('->')   for line in  data.splitlines()]]for m,n in zip(item,item[1:])for x in range(min(m[0],n[0]),max(m[0],n[0])+1)for y in range(min(m[1],n[1]),max(m[1],n[1])+1)},"p2":p2,}))["G"].items()if v=="o"and k is not None])+p2 for(data,p2)in( (i, False),(i, True))])))(__import__("sys"),      __import__("functools"), open(0).read().strip())
""".strip()

s = []
cur = 0

for i in range(len(template)):
    if cur < len(replaceWith) and template[i] == "x":
        s.append(replaceWith[cur])
        cur += 1
    elif cur >= len(replaceWith) and template[i] == "x":
        # replace with comment instead of rest of template
        s.append("#")
    else:
        # don't forget about empty spaces
        s.append(template[i])

tree = "".join(s)


print(tree)
