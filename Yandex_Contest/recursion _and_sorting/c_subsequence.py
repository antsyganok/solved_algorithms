# Яндекс Контест Задача C. "Подпоследовательность."

def subseq(strg, f_strg, idx=0):
    for chr in f_strg:
        if chr == strg[idx]:
            idx += 1
            if idx == len(strg):
                print(True)
                return

    print(False)


if __name__ == '__main__':
    strg = input()
    f_strg = input()
    subseq(strg, f_strg)
