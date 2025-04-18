import random

# progression: I I6 IV V vi ii6 I64 V V7 I
# chords: I I6 I64 ii6 iii IV IV64 V V7 vi vii vii6

notes_I = ["CEGC", "CGEC", "ECGC", "GCEC", "EGCC", "GECC"]
notes_I6 = ["CCGE", "CGCE", "GCCE"]
notes_I64 = ["CEGG", "CGEG", "ECGG", "EGCG", "GCEG", "GECG"]
notes_ii6 = ["DFAF", "DAFF", "FDAF", "FADF", "ADFF", "AFDF"]
notes_iii = ["EGBE", "EBGE", "GEBE", "GBEE", "BEGE", "BGEE"]
notes_IV = ["FACF", "FCAF", "CFAF", "CAFF", "AFCF", "ACFF"]
notes_IV64 = ["FACC", "FCAC", "CFAC", "CAFC", "AFCC", "ACFC"]
notes_V = ["GBDG", "GDBG", "BDGG", "BGDG", "DGBG", "DBGG"]
notes_V7 = ["BDFG", "BFDG", "DBFG", "DFBG", "FDBG", "FBDG"]
notes_vi = ["ACEA", "AECA", "CAEA", "CEAA", "EACA", "ECAA"]
notes_vii = ["BDFB", "BFDB", "DBFB", "DFBB", "FBDB", "FDBB"]
notes_vii6 = ["BDFD", "BFDD", "DBFD", "DFBD", "FBDD", "FDBD"]
chords = [notes_I, notes_I6, notes_I64, notes_ii6, notes_iii, notes_IV, notes_IV64, notes_V, notes_V7, notes_vi, notes_vii, notes_vii6]

for i in range(10):
    print(f"Options for Chord {i+1}:")
    
    for j in range(len(chords)):
        v = random.randint(0, 5)
        if j == 1:
            v = v % 3
    
        print(chords[j][v])   

