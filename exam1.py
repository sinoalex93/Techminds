# ####metrix
# A = [
#     [1, 2],
#     [3, 4]
# ]
#
# B = [
#     [5, 6],
#     [7, 8]
# ]
#
# result = []
#
# for i in range(2):
#     row = []
#     for j in range(2):
#         row.append(A[i][j] + B[i][j])
#     result.append(row)
#
# print(result)

#text = "A l e x"
#
# result = ""
#
# for i in text:
#     if i != " ":
#         result = result + i
#
# print(result)

#
# ####diamond
# n = 4
#
# # Top half
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#
#     for j in range(1, i + 1):
#         print(j, end="")
#
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#
#     print()
#
# # Bottom half
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#
#     for j in range(1, i + 1):
#         print(j, end="")
#
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#
#     print()



####unique
# text = input("Enter a string: ")
#
# unique = True
#
# for i in range(len(text)):
#     for j in range(i + 1, len(text)):
#         if text[i] == text[j]:
#             unique = False
#             break
#
#     if unique == False:
#         break
#
# if unique:
#     print("String is unique")
# else:
#     print("String is not unique")

