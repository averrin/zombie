# coding=utf8
from itertools import permutations
from functools import reduce
from fraction import Fraction

def muliplySets(set_a, set_b):
    '''Возвращает сочетания элементов списков

    Вызов muliplySets(('a', 'b'), ('c', 'd'))
        вернет (('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'))
    '''
    result = []
    for el_a in set_a:
        if type(el_a) != tuple:
            el_a = (el_a, )
        for el_b in set_b:
            result.append(tuple(sorted(el_a + (el_b, ))))
    return tuple(result)

def getPermutationProbability(permutations):
    '''Возвращает словарь вероятностей для списка tuple'ов

    Вызов getPermutationProbability(((1, 2), (1, 2), (1, 3)))
        вернет {(1, 2): 0.66, (1, 3): 0.33}
    '''
    probability = {}

    for sub_set in permutations:
        sub_set = tuple(sorted(sub_set))
        probability[sub_set] = probability.get(sub_set, 0) + 1

    total = sum(probability[key] for key in probability)
    for key in probability:
        # probability[key] /= float(total)
        probability[key] = Fraction(probability[key], total)

    return probability

def getFaceProbability(dice, faces_taken):
    '''Для списка кубиков возвращает вероятность сочетаний выпадающих граней'''
    face_set = []
    for die in dice:
        if die == 'red':
            face_set.append(('feet', ) * 2 + ('shot', ) * 3 + ('brain', ) * 1)
        elif die == 'yellow':
            face_set.append(('feet', ) * 2 + ('shot', ) * 2 + ('brain', ) * 2)
        elif die == 'green':
            face_set.append(('feet', ) * 2 + ('shot', ) * 1 + ('brain', ) * 3)
        else:
            raise Exception('Wrong color: %s' % die)

    set_mul = reduce(muliplySets, face_set)

    probability = getPermutationProbability(set_mul)

    return probability

def getStats(reds_count=3, yellows_count=4, greens_count=6, dice_taken=3):
    dice = (('red',) * reds_count +
            ('yellow',) * yellows_count +
            ('green',) * greens_count)

    probability = {}

    dice_prob = getPermutationProbability(permutations(dice, dice_taken))
    for dkey, dvalue in dice_prob.items():
        for fkey, fvalue in getFaceProbability(dkey, dice_taken).items():
            probability[fkey] = probability.get(fkey, 0.0) + dvalue * fvalue

    return probability

def printDictSorted(dictionary):
    maxlen = max(len(str(key)) for key in dictionary)
    for key, val in reversed(sorted(dictionary.items(), key=lambda x: x[1])):
        print('%*s: %.5f: %s' % (-maxlen, key, val, val))
    print

def main():
    # printDictSorted(getStats(3, 0, 0))
    # printDictSorted(getStats(0, 3, 0))
    # printDictSorted(getStats(0, 0, 3))
    printDictSorted(getStats())
    # printDictSorted(getStats(3, 4, 0))
    # printDictSorted(getStats(3, 0, 6))

if __name__ == '__main__':
    main()
