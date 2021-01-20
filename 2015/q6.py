def is_similar_new(text1, text2):
    """
    text1とtext2が類似しているかを判定する
    """
    if text1 == text2:
        return False
    else:
        list1 = list(text1)
        list2 = list(text2)
        # 文字数を大きい方に揃える
        # 少ない方の文字列に" "をたす
        if len(list1) > len(list2):
            list2 += [" "]*(len(list1)-len(list2))
        elif len(list1) < len(list2):
            list1 += [" "]*(len(list2)-len(list1)) 
        cnt = 0     # 対応する文字が異なる位置の箇所数
        for l1, l2 in zip(list1, list2):
            if l1 != l2:
                cnt += 1
        if cnt < 5:
            return True
        else:
            return False