import pythainlp
import pythainlp.util
name = input('ชื่อ :: ')
birthday = input('วันเกิด(วัน) :: ')

numname = 0
ls = []
for i in name:
    if pythainlp.util.isthai(i, ignore_chars=" ") == True :
        if i== 'ก' or i=='ข' or i=='ค' or i=='ฆ' or i=='ง' :
            numname += 15
            if birthday == "อังคาร" :ls.append(i)
        elif i=='จ' or i=='ฉ' or i=='ช' or i=='ซ' or i=='ฌ' or i=='ญ' :
            numname += 8
            if birthday == "พุธ" :ls.append(i)
        elif i=='ฎ' or i=='ฏ' or i=='ฑ' or i=='ฒ' or i=='ฐ' or i=='ณ' :
            numname += 17
            if birthday == "เสาร์" :ls.append(i)
        elif i=='ด' or i=='ต' or i=='ถ' or i=='ท' or i=='ธ' or i=='น' :
            numname += 10
            if birthday == "พฤหัสบดี" :ls.append(i)
        elif i=='ป' or i=='ผ' or i=='ฝ' or i=='พ' or i=='ฟ' or i=='ภ' or i=='ม' :
            numname += 19
            if birthday == "พุธ" :ls.append(i)
        elif i=='ย' or i=='ล' or i=='ว' or i=='ร' :
            numname += 12
            if birthday == "ศุกร์" :ls.append(i)
        elif i=='ศ' or i=='ส' or i=='ษ' or i=='ห' or i=='ฮ' or i=='ฬ' :
            numname += 21
            if birthday == "อาทิตย์" :ls.append(i)
        else :
            numname += 6
            if birthday == "จันทร์" :ls.append(i)
    else:
        break
        
sumnum = 0
sumnum_n = numname
indexnum = len(str(numname))
while indexnum != 1 :
    sumnum = (sumnum_n//100) + (sumnum_n%100//10) + (sumnum_n%10)
    sumnum_n = sumnum
    indexnum = len(str(sumnum))

if sumnum == 9 : sumnum = 8

print('คนเกิดวัน%s ชื่อ %s ผลรวม %d' %(birthday,name,sumnum),end = ' ')

if birthday == "อาทิตย์" and sumnum == 6:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif birthday == "จันทร์" and sumnum == 1:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif birthday == "อังคาร" and sumnum == 1:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif birthday == "พุธ" and sumnum == 1:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif birthday == "พฤหัสบดี" and sumnum == 1:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif birthday == "ศุกร์" and sumnum == 1:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif birthday == "เสาร์" and sumnum == 1:
    print('ไม่มงคล!', end =' ')
    if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
elif ls != []: print('ไม่มงคล! อักษรกาลกิณี', ' '.join(ls))
else: print('มงคล!!!')


    
