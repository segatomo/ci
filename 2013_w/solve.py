import itertools
import pprint

def split_equation(equation):
    """
    +を区切り文字として論理式を分割する
    >>> split_equation('b&a+b&c+a&b&c')
    ['b&a', 'b&c', 'a&b&c']
    """
    res = []
    for e in equation.split('+'):
        res.append(e)
    return res



def solve2(equation):
    res = split_equation(equation)
    # 論理式に登場する変数
    var = list(set(itertools.chain.from_iterable([r.split('&') for r in res])))
    ans = []
    values = list(itertools.combinations_with_replacement([0,1],len(var)))
    # 解の候補
    values = list(set(itertools.chain.from_iterable([list(itertools.permutations(v)) for v in values])))

    for v in values:
        data = {}
        for i in range(len(var)):
            data[var[i]] = v[i]
        for r in res:
            var2 = r.split('&')
            if sum([data[v2] for v2 in var2]) == len(var2):
                ans.append(data)
                break
    if len(ans) > 0:
        pprint.pprint(ans)
    else:
        print('none')


def reverse(x):
    """
    xの否定を返す
    """
    if x == 0:
        return 1
    else:
        return 0


def solve3(equation):
    res = split_equation(equation)
    # 論理式に登場する変数(!も含む)
    var = list(set(itertools.chain.from_iterable([r.split('&') for r in res])))

    # 論理式に登場する変数
    new_var = list(set([r.split('!')[-1] for r in var]))

    # 解の候補
    values = list(itertools.combinations_with_replacement([0,1],len(new_var)))
    values = list(set(itertools.chain.from_iterable([list(itertools.permutations(v)) for v in values])))
    ans = []
    for v in values:
        data = {}
        for i in range(len(new_var)):
            data[new_var[i]] = v[i]
        for r in res:
            var2 = r.split('&')
            if sum([data[v2]  if v2[0] != "!"  else reverse(data[v2[1:]]) for v2 in var2]) == len(var2):
                ans.append(data)
                break
    if len(ans) > 0:
        pprint.pprint(ans)
    else:
        print('none')


def process(equation):
    # ()を処理する
    i = 0
    res = []
    while i < len(equation):
        if equation[i] == '(':
            tmp = []
            for j,e in enumerate(equation[i+1:]):
                if e == ')':
                    i += j+2
                    break
                else:
                    tmp.append(e)
            res.append(tmp)
        else:
            res.append(equation[i])
            i += 1
    return res
    



def solve4(equation):
    res = split_equation(equation)
    # 論理式に登場する変数(!も含む)
    var = list(set(itertools.chain.from_iterable([r.split('&') for r in res])))

    # 論理式に登場する変数
    new_var = list(set([r.split('!')[-1] for r in var]))

    # 解の候補
    values = list(itertools.combinations_with_replacement([0,1],len(new_var)))
    values = list(set(itertools.chain.from_iterable([list(itertools.permutations(v)) for v in values])))
    ans = []
    for v in values:
        data = {}
        for i in range(len(new_var)):
            data[new_var[i]] = v[i]
        for r in res:
            var2 = r.split('&')
            if sum([data[v2]  if v2[0] != "!"  else reverse(data[v2[1:]]) for v2 in var2]) == len(var2):
                ans.append(data)
                break
    if len(ans) > 0:
        pprint.pprint(ans)
    else:
        print('none')

                

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    split_equation('b&a+b&c+a&b&c')
    solve2('b&a+b&c+a&b&c')
    solve3('!a&b&!c+a&!d')