import functools


@functools.total_ordering
class List:
    def __init__(self, ll): self.ll = ll
    def __repr__(self): return f"List({self.ll})"
    def __eq__(self, obj): return self == List([obj]) if isinstance(obj, Int) else self.ll == obj.ll
    def __lt__(self, obj): return self < List([obj]) if isinstance(obj, Int) else self.ll < obj.ll



@functools.total_ordering
class Int:
    def __init__(self, x): self.x = x
    def __repr__(self): return f"Int({self.x})"
    def __eq__(self, obj): return NotImplemented if isinstance(obj, List) else self.x == obj.x
    def __lt__(self, obj): return NotImplemented if isinstance(obj, List) else self.x < obj.x



def wrap(x):
    if isinstance(x, int):
        return Int(x)

    ans = List([])
    for y in x:
        ans.ll.append(wrap(y))

    return ans


def main(fname):
    print(fname)
    print('----')
    ans = 0
    paras = open(fname).read().split("\n\n")
    for i, para in enumerate(paras, start=1):
        a, b = para.splitlines()

        a = wrap(eval(a))
        b = wrap(eval(b))

        if a < b: ans += i


    print(ans)

    lines = [wrap(eval(ll)) for ll in open(fname).read().splitlines() if ll]

    lines.append(wrap([[2]]))
    lines.append(wrap([[6]]))

    z = sorted(lines)
    ans = 1
    ans *= z.index(wrap([[2]])) + 1
    ans *= z.index(wrap([[6]])) + 1

    print(ans)


main("test")
main("input")
