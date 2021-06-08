def NGE(arr, n):
    st = []
    ans = []
    for i in range(n):
        while len(st) > 0 and st[-1] <= arr[i]:
            ans.append(arr[i] - st[-1])
            st.pop()
        st.append(arr[i])

    return ans


tcs = int(input())

for _ in range(tcs):
    n = int(input())
    a = list(map(int, input().split()))
    
    a1 = NGE(a, n)
    a2 = NGE(a[::-1], n)[::-1]
    an = set(a1+a2)
    
    print(len(an))