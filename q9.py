strg=input()
strg_order_list=[]
for i in range(len(strg)):
    strg_order=ord(strg[i])
    strg_order_list.append(strg_order)

strg_order_list.sort()
reqStrg=""
for i in range(len(strg)):
    reqStrg+=chr(strg_order_list[i])
print(reqStrg)