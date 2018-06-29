
# a.Return only those items that are present in both lists.
# b.Return only those items that are present in the first list, but not in the second.
# c.Return only those items that are present in the second list, but not in the first.
# d.Return items that are present in either the first or the second list.
# e.Return items from the first list that are not eliminated by a matching element in the second list. In this case, an item in the second list “knocks out” just one matching item in the first list. This operation is sometimes called bagdiff. For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]

def merge(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          
            result.extend(ys[yi:]) 
            return result          

        if yi >= len(ys):          
            result.extend(xs[xi:])
            return result
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

# a.Return only those items that are present in both lists.
def merge_a(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs) or yi >= len(ys):          
            return result          

        if xs[xi] < ys[yi]:
            # result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            # result.append(ys[yi])
            yi += 1
        else:
            if len(result)==0 or ys[yi] != result[-1]:
                result.append(ys[yi])
            yi += 1
            xi += 1

# b.Return only those items that are present in the first list, but not in the second.
def merge_b(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          
            return result          

        if yi >= len(ys):          
            result.extend(xs[xi:])
            return result

        if xs[xi] < ys[yi]:
            if len(result)==0 or xs[xi] != result[-1]:
                result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1

# c.Return only those items that are present in the second list, but not in the first.
def merge_c(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):    
            result.extend(ys[yi:])       
            return result          

        if yi >= len(ys):          
            return result

        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            if len(result)==0 or ys[yi] != result[-1]:
                result.append(ys[yi])
            yi += 1
        else:
            xi += 1
            yi += 1

# d.Return items that are present in either the first or the second list.
def merge_d(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          
            result.extend(ys[yi:]) 
            return result          

        if yi >= len(ys):          
            result.extend(xs[xi:])
            return result
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1
        else:
            yi += 1
            xi += 1

# e.Return items from the first list that are not eliminated by a 
# matching element in the second list. In this case, an item in the 
# second list “knocks out” just one matching item in the first list. 
# This operation is sometimes called bagdiff. 
# For example bagdiff([5,7,11,11,11,12,13], [7,8,11]) would return [5,11,11,12,13]

def merge_e(xs, ys):
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          
            return result          

        if yi >= len(ys):          
            result.extend(xs[xi:])
            return result

        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


xs = [1,2,2,3,4,5,6,9]
ys = [1,2,2,4,8,8,9,10,12]
            
print(merge_a(xs,ys))
print(merge_b(xs,ys))
print(merge_c(xs,ys))
print(merge_d(xs,ys))
xs = [5,7,11,11,11,12,13]
ys =  [7,8,11]
print(merge_e(xs,ys))