
# (lambda inp:print(inp)
# )(open(0).read().strip().splitlines())

(lambda lines:print([sum((lambda a,b:{0:3,-1:0,+2:0,+1:6,-2:6}["XYZ".index(b)-"ABC".index(a)]+"XYZ".index(b)+1)(*line.split())for line in lines),sum((lambda a,b:{"X":{"A":3,"B":1,"C":2},"Y":{"A":1,"B":2,"C":3},"Z":{"A":2,"B":3,"C":1}}[b][a]+"XYZ".index(b)*3)(*line.split())for line in lines),]))(open(0).read().strip().splitlines())
