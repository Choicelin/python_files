invited_names = ['chenjiangqun', 'wangjuling', 'linyunjian']
print invited_names
cannot_come = invited_names.pop(2)
invited_names.append('linyunjian')
print invited_names
invited_names.insert(0, 'linzixiang')
invited_names.insert(2, 'chennanzheng')
invited_names.append('chensongjun')
print invited_names
del invited_names[2]
invited_names.pop()
invited_names.pop()
invited_names.pop()
print invited_names
invited_names.remove('linzixiang')
invited_names.remove('chenjiangqun')
print invited_names
print len(invited_names)