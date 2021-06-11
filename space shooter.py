# space shooter
import time, secrets, socket
def printlines():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    print(line18[1:100]),print(line17[1:100]),print(line16[1:100]),print(line15[1:100]),print(line14[1:100]),print(line13[1:100]),print(line12[1:100]),print(line11[1:100]),print(line10[1:100]),print(line9[1:100]),print(line8[1:100]),print(line7[1:100]),print(line6[1:100]),print(line5[1:100]),print(line4[1:100]),print(line3[1:100]),print(line2[1:100]),print(line1[1:100])
    print(' '*pos,' ||')
    print(' '*pos,' ||')
    print(' '*pos,'<||>')
    print(' '*pos,'<__>')
    print('balls: ',balls)
def removeballs():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('-',' '),line2.replace('-',' '),line3.replace('-',' '),line4.replace('-',' '),line5.replace('-',' '),line6.replace('-',' '),line7.replace('-',' '),line8.replace('-',' '),line9.replace('-',' '),line10.replace('-',' '),line11.replace('-',' '),line12.replace('-',' '),line13.replace('-',' '),line14.replace('-',' '),line15.replace('-',' '),line16.replace('-',' '),line17.replace('-',' '),line18.replace('-',' ')
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('o',' '),line2.replace('o',' '),line3.replace('o',' '),line4.replace('o',' '),line5.replace('o',' '),line6.replace('o',' '),line7.replace('o',' '),line8.replace('o',' '),line9.replace('o',' '),line10.replace('o',' '),line11.replace('o',' '),line12.replace('o',' '),line13.replace('o',' '),line14.replace('o',' '),line15.replace('o',' '),line16.replace('o',' '),line17.replace('o',' '),line18.replace('o',' ')
def rb(line):
    line = line.replace('-oo-','    ')
    return line
def scanforball(line):
    scanner,num = '',0
    while scanner != '-oo-':
        scanner = line[num]
    if '-oo-' in line:
        num = 999
    return num
def removearrow():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('^',' '),line2.replace('^',' '),line3.replace('^',' '),line4.replace('^',' '),line5.replace('^',' '),line6.replace('^',' '),line7.replace('^',' '),line8.replace('^',' '),line9.replace('^',' '),line10.replace('^',' '),line11.replace('^',' '),line12.replace('^',' '),line13.replace('^',' '),line14.replace('^',' '),line15.replace('^',' '),line16.replace('^',' '),line17.replace('^',' '),line18.replace('^',' ')
def addball(ballpos,line):
    linepart1 = line[:ballpos-1]
    linepart2 = line[ballpos+1:]
    line = linepart1 + '-oo- ' + linepart2
    return line
def addarrow(arrowpos,line):
    linepart1 = line[:arrowpos-1]
    linepart2 = line[arrowpos+1:]
    line = linepart1 + '^ ' + linepart2
    return line
def movelinesdown():
    global balls,ballpos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18 = True if '-oo-' in line1 else False,True if '-oo-' in line2 else False,True if '-oo-' in line3 else False,True if '-oo-' in line4 else False,True if '-oo-' in line5 else False,True if '-oo-' in line6 else False,True if '-oo-' in line7 else False,True if '-oo-' in line8 else False,True if '-oo-' in line9 else False,True if '-oo-' in line10 else False,True if '-oo-' in line11 else False,True if '-oo-' in line12 else False,True if '-oo-' in line13 else False,True if '-oo-' in line14 else False,True if '-oo-' in line15 else False,True if '-oo-' in line16 else False,True if '-oo-' in line17 else False,True if '-oo-' in line18 else False
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(ballpos,line1) if b2 == True else line1),(addball(ballpos,line2) if b3 == True else (rb(line2) if b2 == True else line2)),(addball(ballpos,line3) if b4 == True else (rb(line3) if b3 == True else line3)),(addball(ballpos,line4) if b5 == True else (rb(line4) if b5 == True else line4)),(addball(ballpos,line5) if b6 == True else (rb(line5) if b5 == True else line5)),(addball(ballpos,line6) if b7 == True else (rb(line6) if b6 == True else line6)),(addball(ballpos,line7) if b8 == True else (rb(line7) if b7 == True else line7)),(addball(ballpos,line8) if b9 == True else (rb(line8) if b8 == True else line8)),(addball(ballpos,line9) if b10 == True else (rb(line9) if b9 == True else line9)),(addball(ballpos,line10) if b11 == True else (rb(line10) if b10 == True else line10)),(addball(ballpos,line11) if b12 == True else (rb(line11) if b11 == True else line11)),(addball(ballpos,line12) if b13 == True else (rb(line12) if b12 == True else line12)),(addball(ballpos,line13) if b14 == True else (rb(line13) if b13 == True else line13)),(addball(ballpos,line14) if b15 == True else (rb(line14) if b14 == True else line14)),(addball(ballpos,line15) if b16 == True else (rb(line15) if b15 == True else line15)),(addball(ballpos,line16) if b17 == True else (rb(line16) if b16 == True else line16)),(addball(ballpos,line17) if b18 == True else (rb(line17) if b17 == True else line17)),(rb(line18) if b18 == True else line18)
def moveup():
    global balls,arrowpos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    linenum = 1 if ('^' in line1 ) else (2 if ('^' in line2 ) else (3 if ('^' in line3 ) else (4 if ('^' in line4 ) else (5 if ('^' in line5 ) else (6 if ('^' in line6 ) else (7 if ('^' in line7 ) else (8 if ('^' in line8 ) else (9 if ('^' in line9 ) else (10 if ('^' in line10 ) else (11 if ('^' in line11 ) else (12 if ('^' in line12 ) else (13 if ('^' in line13 ) else (14 if ('^' in line14 ) else (15 if ('^' in line15 ) else (16 if ('^' in line16 ) else (17 if ('^' in line17 ) else 18))))))))))))))))
    removearrow()
    line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addarrow(arrowpos,line2) if linenum == 1 else line2),(addarrow(arrowpos,line3) if linenum == 2 else line3),(addarrow(arrowpos,line4) if linenum == 3 else line4),(addarrow(arrowpos,line5) if linenum == 4 else line5),(addarrow(arrowpos,line6) if linenum == 5 else line6),(addarrow(arrowpos,line7) if linenum == 6 else line7),(addarrow(arrowpos,line8) if linenum == 7 else line8),(addarrow(arrowpos,line9) if linenum == 8 else line9),(addarrow(arrowpos,line10) if linenum == 9 else line10),(addarrow(arrowpos,line11) if linenum == 10 else line11),(addarrow(arrowpos,line12) if linenum == 11 else line12),(addarrow(arrowpos,line13) if linenum == 12 else line13),(addarrow(arrowpos,line14) if linenum == 13 else line14),(addarrow(arrowpos,line15) if linenum == 14 else line15),(addarrow(arrowpos,line16) if linenum == 15 else line16),(addarrow(arrowpos,line17) if linenum == 16 else line17),(addarrow(arrowpos,line18) if linenum == 17 else line18)
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'-oo-'+(' '*49))
pos = 50
ballpos = 50
arrowpos = 50
balls = 25
movedirection = 'right'
while True:
    ctry:
        time.sleep(0.1)
        if movedirection == 'right':
            pos += 1
            if pos == 55:
                movedirection = 'left'
        if movedirection == 'left':
            pos -= 1
            if pos == 45:
                movedirection = 'right'
        linenum = 1 if ('-oo-' in line1 ) else (2 if ('-oo-' in line2 ) else (3 if ('-oo-' in line3 ) else (4 if ('-oo-' in line4 ) else (5 if ('-oo-' in line5 ) else (6 if ('-oo-' in line6 ) else (7 if ('-oo-' in line7 ) else (8 if ('-oo-' in line8 ) else (9 if ('-oo-' in line9 ) else (10 if ('-oo-' in line10 ) else (11 if ('-oo-' in line11 ) else (12 if ('-oo-' in line12 ) else (13 if ('-oo-' in line13 ) else (14 if ('-oo-' in line14 ) else (15 if ('-oo-' in line15 ) else (16 if ('-oo-' in line16 ) else (17 if ('-oo-' in line17 ) else 18))))))))))))))))
        printlines()
        movelinesdown()
        moveup()
        print(pos)
        #moveup()
        lb = line1 if ('-oo-' in line1 ) else (line1 if ('-oo-' in line2 ) else (line2 if ('-oo-' in line3 ) else (line3 if ('-oo-' in line4 ) else (line4 if ('-oo-' in line5 ) else (line5 if ('-oo-' in line6 ) else (line6 if ('-oo-' in line7 ) else (line7 if ('-oo-' in line8 ) else (line8 if ('-oo-' in line9 ) else (line9 if ('-oo-' in line10 ) else (line10 if ('-oo-' in line11 ) else (line11 if ('-oo-' in line12 ) else (line12 if ('-oo-' in line13 ) else (line13 if ('-oo-' in line14 ) else (line14 if ('-oo-' in line15 ) else (line15 if ('-oo-' in line16 ) else (line16 if ('-oo-' in line17 ) else (line17 if ('-oo-' in line18 ) else line18)))))))))))))))))
        lbb = line1 if ('-oo-' in line1 ) else (line1 if ('-oo-' in line2 ) else (line1 if ('-oo-' in line3 ) else (line2 if ('-oo-' in line4 ) else (line3 if ('-oo-' in line5 ) else (line4 if ('-oo-' in line6 ) else (line5 if ('-oo-' in line7 ) else (line6 if ('-oo-' in line8 ) else (line7 if ('-oo-' in line9 ) else (line8 if ('-oo-' in line10 ) else (line9 if ('-oo-' in line11 ) else (line10 if ('-oo-' in line12 ) else (line11 if ('-oo-' in line13 ) else (line12 if ('-oo-' in line14 ) else (line13 if ('-oo-' in line15 ) else (line14 if ('-oo-' in line16 ) else (line15 if ('-oo-' in line17 ) else (line16 if ('-oo-' in line18 ) else line18)))))))))))))))))
        if ('^' == lb[arrowpos+1] or '^' == lb[arrowpos+2] or '^' == lb[arrowpos+3] or '^' == lb[arrowpos+4]) or ('^' == lbb[arrowpos+1] or '^' == lbb[arrowpos+2] or '^' == lbb[arrowpos+3] or '^' == lb[arrowpos+4]):
            removeballs()
            removeballs()
            removearrow()
            line18 = addball(pos,line18)
        if '-oo-' in line1:
            print('you have lost')
            break
    except:
        arrowpos = pos + 5
        line1 = addarrow(arrowpos,line1)
        balls -= 1
    
    
