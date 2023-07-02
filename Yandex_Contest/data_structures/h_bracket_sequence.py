# Яндекс Контест Задача H. "Скобочная последовательность."

def is_correct_bracket_seq(seq):
    if len(seq) % 2 != 0:
        return False
    for _ in range(len(seq)):
        seq = seq.replace('()', '')
        seq = seq.replace('[]', '')
        seq = seq.replace('{}', '')
    return not seq


print(is_correct_bracket_seq(input()))
