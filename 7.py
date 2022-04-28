def countsteps(n):
  if (n<0):
    return 0
  if (n==0):
    return 1
  else:
    return countsteps(n-1) + countsteps(n-2) + countsteps(n-3)



def fastercount(n):
  rev = [0] * (n+3)
  rev[0] = 1
  rev[1] = 1
  rev[2] = 2
  for i in range (3, n+1):
    return rev[n-1] + rev[n-2] + rev[n-3]
print(fastercount(4))