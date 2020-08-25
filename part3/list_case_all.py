game = ['paopao', 'tianlong', 'moshou']
game.append('jiansan')
game.remove('jiansan')
game.pop(0)
del game[0]
print len(game)
game.insert(1, 'shishenzhe')
game.sort()
game.sort(reverse=True)
sorted(game)
sorted(game, reverse=True)
game.reverse()
print game