def is_inside(pointz, orzz):
    
    [xA,yA] = pointz
    [kx, ky, xS, yS] = orzz
    if (kx <= xA <= kx + xS) and (ky <= yA <= ky + yS):
        return(True)
    else:
        return(False)
###################

#day la phan kiem tra lai code!!
aaa = is_inside([200,120],[140, 60,100,200])
if aaa == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
