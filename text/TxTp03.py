#!/usr/bin/python
#-*-coding: utf-8 -*-

import pythainlp
import pythainlp.util
from pythainlp.util import rank

fn = input('ชื่อ :: ')
ln = input('นามสกุล :: ')
bd = input('วันเกิด(วัน) :: ')

name = fn + ' ' + ln
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
    
    ch1 = ['ก','ด','ถ','ท','ภ','า','ำ','ฤ','่','ุ']
    ch2 = ['ข','ช','ง','บ','ป','เ','แ','้','ู']
    ch3 = ['ฆ','ฒ','ฑ','ต','๋']
    ch4 = ['ค','ธ','ญ','ร','ษ','ะ','โ','ั','ิ']
    ch5 = ['ฉ','ฌ','ณ','น','ม','ห','ฎ','ฮ','ฬ','ึ']
    ch6 = ['จ','ล','ว','อ','ใ']
    ch7 = ['ซ','ศ','ส','ี','ื','๊']
    ch8 = ['ผ','ฝ','พ','ฟ','ย','็']
    ch9 = ['ฏ','ฐ','ไ','์']


    num_fn = 0
    for i in fn:
        if i in ch1: num_fn +=1
        elif i in ch2: num_fn +=2
        elif i in ch3: num_fn +=3
        elif i in ch4: num_fn +=4
        elif i in ch5: num_fn +=5
        elif i in ch6: num_fn +=6
        elif i in ch7: num_fn +=7
        elif i in ch8: num_fn +=8
        elif i in ch9: num_fn +=9
        else: num_fn +=0
        
    num_ln = 0
    for i in ln:
        if i in ch1: num_ln +=1
        elif i in ch2: num_ln +=2
        elif i in ch3: num_ln +=3
        elif i in ch4: num_ln +=4
        elif i in ch5: num_ln +=5
        elif i in ch6: num_ln +=6
        elif i in ch7: num_ln +=7
        elif i in ch8: num_ln +=8
        elif i in ch9: num_ln +=9
        else: num_ln +=0

    num_name = num_fn + num_ln

    sum_fn = 0
    if num_fn > 100 and num_fn <110:
        sum_fn == (num_fn//100) + (num_fn%10)
    elif num_fn >= 110:
        sum_fn == (num_fn%100)
    else:sum_fn = num_fn

    sum_ln = 0
    if num_ln > 100 and num_ln <110:
        sum_ln == (num_ln//100) + (num_ln%10)
    elif num_ln >= 110:
        sum_ln == (num_ln%100)
    else:sum_ln = num_ln

    sum_name = 0
    if num_name > 100 and num_name <110:
        sum_name == (num_name//100) + (num_name%10)
    elif num_name >= 110:
        sum_name == (num_name%100)
    else:sum_name = num_name

    goodnum = [1,2,3,4,5,6,9,14,15,22,24,25,32,36,40,41,42,44,45,46,50,51,52,54,55,56,59,60,63,64,65,74,79,89,90,91,95,97,98,99,100]  

    print('"%s" ผลรวม : %d' %(fn,sum_fn),end =' ')
    if sum_fn in goodnum : print('เป็นมงคล')
    else : print('ไม่เป็นมงคล')

    print('"%s" ผลรวม : %d' %(ln,sum_ln),end =' ')
    if sum_ln in goodnum : print('เป็นมงคล')
    else :print('ไม่เป็นมงคล')
        
    print('"%s" ผลรวม : %d' %(name,sum_name),end =' ')
    if sum_name in goodnum : print('เป็นมงคล')
    else :print('ไม่เป็นมงคล')

    if sum_name not in goodnum or sum_ln not in goodnum or sum_fn not in goodnum:
        print('คนเกิดวัน "%s" ' %(bd), end = '')
        if ls != []:
            print('มีอักษรกาลกิณี',end= ' ')
            ch = rank(ls)
            ch_bad = ch.most_common()
            for i in ch_bad:
                print(i[0],end=' ')
        else : print('ไม่มีอักษรกาลกิณี')
          
else :
    print("ไม่ใช่ตัวอักษรภาษาไทย")









    
