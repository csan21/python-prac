# string permutations
# range() interates through sequence of numbers
# len() iterates through sequence using index
def permute(str)
    if len(str) == 1:
        return [str]

    result = []
    for perm in permute(str[1:]):
        for i in range(len(str)):
            result.append(perm[:i] + str[0:1] + perm[i:])

    return result
# print(permute('wow')) output: ['wow', 'oww', 'oww', 'wwo', 'wwo', 'wow']
