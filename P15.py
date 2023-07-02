def input_s(s,ln):
    for i in range(0,ln):
        n=int(input("Enter the element: "))
        s.append(n)
def subsets(s):
    sub=[[]]
    for n in s:
        n_sub=[]
        for su in sub:
            n_sub.append(su+[n])
        sub.extend(n_sub)
    return sub
def ss_subset(subsets,ln,sums):
    for i in range(0,ln):
        sum=0
        for j in subsets[i]:
            sum=sum+j
        if sum==sums:
            print(subsets[i])
def main():
    ln=int(input("Enter the length of the set: "))
    s=[]
    input_s(s,ln)
    subset=subsets(s)
    sum=int(input("Enter the sum of subsets: "))
    print(sum)
    ss_subset(subset,len(subset),sum)
if __name__=="__main__":
    main()