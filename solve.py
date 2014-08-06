import memo

# 1: blue, 2: yellow, 3: green, 4: red
next = {'1': '2', '2': '3', '3': '4', '4': '.'}

def solve(level, width, moves):
    #print('solve', level, moves)
    if moves == 0:
        # Test for empty board
        for c in level:
            if c != '.':
                return None
        return []
    
    def popdir(inrange, coord):
        i = 1
        while inrange(coord(i)):
            if poplevel[coord(i)] != '.':
                pop(coord(i))
                return
            i += 1

    def pop(i):
        balls = [(None, lambda _: True, lambda _: i)]
        while len(balls) > 0:
            newballs = []
            for j, inrange, pos in balls:
                p = pos(j)
                if inrange(p) and p >= 0 and p < len(poplevel):
                    if poplevel[p] == '.':
                        newballs.append((j+1, inrange, pos))
                    else:
                        poplevel[p] = next[poplevel[p]]

                        # If popped (max level), pop neighbours 
                        if poplevel[p] == '.':
                            # Capture value of p in lambda
                            newballs.append((1, lambda x,p=p : x//width == p//width, lambda k,p=p: p-k))       # Left
                            newballs.append((1, lambda x,p=p : x//width == p//width, lambda k,p=p: p+k))       # Right
                            newballs.append((1, lambda _: True, lambda k,p=p: p-k*width))    # Up
                            newballs.append((1, lambda _: True, lambda k,p=p: p+k*width))    # Down
            balls = newballs
            
    empty = True
    for i in range(len(level)):
        # Skip empty
        if level[i] == '.':
            continue
        
        empty = False
        
        poplevel = level[:]
        pop(i)
        #print('poplev', poplevel) 
        res = solve(poplevel[:], width, moves-1)
        #print('res', res)
        
        if res is not None:
            return [(i, poplevel)] + res
    if empty:
        return []
    return None

def solveboard(board, width, moves):
    sol = solve(list(board), width, moves)

    if sol is None:
        print('No solution found!')
        return
    
    def formboard(b):
        return '|'.join([b[start:start+width] for start in range(0, len(b), width)])

    print('ROW\tCOL\tBOARD')
    print(' \t \t|{}|'.format(formboard(board)))
    for step,board in sol:
        row = step // width + 1
        col = step %  width + 1
        print('{}\t{}\t|{}|\t::{}'.format(row, col, formboard(''.join(board)), ''.join(board)))

