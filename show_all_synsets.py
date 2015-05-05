# The following code show the first 20 elements in
# wn.all_synsets('n')

stop = 0
for x in wn.all_synsets('n'):
  if stop == 20:
    break
  else:
    print(x)
    stop += 1
