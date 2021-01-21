from typing import List, Tuple

def compute_transform_tables(
    source_string: str,
    destination_string: str,
    copy_cost: int,
    replace_cost: int,
    delete_cost: int,
    insert_cost: int,
) -> Tuple[List[int], List[str]]:
    source_seq = list(source_string)
    destination_seq = list(destination_string)
    len_source_seq = len(source_seq)
    len_destination_seq = len(destination_seq)

    costs = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]
    ops = [
        [0 for _ in range(len_destination_seq + 1)] for _ in range(len_source_seq + 1)
    ]

    for i in range(1, len_source_seq + 1):
        costs[i][0] = i * delete_cost
        ops[i][0] = "D%c" % source_seq[i - 1]

    for i in range(1, len_destination_seq + 1):
        costs[0][i] = i * insert_cost
        ops[0][i] = "I%c" % destination_seq[i - 1]

    for i in range(1, len_source_seq + 1):
        for j in range(1, len_destination_seq + 1):
            if source_seq[i - 1] == destination_seq[j - 1]:
                costs[i][j] = costs[i - 1][j - 1] + copy_cost
                ops[i][j] = "C%c" % source_seq[i - 1]
            else:
                costs[i][j] = costs[i - 1][j - 1] + replace_cost
                ops[i][j] = "R%c" % source_seq[i - 1] + str(destination_seq[j - 1])

            if costs[i - 1][j] + delete_cost < costs[i][j]:
                costs[i][j] = costs[i - 1][j] + delete_cost
                ops[i][j] = "D%c" % source_seq[i - 1]

            if costs[i][j - 1] + insert_cost < costs[i][j]:
                costs[i][j] = costs[i][j - 1] + insert_cost
                ops[i][j] = "I%c" % destination_seq[j - 1]

    return costs, ops

def assemble_transformation(ops: List[str], i: int, j: int) -> List[str]:
    if i == 0 and j == 0:
        return []
    else:
        if ops[i][j][0] == "C" or ops[i][j][0] == "R":
            seq = assemble_transformation(ops, i - 1, j - 1)
            seq.append(ops[i][j])
            return seq
        elif ops[i][j][0] == "D":
            seq = assemble_transformation(ops, i - 1, j)
            seq.append(ops[i][j])
            return seq
        else:
            seq = assemble_transformation(ops, i, j - 1)
            seq.append(ops[i][j])
            return seq


def calc_min_steps(text1, text2):
    """
    最小コスト数を計算する
    """
    if len(text1) > len(text2):
        long = text1
        short = text2
    else:
        long = text2
        short = text1
    _, operations = compute_transform_tables(short, long, 0, 1, 1, 1)
    m = len(operations)
    n = len(operations[0])
    sequence = assemble_transformation(operations, m - 1, n - 1)

    string = list(short)
    i = 0
    cost = 0

    for op in sequence:

        if op[0] == "C":
            cost += 0
        elif op[0] == "R":
            string[i] = op[2]
            cost += 1
        elif op[0] == "D":
            string.pop(i)
            cost += 1
        else:
            string.insert(i, op[1])
            cost += 1
        i += 1

    return cost

def find_similar_lines(text):
    cnt = 0
    for i in range(len(text)):
        for j in range(i):
            if text[i] == text[j]:
                continue
            elif calc_min_steps(text[i], text[j]) < 4:
                print("類似する2行の組: {}と{}".format(text[j], text[i]), "\n")
                cnt += 1
    print("見つけた組の個数: {}".format(cnt))

    
if __name__ == "__main__":
    text = []
    with open('sample.txt') as f:
        for line in f.readlines():
            text.append(line.split('\n')[0])
    find_similar_lines(text)