# #creates a list containing 5 lists, each of 8 items, all set to 0
# w, h = 8, 5 #w=width/columns, h=height/rows
# Matrix=[[0 for x in range(w)] for y in range(h)]
# Matrix[0][0]=1
# Matrix[6][0]=3 #range error! there are only 5 rows
# Matrix[0][0]=1 #valid
# print(Matrix[0][0]) #print 1
# row, col= 0, 6
# print(Matrix[row][col] #prints 3; be careful with indexing!)

#podpowiedz 2
# import numpy
# import pprint
# pp= pprint.PrettyPrinter()
# matrix1=numpy.zeros((5,5))
# pp.pprint(matrix1)
# matrix2=numpy.matrix([[1,2],[3,4]])
# pp.pprint(matrix2)
# matrix3=numpy.matrix('1 2; 3 4')
# matrix4=numpy.arange(25).reshape((5, 5))
# matrix5=numpy.ndarray((5,5))

#wyraz = input("Podaj pierwszy term: ")
# wyraz=input()
# wyraz=wyraz.strip()
# #print ('Ten wyraz został wprowadzony:', wyraz)
# wyraz2=input()
# # wyraz2 = input("Podaj drugi term: ")
# wyraz2=wyraz2.strip()
# #print ('Ten wyraz został wprowadzony:', wyraz2)

# def levenshtein(term, term1):
#     w, h = len(term) + 1, len(term1) + 1
#     matrix = []
#     for _ in range(h):
#         row = [0] * w
#         matrix.append(row)

#     for i in range(w):
#         matrix[0][i] = i
#     for j in range(h):
#         matrix[j][0] = j

#     for i in range(1, h):
#         for j in range(1, w):
#             jedn = 0 if term[j - 1] == term1[i - 1] else 1
#             matrix[i][j] = min(
#                 matrix[i - 1][j] + 1,
#                 matrix[i][j - 1] + 1,
#                 matrix[i - 1][j - 1] + jedn 
#             )

#     return matrix[h - 1][w - 1]

# odl = levenshtein(wyraz, wyraz2)
# print(odl)


import numpy as np

def levenshtein(term, term1):
    w, h = len(term) + 1, len(term1) + 1
    matrix = np.zeros((h, w), dtype=int)

    for i in range(h):
        matrix[i][0] = i

    for j in range(w):
        matrix[0][j] = j

    for i in range(1, h):
        for j in range(1, w):
            jedn = 0 if term[j - 1] == term1[i - 1] else 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + jedn
            )

    return matrix[h - 1][w - 1]

wyraz = input().strip()
# print('Ten wyraz został wprowadzony:', wyraz)
wyraz2 = input().strip()
# print('Ten wyraz został wprowadzony:', wyraz2)

odl = levenshtein(wyraz, wyraz2)
print(odl)
