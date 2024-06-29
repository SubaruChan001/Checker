
import random
from new.luhn import checkLuhn

def cc_gen(cc, mes = 'x', ano = 'x', cvv = 'x',amount = 'x',): 
    if amount != 'x':
        amount = int(amount)
    else:
        amount = 1
    genrated = 0
    
    while(genrated < amount):
        genrated += 1
        s="0123456789"
        l = list(s)
        random.shuffle(l)
        result = ''.join(l)
        result = cc + result
        if cc[0] == "3":
            ccgen = result[0:15]
        else:
            ccgen = result[0:16]
        if mes == 'x':
            mesgen = random.randint(1,12)
            if len(str(mesgen)) == 1:
                mesgen = "0" + str(mesgen)
        else:
            mesgen = mes
        if ano == 'x':
            anogen = random.randint(2021,2029)
        else:
            anogen = ano
        if cvv == 'x':
            if cc[0] == "3":
                cvvgen = random.randint(1000,9999) 
            else:
                cvvgen = random.randint(100,999)
        else:
            cvvgen = cvv   
        # if not x: continue

        if ccgen and not checkLuhn(ccgen):
            pass
        if (ccgen, mesgen, anogen, cvvgen):
            lista = str(ccgen) +"|" + str(mesgen) + "|"+ str(anogen) + "|" + str(cvvgen) 
            


    return lista






def okcc(num):

    while True:
        ok = cc_gen(num)
        if checkLuhn(ok)==True:
            break
        else:
            continue
    return ok


