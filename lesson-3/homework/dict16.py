dc = {1: {1: 2}, 2: 'a'}
ok = 1
for i in dc.values():
    try:
        x = i.items()
        print(True)
        ok = 0
    except:
        pass
if ok: print(False)