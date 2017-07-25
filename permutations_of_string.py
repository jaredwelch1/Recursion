

'''
string[] permutations( string s )

insert our current starting character into every spot
of the substring, for every substring. This gives all possible
permutations for that string. Recursion allows this to
lead to base case of empty

Example:

abc
char1: a
substring: bc

{bc, cb} = permutations(bc)

now we insert char1 into spots of substrings

{abc, bac, bca, acb, cab, cba}

'''

def find_permutations( s ):
    permutations = []

    # base case of empty substring
    if not s:
        permutations.append("")
        return permutations

    # get first char of string s
    char1 = s[0][0]

    # get the remaining substring and get its possible permutations
    remainder = s[1:]
    words = find_permutations(remainder)

    for word in words:
        for i in range(len(word)+1):
            permutations.append(insert_char_at(word, char1, i))
    return permutations

def insert_char_at( word, char, index ):
    start = word[0:index]
    end = word[index:]
    return str(start + char + end)

if __name__ == "__main__":
    s = str(raw_input('Please provide a string to permutate(?): '))

    combos = find_permutations(s)
    print(str(combos))
