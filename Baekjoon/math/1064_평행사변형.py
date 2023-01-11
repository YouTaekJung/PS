xa, ya, xb, yb, xc, yc = map(int, input().split())

ans = 0
if xa == xb == xc or ya == yb == yc:
    ans = -1
elif ya-yb != 0 and ya-yc != 0 and yb-yc != 0 and \
        (xa-xb)/(ya-yb) == (xb-xc)/(yb-yc) == (xa-xc)/(ya-yc):
    ans = -1
else:
    dab = ((xa-xb)**2 + (ya-yb)**2) ** (1/2)
    dbc = ((xb-xc)**2 + (yb-yc)**2) ** (1/2)
    dca = ((xc-xa)**2 + (yc-ya)**2) ** (1/2)

    ans = (max(dab, dbc, dca) - min(dab, dbc, dca)) * 2
print(ans)
