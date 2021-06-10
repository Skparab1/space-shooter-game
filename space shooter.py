# space shooter
import time, secrets, socket
def printlines():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    print(line18[1:100]),print(line17[1:100]),print(line16[1:100]),print(line15[1:100]),print(line14[1:100]),print(line13[1:100]),print(line12[1:100]),print(line11[1:100]),print(line10[1:100]),print(line9[1:100]),print(line8[1:100]),print(line7[1:100]),print(line6[1:100]),print(line5[1:100]),print(line4[1:100]),print(line3[1:100]),print(line2[1:100]),print(line1[1:100])
    print('balls: ',balls)
    print(' '*pos,' ||')
    print(' '*pos,' ||')
    print(' '*pos,'<||>')
    print(' '*pos,'<__>')
def removeballs():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('o',' '),line2.replace('o',' '),line3.replace('o',' '),line4.replace('o',' '),line5.replace('o',' '),line6.replace('o',' '),line7.replace('o',' '),line8.replace('o',' '),line9.replace('o',' '),line10.replace('o',' '),line11.replace('o',' '),line12.replace('o',' '),line13.replace('o',' '),line14.replace('o',' '),line15.replace('o',' '),line16.replace('o',' '),line17.replace('o',' '),line18.replace('o',' ')
def removearrow():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('^',' '),line2.replace('^',' '),line3.replace('^',' '),line4.replace('^',' '),line5.replace('^',' '),line6.replace('^',' '),line7.replace('^',' '),line8.replace('^',' '),line9.replace('^',' '),line10.replace('^',' '),line11.replace('^',' '),line12.replace('^',' '),line13.replace('^',' '),line14.replace('^',' '),line15.replace('^',' '),line16.replace('^',' '),line17.replace('^',' '),line18.replace('^',' ')
def addball(pos,line):
    linepart1 = line[:pos-1]
    linepart2 = line[pos+1:]
    line = linepart1 + 'o ' + linepart2
    return line
def addarrow(pos,line):
    linepart1 = line[:pos-1]
    linepart2 = line[pos+1:]
    line = linepart1 + '^ ' + linepart2
    return line
def movelinesdown():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    removeballs()
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)
def moveup():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    linenum = 1 if ('^' in line1 ) else (2 if ('^' in line2 ) else (3 if ('^' in line3 ) else (4 if ('^' in line4 ) else (5 if ('^' in line5 ) else (6 if ('^' in line6 ) else (7 if ('^' in line7 ) else (8 if ('^' in line8 ) else (9 if ('^' in line9 ) else (10 if ('^' in line10 ) else (11 if ('^' in line11 ) else (12 if ('^' in line12 ) else (13 if ('^' in line13 ) else (14 if ('^' in line14 ) else (15 if ('^' in line15 ) else (16 if ('^' in line16 ) else (17 if ('^' in line17 ) else 18))))))))))))))))
    removearrow()
    line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addarrow(pos,line2) if linenum == 1 else line2),(addarrow(pos,line3) if linenum == 2 else line3),(addarrow(pos,line4) if linenum == 3 else line4),(addarrow(pos,line5) if linenum == 4 else line5),(addarrow(pos,line6) if linenum == 5 else line6),(addarrow(pos,line7) if linenum == 6 else line7),(addarrow(pos,line8) if linenum == 7 else line8),(addarrow(pos,line9) if linenum == 8 else line9),(addarrow(pos,line10) if linenum == 9 else line10),(addarrow(pos,line11) if linenum == 10 else line11),(addarrow(pos,line12) if linenum == 11 else line12),(addarrow(pos,line13) if linenum == 12 else line13),(addarrow(pos,line14) if linenum == 13 else line14),(addarrow(pos,line15) if linenum == 14 else line15),(addarrow(pos,line16) if linenum == 15 else line16),(addarrow(pos,line17) if linenum == 16 else line17),(addarrow(pos,line18) if linenum == 17 else line18)
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'o'+(' '*49))
pos = 50
balls = 25
while True:
    try:
        time.sleep(0.1)
        printlines()
        movelinesdown()
        moveup()
        if pos == 44 or pos == 46 or pos == 48 or pos == 50 or pos == 52 or pos == 54 or pos == 56:
            pos += 2
        if pos == 58:
            pos -= 1
        if pos == 43:
            pos += 1
        if pos == 57 or pos == 55 or pos == 53 or pos == 51 or pos == 49 or pos == 47 or pos == 45:
            pos -= 2
    except:
        line1 = addarrow(pos,line1)
    
    
