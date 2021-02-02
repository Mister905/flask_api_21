friends = {'Bob', 'Rolf', 'Anne', 'Tim'}
abroad = {'Bob', 'Anne'}

local_friends = friends.difference(abroad)
print(local_friends)

total_friends = local_friends.union(abroad)
print(total_friends)


art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)
print(both)