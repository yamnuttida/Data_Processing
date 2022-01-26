import pythainlp
import pythainlp.util

fn = input('ชื่อ :: ')
#ln = input('นามสกุล :: ')
bd = input('วันเกิด(วัน) :: ')

name = fn #+ ln 
if pythainlp.util.isthai(name, ignore_chars=" ") == True :
    
    ls = []
    for i in name:
        if i== 'ก' or i=='ข' or i=='ค' or i=='ฆ' or i=='ง' :
            if bd == "อังคาร" :ls.append(i)
        elif i=='จ' or i=='ฉ' or i=='ช' or i=='ซ' or i=='ฌ' or i=='ญ' :
            if bd == "พุธ" :ls.append(i)
        elif i=='ฎ' or i=='ฏ' or i=='ฑ' or i=='ฒ' or i=='ฐ' or i=='ณ' :
            if bd == "เสาร์" :ls.append(i)
        elif i=='ด' or i=='ต' or i=='ถ' or i=='ท' or i=='ธ' or i=='น' :
            if bd == "พฤหัสบดี" :ls.append(i)
        elif i=='ป' or i=='ผ' or i=='ฝ' or i=='พ' or i=='ฟ' or i=='ภ' or i=='ม' :
            if bd == "พุธ" :ls.append(i)
        elif i=='ย' or i=='ล' or i=='ว' or i=='ร' :
            if bd == "ศุกร์" :ls.append(i)
        elif i=='ศ' or i=='ส' or i=='ษ' or i=='ห' or i=='ฮ' or i=='ฬ' :
            if bd == "อาทิตย์" :ls.append(i)
        else :
            if bd == "จันทร์" :ls.append(i)

            
    num_fn = 0
    for i in fn:
        if i== 'ก' or i=='ด' or i=='ถ' or i=='ท' or i=='ภ' or i== 'า' or i=='ำ' or i=='ฤ' or i=='่' or i=='ุ' : 
            num_fn += 1
        elif i== 'ข' or i=='ช' or i=='ง' or i=='บ' or i=='ป' or i== 'เ' or i=='แ' or i=='้' or i=='ู' : 
            num_fn += 2
        elif i== 'ฆ' or i=='ฒ' or i=='ฑ' or i=='ต' or i=='๋' : 
            num_fn += 3
        elif i== 'ค' or i=='ธ' or i=='ญ' or i=='ร' or i=='ษ' or i== 'ะ' or i=='โ' or i=='ั' or i=='ิ' : 
            num_fn += 4
        elif i== 'ฉ' or i=='ฌ' or i=='ณ' or i=='น' or i=='ม' or i== 'ห' or i=='ฎ' or i=='ฮ' or i=='ฬ' or i=='ึ' : 
            num_fn += 5
        elif i== 'จ' or i=='ล' or i=='ว' or i=='อ' or i=='ใ' : 
            num_fn += 6
        elif i== 'ซ' or i=='ศ' or i=='ส' or i=='ี' or i=='ื' or i=='๊' : 
            num_fn += 7
        elif i== 'ผ' or i=='ฝ' or i=='พ' or i=='ฟ' or i=='ย' or i=='็' : 
            num_fn += 8
        elif i== 'ฏ' or i=='ฐ' or i=='ไ' or i=='์' : 
            num_fn += 9
        else: num_fn += 0
    '''
    num_ln = 0
    for i in fname:
        if i== 'ก' or i=='ด' or i=='ถ' or i=='ท' or i=='ภ' or i== 'า' or i=='ำ' or i=='ฤ' or i=='่' or i=='ุ' : 
            num_ln += 1
        elif i== 'ข' or i=='ช' or i=='ง' or i=='บ' or i=='ป' or i== 'เ' or i=='แ' or i=='้' or i=='ู' : 
            num_ln += 2
        elif i== 'ฆ' or i=='ฒ' or i=='ฑ' or i=='ต' or i=='๋' : 
            num_ln += 3
        elif i== 'ค' or i=='ธ' or i=='ญ' or i=='ร' or i=='ษ' or i== 'ะ' or i=='โ' or i=='ั' or i=='ิ' : 
            num_ln += 4
        elif i== 'ฉ' or i=='ฌ' or i=='ณ' or i=='น' or i=='ม' or i== 'ห' or i=='ฎ' or i=='ฮ' or i=='ฬ' or i=='ึ' : 
            num_ln += 5
        elif i== 'จ' or i=='ล' or i=='ว' or i=='อ' or i=='ใ' : 
            num_ln += 6
        elif i== 'ซ' or i=='ศ' or i=='ส' or i=='ี' or i=='ื' or i=='๊' : 
            num_ln += 7
        elif i== 'ผ' or i=='ฝ' or i=='พ' or i=='ฟ' or i=='ย' or i=='็' : 
            num_ln += 8
        elif i== 'ฏ' or i=='ฐ' or i=='ไ' or i=='์' : 
            num_ln += 9
        else: num_ln += 0
        
    sumnum = num_fn + num_ln

    '''
    if num_fn > 100 and num_fn <110:
        num_fn == (sumnum_n//100) + (sumnum_n%10)
    elif num_fn >= 110:
        num_fn == (sumnum_n%100)

    goodnum = [1,2,3,4,5,6,9,14,15,22,24,25,32,36,40,41,42,44,45,46,50,51,52,54,55,56,59,60,63,64,65,74,79,89,90,91,95,97,98,99,100]  
    if num_fn in goodnum :
        print('คนเกิดวัน%s ชื่อ %s ผลรวม %d' %(bd,fn,num_fn), 'เป็นมงคล')
    else :
        print('คนเกิดวัน%s ชื่อ %s ผลรวม %d' %(bd,fn,num_fn), 'ไม่มงคล', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
        
    '''


    print('คนเกิดวัน%s ชื่อ %s ผลรวม %d' %(bd,name,sumnum),end = ' ')

    if bd == "อาทิตย์" and sumnum == 6:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif bd == "จันทร์" and sumnum == 1:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif bd == "อังคาร" and sumnum == 2:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif bd == "พุธ" and sumnum == 3 or sumnum == 5:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif bd == "พฤหัสบดี" and sumnum == 7:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif bd == "ศุกร์" and sumnum == 8:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif bd == "เสาร์" and sumnum == 4:
        print('ไม่มงคล!', end =' ')
        if ls != []: print('อักษรกาลกิณี', ' '.join(ls))
    elif ls != []: print('ไม่มงคล! อักษรกาลกิณี', ' '.join(ls))
    else: print('มงคล!!!')

    '''
else :
    print("ไม่ใช่ตัวอักษรภาษาไทย")
