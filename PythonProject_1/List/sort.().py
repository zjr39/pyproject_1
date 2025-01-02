n = [1,1,1,12,21,2,2,2,2,2,3,4,5]
n.sort()
print(n)

n.sort(reverse=True)    #反序
print(sorted(n))        #临时排序可以直接调用print
print(sorted(n,reverse=True))   #临时反序

n.reverse()             #只是反转列表顺序
print(n)

print(len(n))           #列表长度，元素个数

#不能使用  print(n.sort())

#也不能使用   result=n.sort()
#           print(result)

#在 Python 中，列表的 sort 方法用于对列表本身进行原地排序，
# 也就是它会直接修改原列表中元素的顺序，而它的返回值是 None。
# 所以当你使用 print(n.sort()) 这样的语句时，
# 实际上是在尝试打印 sort 方法返回的 None，而不是排序后的列表内容。