import sys
def II(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def SI(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

S = SI()
p_list = [("tourist",3858),
("ksun48",3679),
("Benq",3658),
("Um_nik",3648),
("apiad", 3638),
("Stonefeang", 3630),
("ecnerwala",3613),
("mnbvmar", 3555),
("newbiedmy", 3516),
("semiexp", 3481)]

for p in p_list:
    if p[0] == S:
        print(p[1])
        break