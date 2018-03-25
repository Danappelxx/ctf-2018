#alphabet
permissible = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-|'

#contain an index
def contain(pos, shift, mx):
    if( (pos + shift) <= (mx - 1) ):
        return pos + shift
    else:
        round = (pos + shift) - (mx - 1)
        return round

#encode a string
def encode(inp):
    output = ''
    sh = 0
    for ch in inp:
        pos = permissible.index(ch)
        c = contain(pos, sh, len(permissible))
        nC = permissible[c]
        sh = pos
        output += nC
    return output
