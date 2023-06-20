s = int(input())
vid1 = (s-s//3600*3600)//60
vid2 = (s-s//3600*3600)%60
print(s//3600, vid1, vid2)
