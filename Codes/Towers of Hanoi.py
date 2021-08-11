def moveTower(h,fp,tp,mp):
    if(h>=1):
        moveTower(h-1,fp,mp,tp)
        moveDisk(fp,tp,h)
        moveTower(h-1,mp,tp,fp)
def moveDisk(fp,tp,h):
    print("Moving disk",h,"from",fp,"to",tp)
moveTower(4,"A","C","B")
