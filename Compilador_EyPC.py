from math import ceil

def Elemento1(array, varB, x=0):
    if x >= 1:
        op, a1 = Encontrar_opCpde(array[0].upper(), None, '0', varB)
        return array[0].upper(), op, a1
    else:
        return array[0].upper()

def Elemento2(array, varB, x=0):
    if x == 1:
        op, a1 = Encontrar_opCpde(array[0].upper(), array[1], '0', varB)
    elif x == 2:
        op, a1 = Encontrar_opCpde(array[0].upper(), '0', array[1], varB)
    elif x == 3:
        op, a1 = Encontrar_opCpde(array[1].upper(), None, array[1], varB)
    return array[0].upper(), array[1], op, a1

def Elemento3(array, varB, x=0):
    if x == 1:
        op, a1 = Encontrar_opCpde(array[0].upper(), array[1], '0', varB)
        return array[0].upper(), array[1], array[2], op, a1
    elif x == 2:
        op, a1 = Encontrar_opCpde(array[1].upper(), array[2], '0', varB)
        return array[0], array[1].upper(), array[2], op, a1

def Elemento4(array, varB):
    op, a1 = Encontrar_opCpde(array[1].upper(), array[2], '0', varB)
    return array[0], array[1], array[2], array[3], op, a1

def contLineas(codigo):
    return len(codigo.readlines())

def apartarMem(numLineas):
    eTq=[[numLineas]*2 for x in range(numLineas)]                                                                          
    varB=[[numLineas]*2 for x in range(numLineas)]
    programaLin=list(range(numLineas))
    error=[[numLineas]*2 for x in range(numLineas)]
    opCode=[[numLineas]*3 for x in range(numLineas)]
    momento_dirCcion=[[numLineas]*2 for x in range(numLineas)]
    dirMom_op=[[numLineas]*2 for x in range(numLineas)]
    dirT=[[numLineas]*2 for x in range(numLineas)]
    eTq2=[[numLineas]*6 for x in range(numLineas)]
    Ar_2=[[50]*2 for x in range(50)]
    return eTq,varB,programaLin,opCode,momento_dirCcion,dirMom_op,dirT,eTq2,Ar_2,error


def complementos(dig):
    binary = bin(dig)[2:]
    binary = binary.zfill(8)
    
    total = 'r'
    for bit in binary:
        if bit == '0':
            y = '1'
        elif bit == '1':
            y = '0'
        total += y
    
    total = total[1:]
    total = int(total, 2) + 1
    total = bin(total)[2:]
    total = str(format(int(total[:4], 2), 'X')) + str(format(int(total[4:], 2), 'X'))
    
    return total

def elemxLinea(lin):                                                                                                           
    return len(lin.split())

def numPuntos(dir):
    regla=0
    if dir.count(".")>=1:                                                                                                              
        while regla>=0:
            if dir[regla]==".":
                dir=dir[:regla]
                regla=-1
            else:
                regla+=1
    return dir

def numdX(opCode):
    regla=0
    if opCode.count("X")>=1:                                                                                                                 
        while regla>=0:
            if opCode[regla]=="X":
                opCode=opCode[:regla]
                regla=-1
            else:
                regla+=1
    return opCode

def numAsteri(lin):
    regla=0
    if lin.count("*")>=1:                                                                                                              
        while regla>=0:
            if lin[regla]=="*":
                lin=lin[:regla]
                regla=-1
            else:
                regla+=1
    return lin

def idenHasht(dir):                                                                                                               
    regla=0
    a1=0
    if dir[0]=='#':
        while regla>=0:
            if dir[regla]=="#":
                dir=dir[regla+1:]
                regla=-1
                a1=3
            else:
                regla+=1
    return dir,a1

def Encontrar_opCpde(array, dir, eTq,varB=0):
    simb=[[' ',"20"],['!',"21"],['"',"22"],['#',"23"],['$',"24"],['%',"25"],['&',"26"],["'","27"],['(',"28"],[')',"29"],['*',"2A"],['+',"2B"],[',',"2C"],['-',"2D"],['.',"2E"]
             ,['/',"2F"],['0',"30"],['1',"31"],['2',"32"],['3',"33"],['4',"34"],['5',"35"],['6',"36"],['7',"37"],['8',"38"],['9',"39"],[':',"3A"],[';',"3B"],['<',"3C"],['=',"3D"]
             ,['>',"3E"],['?',"3F"],['@',"40"],['A',"41"],['B',"42"],['C',"43"],['D',"44"],['E',"45"],['F',"46"],['G',"47"],['H',"48"],['I',"49"],['J',"4A"],['K',"4B"],['L',"4C"]
             ,['M',"4D"],['N',"4E"],['O',"4F"],['P',"50"],['Q',"51"],['R',"52"],['S',"53"],['T',"54"],['U',"55"],['V',"56"],['W',"57"],['X',"58"],['Y',"59"],['s',"5A"],['[',"5B"]
             ,['￥',"5C"],[']',"5D"],['^',"5E"],['_',"5F"],['`',"60"],['a',"61"],['b',"62"],['c',"63"],['d',"64"],['e',"65"],['f',"66"],['g',"67"],['h',"68"],['i',"69"],['j',"6A"]
             ,['k',"6B"],['l',"6C"],['m',"6D"],['n',"6E"],['o',"6F"],['p',"70"],['q',"71"],['r',"72"],['s',"73"],['t',"74"],['u',"75"],['v',"76"],['w',"77"],['x',"78"],['y',"79"]
             ,['s',"7A"],['{',"7B"],['|',"7C"],['}',"7D"],['→',"7E"],['←',"7F"],['┌',"A2"],['┘',"A3"],['°',"A5"]]
    mncos=[["ADCA","89","99","A9","18A9","B9",0,0],["ADCB","C9","D9","E9","18E9","F9",0,0],["ADDA","8B","9B","AB","18AB","BB",0,0],["ADDB","CB","DB","EB","18EB","FB",0,0]
            ,["ADDD","C3","D3","E3","18E3","F3",0,0],["ANDA","84","94","A4","18A4","B4",0,0],["ANDB","C4","D4","E4","18E4","F4",0,0],["ASL",0,0,"68","1868","78",0,0]
            ,["ASR",0,0,"67","1867","77",0,0],["BCLR",0,"15","1D","181D",0,0,0],["BITA","85","95","A5","18A5","B5",0,0],["BITB","C5","D5","E5","18E5","F5",0,0]
            ,["BRCLR",0,"13","IF","181F",0,0,0],["BRSET",0,"12","1E","181E",0,0,0],["BSET",0,"14","1C","181C",0,0,0],["CLR",0,0,"6F","186F","7F",0,0]
            ,["CMPA","81","91","A1","18A1","B1",0,0],["CMPB","C1","D1","E1","18E1","F1",0,0],["COM",0,0,"63","1863","73",0,0],["CPD","1A83","1A93","1AA3","CDA3","1AB3",0,0]
            ,["CPX","8C","9C","AC","CDAC","BC",0,0],["CPY","188C","189C","1AAC","18AC","18BC",0,0],["DEC",0,0,"6A","186A","7A",0,0],["EORA","88","98","A8","18A8","B8",0,0]
            ,["EORB","C8","D8","E8","18E8","F8",0,0],["INC",0,0,"6C","186C","7C",0,0],["LDAA","86","96","A6","18A6","B6",0,0],["LDAB","C6","D6","E6","18E6","F6",0,0]
            ,["LDD","CC","DC","EC","18EC","FC",0,0],["LDS","8E","9E","AE","18AE","BE",0,0],["LDX","CE","DE","EE","CDEE","FE",0,0],["LDY","18CE","18DE","1AEE","18EE","18FE",0,0]
            ,["LSL",0,0,"68","1868","78",0,0],["LSR",0,0,"64","1864","74",0,0],["NEG",0,0,"60","1860","70",0,0],["ORAA","8A","9A","AA","18AA","BA",0,0]
            ,["ORAB","CA","DA","EA","18EA","FA",0,0],["ROL",0,0,"69","1869","79",0,0],["ROR",0,0,"66","1866","76",0,0],["SBCA","82","92","A2","18A2","B2",0,0]
            ,["SBCB","C2","D2","E2","18E2","F2",0,0],["STAA",0,"97","A7","18A7","B7",0,0],["STAB",0,"D7","E7","18E7","F7",0,0],["STD",0,"DD","ED","18ED","FD",0,0]
            ,["STS",0,"9F","AF","18AF","BF",0,0],["STX",0,"D","EF","CDEF","FF",0,0],["STY",0,"18DF","1AEF","18EF","FF",0,0],["SUBA","80","90","A0","18A0","B0",0,0]
            ,["SUBB","C0","D0","E0","18E0","F0",0,0],["SUBD","83","93","A3","18A3","B3",0,0],["TST",0,0,"6D","186D","7D",0,0]]

    inh=[["ABA",0,0,0,0,0,"1B",0],["ABX",0,0,0,0,0,"3A",0],["ABY",0,0,0,0,0,"183A",0],["ASLA",0,0,0,0,0,"48",0],["ASLB",0,0,0,0,0,"58",0],["ASLD",0,0,0,0,0,"5",0]
                ,["ASRA",0,0,0,0,0,"47",0],["ASRB",0,0,0,0,0,"57",0],["CBA",0,0,0,0,0,"11",0],["CLC",0,0,0,0,0,"0C",0],["CLI",0,0,0,0,0,"0E",0],["CLRA",0,0,0,0,0,"4F",0]
                ,["CLRB",0,0,0,0,0,"5F",0],["CLV",0,0,0,0,0,"0A",0],["COMA",0,0,0,0,0,"43",0],["COMB",0,0,0,0,0,"53",0],["DAA",0,0,0,0,0,"19",0],["DECA",0,0,0,0,0,"4A",0]
                ,["DECB",0,0,0,0,0,"5A",0],["DES",0,0,0,0,0,"34",0],["DEX",0,0,0,0,0,"09",0],["DEY",0,0,0,0,0,"1809",0],["FDIV",0,0,0,0,0,"03",0],["IDIV",0,0,0,0,0,"02",0]
                ,["INCA",0,0,0,0,0,"4C",0],["INCB",0,0,0,0,0,"5C",0],["INS",0,0,0,0,0,"31",0],["INX",0,0,0,0,0,"08",0],["INY",0,0,0,0,0,"1808",0],["LSLA",0,0,0,0,0,"48",0]
                ,["LSLB",0,0,0,0,0,"58",0],["LSLD",0,0,0,0,0,"05",0],["LSRA",0,0,0,0,0,"44",0],["LSRB",0,0,0,0,0,"54",0],["LSRD",0,0,0,0,0,"04",0],["MUL",0,0,0,0,0,"3D",0]
                ,["NEGA",0,0,0,0,0,"40",0],["NEGB",0,0,0,0,0,"50",0],["NOP",0,0,0,0,0,"01",0],["PSHA",0,0,0,0,0,"36",0],["PSHB",0,0,0,0,0,"37",0],["PSHX",0,0,0,0,0,"3C",0]
                ,["PSHY",0,0,0,0,0,"183C",0],["PULA",0,0,0,0,0,"32",0],["PULB",0,0,0,0,0,"33",0],["PULX",0,0,0,0,0,"38",0],["PULY",0,0,0,0,0,"1838",0],["ROLA",0,0,0,0,0,"49",0]
                ,["ROLB",0,0,0,0,0,"59",0],["RORA",0,0,0,0,0,"46",0],["RORB",0,0,0,0,0,"56",0],["RTI",0,0,0,0,0,"3B",0],["RTS",0,0,0,0,0,"39",0],["SBA",0,0,0,0,0,"10",0]
                ,["SEC",0,0,0,0,0,"OD",0],["SEI",0,0,0,0,0,"OF",0],["SEV",0,0,0,0,0,"OB",0],["STOP",0,0,0,0,0,"CF",0],["SWI",0,0,0,0,0,"3F",0],["TAB",0,0,0,0,0,"16",0]
                ,["TAP",0,0,0,0,0,"06",0],["TBA",0,0,0,0,0,"17",0],["TEST",0,0,0,0,0,"00",0],["TPA",0,0,0,0,0,"07",0],["TSTA",0,0,0,0,0,"4D",0],["TSTB",0,0,0,0,0,"5D",0]
                ,["TSX",0,0,0,0,0,"30",0],["TSY",0,0,0,0,0,"1830",0],["TXS",0,0,0,0,0,"35",0],["TYS",0,0,0,0,0,"1835",0],["WAI",0,0,0,0,0,"3E",0],["XGDX",0,0,0,0,0,"8F",0]
                ,["XGDY",0,0,0,0,0,"188F",0]]
    reTv=[["BCC",0,0,0,0,0,0,"24"],["BCS",0,0,0,0,0,0,"25"],["BEQ",0,0,0,0,0,0,"27"],["BGE",0,0,0,0,0,0,"2C"],["BGT",0,0,0,0,0,0,"2E"],["BHI",0,0,0,0,0,0,"22"]
               ,["BHS",0,0,0,0,0,0,"24"],["BLE",0,0,0,0,0,0,"2F"],["BLO",0,0,0,0,0,0,"25"],["BLS",0,0,0,0,0,0,"23"],["BLT",0,0,0,0,0,0,"2D"],["BMI",0,0,0,0,0,0,"2B"]
               ,["BNE",0,0,0,0,0,0,"26"],["BPL",0,0,0,0,0,0,"2A"],["BRA",0,0,0,0,0,0,"20"],["BRN",0,0,0,0,0,0,"21"],["BSR",0,0,0,0,0,0,"8D"],["BVC",0,0,0,0,0,0,"28"]
               ,["BVS",0,0,0,0,0,0,"29"]]
    a1=0
    s=0
    if dir != None:
        dir,tres=idenHasht(dir)
        for conteo in list(range(len(varB))):
            if eTq==varB[conteo][0] or dir==varB[conteo][0]:
                dir=varB[conteo][1]
            if dir.count("'")>=1:
                for conteo in list(range(len(simb))):
                    if simb[conteo][0]==dir[1:]:
                        dir="$"+simb[conteo][1]
                        break
        if len(dir)>5:
                if dir.count(",")==0:
                    s=1
        if tres==3:
            dir='#'+dir
        if array=="BSET":
            if dir.count("X")==1 or dir.count("x")==1:
                if len(dir)>10:
                    return "1C","Magnitud de operando erronea"
                else:
                    return "1C"+dir[1]+dir[2]+dir[8]+dir[9],a1
            elif dir.count("Y")==1 or dir.count("y")==1:
                if len(dir)>10:
                    return "181C","Magnitud de operando erronea"
                else:
                    return "181C"+dir[1]+dir[2]+dir[8]+dir[9],a1                                                          
            else:
                if len(dir)>8:
                    return "14","Magnitud de operando erronea"
                else:
                    return "14"+dir[1]+dir[2]+dir[6]+dir[7],a1
        if array=="BCLR":
            if dir.count("X")==1 or dir.count("x")==1:
                if len(dir)>10:
                    return "1D","Magnitud de operando erronea"
                else:
                    return "1D"+dir[1]+dir[2]+dir[8]+dir[9],a1                                                            
            elif dir.count("Y")==1 or dir.count("y")==1:
                if len(dir)>10:
                    return "181D","Magnitud de operando erronea"
                else:
                    return "181D"+dir[1]+dir[2]+dir[8]+dir[9],a1
            else:
                if len(dir)>8:
                    return "15","Magnitud de operando erronea"
                else:
                    return "15"+dir[1]+dir[2]+dir[6]+dir[7],a1
        if array=="BRCLR":
            if dir.count("X")==1 or dir.count("x")==1:
                if len(dir)>10:
                    return "1F","Magnitud de operando erronea"
                else:
                    return "1F"+dir[1]+dir[2]+dir[8]+dir[9]+"XX",a1
            elif dir.count("Y")==1 or dir.count("y")==1:
                if len(dir)>10:
                    return "181F","Magnitud de operando erronea"
                else:
                    return "181F"+dir [1]+dir[2]+dir[8]+dir[9]+"XX",a1                                                   
            else:
                if len(dir)>8:
                    return "13","Magnitud de operando erronea"
                else:
                    return "13"+dir[1]+dir[2]+dir[6]+dir[7]+"XX",a1
        if array=="BRSET":
            if dir.count("X")==1 or dir.count("x")==1:
                if len(dir)>10:
                    return "1E","Magnitud de operando erronea"
                else:
                    return "1E"+dir[1]+dir[2]+dir[8]+dir[9]+"XX",a1                                                       
            elif dir.count("Y")==1 or dir.count("y")==1:
                if len(dir)>10:
                    return "181E","Magnitud de operando erronea"
                else:
                    return "181E"+dir[1]+dir[2]+dir[8]+dir[9]+"XX",a1
            else:
                if len(dir)>8:
                    return "12","Magnitud de operando erronea"
                else:
                    return "12"+dir[1]+dir[2]+dir[6]+dir[7]+"XX",a1
        if array=="FCB":
            if s==1:
                return dir[1]+dir[2]+dir[5]+dir[6],"Magnitud de operando erronea" 
            else:
                return dir[1]+dir[2]+dir[5]+dir[6],a1
        if array=="JSR" or array=="JMP":
            if array=="JSR":
                return "BDXXXX",1
            if array=="JMP":
                return "7EXXXX",1
        for conteo in list(range (len(reTv))):
            if array==reTv[conteo][0]:
                return reTv[conteo][7]+"XX",1
    for conteo in list(range (len(inh))):
            if array==inh[conteo][0]:
                if dir!=None:
                    return inh[conteo][6],"Operando inexistente"
                else:
                    return inh[conteo][6],a1
    for conteo in list(range (len(mncos))):
        if array==mncos[conteo][0]:
            if dir==None:
                return mncos[conteo][6],"Instruccion sin operandos"
            if dir.count("$")==0 and dir[0]=='#':
                return "XX","No existe la constante"
            if dir.count("$")==0 and dir[0]!='#':
                return mncos[conteo][1],"Variable inexistente"
            if dir.count("$")>=1:
                if dir[0]=='#':
                    if s==1:
                        return mncos[conteo][1],"Magnitud de operando erronea"
                    else:
                        if array=="ADDD" or array=="CPD" or array=="CPX" or array=="CPY" or array=="LDD" or array=="LDS" or array=="LDX" or array=="LDY" or array=="SUBD":
                            if len(dir[2:])==1:
                                return mncos[conteo][1]+'000'+dir[2:],0
                            if len(dir[2:])==2:
                                return mncos[conteo][1]+'00'+dir[2:],0
                            if len(dir[2:])==3:
                                return mncos[conteo][1]+'0'+dir[2:],0
                    return mncos[conteo][1]+dir[2:],0
                if dir.count("#")==0:
                    if len(dir)<=3:
                        return mncos[conteo][2]+dir[1:],a1
                    if len(dir)>=4 and dir.count(",")==0:                                                                           
                        if dir[1]=='0' and dir[2]=='0':
                            if mncos[conteo][2]==0:
                                if s==1:
                                    return mncos[conteo][5],"Magnitud de operando erronea"
                                else:

                                    return mncos[conteo][5]+dir[1:],a1
                            else:
                                if s==1:
                                    return mncos[conteo][2],"Magnitud de operando erronea"
                                else:

                                    return mncos[conteo][2]+dir[3:],a1
                        else:
                            if s==1:
                                return mncos[conteo][5],"Magnitud de operando erronea"
                            else:
                                return mncos[conteo][5]+dir[1:],a1
                    if dir.count(",")==1:
                        if dir.count("X")==1 or dir.count("x")==1:
                            if s==1:
                                
                                return mncos[conteo][3],"Magnitud de operando erronea"
                            else:
                                if dir[1]=='0' and dir[2]=='0' and len(dir)<=5:
                                    
                                    return mncos[conteo][3]+dir[1]+dir[2],a1
                                else:
                                    if dir[1]=='0' and dir[2]=='0':
                                        
                                        return mncos[conteo][3]+dir[3]+dir[4],a1
                                    else:
                                        
                                        return mncos[conteo][3]+dir[1:5],a1
                        if dir.count("Y")==1 or dir.count("y")==1:
                            if s==1:
                                return mncos[conteo][3],"Magnitud de operando erronea"
                            else:
                                if dir[1]=='0' and dir[2]=='0' and len(dir)<=5:
                                    
                                    return mncos[conteo][4]+dir[1]+dir[2],a1
                                else:
                                    if dir[1]=='0' and dir[2]=='0':
                                        
                                        return mncos[conteo][4]+dir[3]+dir[4],a1
                                    else:
                                        
                                        return mncos[conteo][4]+dir[1:5],a1
    return 'Mnemonico inexistente',0

def numErrores(opCode):
    cuenta = sum(1 for caracter in opCode if caracter != ' ')
    return int(cuenta * 0.5)

def errUnion(e1, error):
    for aux in range(e1):
        for au2 in range(e1 - 1):
            if error[au2][1] > error[au2 + 1][1]:
                error[au2], error[au2 + 1] = error[au2 + 1], error[au2]

    au2 = 0
    while au2 < e1 - 1:
        if error[au2][1] == error[au2 + 1][1]:
            a1 = [[error[au2][0] + " " + error[au2 + 1][0], error[au2][1]]]
            error[au2:au2 + 2] = a1
            e1 = len(error)
        au2 += 1

    return error

def errores(a1, error, e1, opCode):
    error_codes = {
        "Constante inexistente": "TIPO DE ERROR 1",
        "Variable inexistente": "TIPO DE ERROR 2",
        "Etiqueta inexistente": "TIPO DE ERROR 3",
        "Mnemonico inexistente": "TIPO DE ERROR4",
        "Instruccion sin operandos": "TIPO DE ERROR 5",
        "Operando inexistente": "TIPO DE ERROR6",
        "Magnitud de operando erronea": "TIPO DE ERROR 7",
        "Salto relativo muy lejano": "TIPO DE ERROR 8",
        "Mnemonico inexistente": "TIPO DE ERROR 9"
    }
    
    if a1 in error_codes:
        error[e1][0] = error_codes[a1]
        error[e1][1] = lin_Cont
        e1 += 1

    if opCode[op][0] == 'Mnemonico inexistente':
        opCode[op][0] = 'XX'
        error[e1][0] = "TIPO DE ERROR 04"
        error[e1][1] = lin_Cont
        e1 += 1

    return error, e1, opCode


contp=0



nomArchivo="START" + ".ASC"
print("--------------------------- Compilador del MC68HC11 --------------------------- ")
print("Nombre del archivo a compilar: " + nomArchivo)

while True:
    try:
        Achivo_LST=nomArchivo
        codigo=open(Achivo_LST,"r")                                                                                                    
        break
    except FileNotFoundError as error:
        print("\nEl rchivo:"+"nomArchivo"+"no exixste o es incorrecto\n",error)

numLineas=contLineas(codigo)                                                                                                               #Contador de lineas en el arch_1 .asc
codigo.seek(0)                                                                                                                                #Regresa al inicio del arch_1
eTqi=varC=op=actual_dir=lin_Cont=dirC=direc_A=eTqi_2=arch_12=R1=e1=0
eTq,varB,programaLin,opCode,momento_dirCcion,dirMom_op,dir1,eTq2,Ar_2,error = apartarMem(numLineas)
HAY_END=1

for lin in codigo.readlines():                                                                                                              #Se recorre el arch_1 linea por linea
        guarda_direccion=0
        programaLin[lin_Cont]=lin
        lin=numAsteri(lin)
        array=lin.split()
        dirT=lin.upper().split()
        if dirT.count("EQU")>=1:
            if len(dirT)<3:                                                                                                               #Identifica las variables del programa
                error,e1,h_o=errores("Instruccion sin operandos",error,e1,opCode)
                dir1[dirC][0]='XXXX'
                dir1[dirC][1]=lin_Cont
                dirC+=1
            if len(dirT)==3:
                varB[varC][0]=array[0]
                varB[varC][1]=array[2]
                varC+=1
                dir1[dirC][0]=array[2][1:]
                dir1[dirC][1]=lin_Cont
                dirC+=1
        elif dirT.count("ORG") >= 1:
            if len(dirT)==1:
                momento_dirCcion[actual_dir][0]=int('1000',16)
                momento_dirCcion[actual_dir][1]=lin_Cont+1
                dir1[dirC][0]="1000"
                error,e1,h_o=errores("Magnitud de operando erronea",error,e1,opCode)
            elif len(dirT)==2:
                momento_dirCcion[actual_dir][0]=int(array[1][1:],16)
                momento_dirCcion[actual_dir][1]=lin_Cont+1
                dir1[dirC][0]=array[1][1:]
            elif len(dirT)==3:
                momento_dirCcion[actual_dir][1]=int(array[1][1:],16)
                momento_dirCcion[actual_dir][2]=lin_Cont+1
                dir1[dirC][0]=array[2][1:]
            if arch_12!=0:
                opCode[op-1][2]='Gato'
            Ar_2[arch_12][0]=momento_dirCcion[actual_dir][0]
            arch_12+=1
            dir1[dirC][1]=lin_Cont
            actual_dir+=1
            dirC+=1
        elif dirT.count("END") >=1:
            HAY_END=0
            break
        else:
            if elemxLinea(lin)==1:
                if lin[0]==" " or lin[0]=="\t" :
                    m_nE,opCode[op][0],a1=Elemento1(array,varB,1)                                                                      #El elemento 1 se guarda en el mnemonico
                    opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                    error,e1,opCode=errores(a1,error,e1,opCode)
                    momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                    momento_dirCcion[actual_dir][1]=lin_Cont+1
                    opCode[op][1]=lin_Cont
                    op+=1
                    actual_dir+=1
                else:
                    eTq[eTqi][0]=Elemento1(array,varB)                                                                             #El elemento 1 se guarda en etiqueta
                    eTq[eTqi][1]=momento_dirCcion[actual_dir-1][0]
                    eTqi+=1
            elif elemxLinea(lin)==2:
                if lin[0]==" " or lin[0]=="\t" :                                                         #regla por si el primer elemento de la linea es espacio o tabulacion
                    if array[1].count("#")>=1 or array[1].count("$")>=1:
                        m_nE,direC,opCode[op][0],a1=Elemento2(array,varB,1)                        #El elemento 1 se guarda como mnemonico, elemento 2 se guarda como direccion
                        opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                        error,e1,opCode=errores(a1,error,e1,opCode)
                        momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                        momento_dirCcion[actual_dir][1]=lin_Cont+1
                        opCode[op][1]=lin_Cont
                        op+=1
                        actual_dir+=1
                    else:
                        m_nE,eT,opCode[op][0],a1=Elemento2(array,varB,2)                          #El elemento 1 se guarda como mnemonico, elemento 2 se guarda como etiqueta
                        opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                        error,e1,opCode=errores(a1,error,e1,opCode)
                        if a1==1:
                            eTq2[eTqi_2][0]=eT
                            eTq2[eTqi_2][2]=opCode[op][0]
                            eTq2[eTqi_2][3]=op
                            eTq2[eTqi_2][4]=lin_Cont
                            guarda_direccion=1
                        momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                        momento_dirCcion[actual_dir][1]=lin_Cont+1
                        if guarda_direccion==1:
                            eTq2[eTqi_2][1]=momento_dirCcion[actual_dir][0]
                            eTqi_2+=1
                        opCode[op][1]=lin_Cont
                        op+=1
                        actual_dir+=1
                else:
                    eTq[eTqi][0],m_nE,opCode[op][0],a1=Elemento2(array,varB,3)                #El elemento 1 se guarda como etiqueta, elemento 2 se guarda como mnemonico
                    eTq[eTqi][1]=momento_dirCcion[actual_dir-1][0]
                    opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                    error,e1,opCode=errores(a1,error,e1,opCode)
                    momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                    momento_dirCcion[actual_dir][1]=lin_Cont+1
                    opCode[op][1]=lin_Cont
                    op+=1
                    actual_dir+=1
                    eTqi+=1
            elif elemxLinea(lin)==3:
                if lin[0]==" " or lin[0]=="\t" :                                                        #reglan por si el elemento primero de la linea es espacio o tabulacion
                    m_nE,direC,eT,opCode[op][0],a1=Elemento3(array,varB,1)                     #El elemento 1 se guarda en etiqueta, el 2 como mnemonico y el 3 como direccion
                    opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                    error,e1,opCode=errores(a1,error,e1,opCode)
                    eTq2[eTqi_2][0]=eT
                    eTq2[eTqi_2][2]=opCode[op][0]
                    eTq2[eTqi_2][3]=op
                    eTq2[eTqi_2][4]=lin_Cont
                    momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                    momento_dirCcion[actual_dir][1]=lin_Cont+1
                    eTq2[eTqi_2][1]=momento_dirCcion[actual_dir][0]
                    opCode[op][1]=lin_Cont
                    op+=1
                    actual_dir+=1
                    eTqi_2+=1
                else:
                    eTq[eTqi][0],m_nE,direC,opCode[op][0],a1=Elemento3(array,varB,2)       #El elemento 1 se guarda en etiqueta, el 2 como mnemonico y el 3 como direccion
                    eTq[eTqi][1]=momento_dirCcion[actual_dir-1][0]
                    opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                    error,e1,opCode=errores(a1,error,e1,opCode)
                    if a1==1 and m_nE!="FCB":
                        eTq2[eTqi_2][0]=direC
                        eTq2[eTqi_2][2]=opCode[op][0]
                        eTq2[eTqi_2][3]=op
                        eTq2[eTqi_2][4]=lin_Cont
                        guarda_direccion=1
                    momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                    momento_dirCcion[actual_dir][1]=lin_Cont+1
                    if guarda_direccion==1:
                            eTq2[eTqi_2][1]=momento_dirCcion[actual_dir][0]
                            eTqi_2+=1
                    opCode[op][1]=lin_Cont
                    op+=1
                    actual_dir+=1
                    eTqi+=1
            elif elemxLinea(lin)==4:
                if lin[0]==" " or lin[0]=="\t" :
                    pass
                else:
                    eTq[eTqi][0],m_nE,dir,eTqi_1,opCode[op][0],a1=Elemento4(array,varB)#El elemento 1 se guarda en etiqueta, el 2 como mnemonico y el 3 como direccion
                    eTq[eTqi][1]=momento_dirCcion[actual_dir-1][0]
                    opCode[op][2]=momento_dirCcion[actual_dir-1][0]
                error,e1,opCode=errores(a1,error,e1,opCode)
                eTq2[eTqi_2][0]=eTqi_1
                eTq2[eTqi_2][2]=opCode[op][0]
                eTq2[eTqi_2][3]=op
                eTq2[eTqi_2][4]=lin_Cont
                momento_dirCcion[actual_dir][0]=momento_dirCcion[actual_dir-1][0]+numErrores(opCode[op][0])
                momento_dirCcion[actual_dir][1]=lin_Cont+1
                eTq2[eTqi_2][1]=momento_dirCcion[actual_dir][0]
                opCode[op][1]=lin_Cont
                eTqi_2+=1
                op+=1
                actual_dir+=1
                eTqi+=1
        lin_Cont+=1

if HAY_END==1:
        sin_end="ERROR 010"

eTq=eTq[:eTqi]
dir1=dir1[:dirC]
momento_dirCcion=momento_dirCcion[:actual_dir]
opCode=opCode[:op]
eTq2=eTq2[:eTqi_2]
Ar_2=Ar_2[:arch_12]
dir_y_op=0

#Sustituir X por números en Hexadecimal

for eti2 in range(len(eTq2)):
    for prim_eti in range(len(eTq)):
        if eTq2[eti2][0]==eTq[prim_eti][0]:
            if eTq2[eti2][2].count("X")>2:
                eTq2[eti2][2]=numdX(eTq2[eti2][2])+str(format(eTq[prim_eti][1],'X'))
                opCode[eTq2[eti2][3]][0]=eTq2[eti2][2]
                eTq2[eti2][5]="Check"
                continue
            if eTq[prim_eti][1]<eTq2[eti2][1]:
                if eTq2[eti2][1]-eTq[prim_eti][1]>=128:
                    error[e1][0]="ERROR 002"
                    error[e1][1]=eTq2[eti2][4]
                    e1+=18
                else:
                    eTq2[eti2][2]=numdX(eTq2[eti2][2])+complementos(eTq2[eti2][1]-eTq[prim_eti][1])
                opCode[eTq2[eti2][3]][0]=eTq2[eti2][2]
                eTq2[eti2][5]="Check"
                continue
            if eTq[prim_eti][1]>eTq2[eti2][1]:
                if eTq[prim_eti][1]-eTq2[eti2][1]>=127:
                    error[e1][0]="ERROR 008"
                    error[e1][1]=eTq2[eti2][4]
                    e1+=1
                else:
                    hexDir=str(eTq[prim_eti][1]-eTq2[eti2][1])
                    if len(hexDir)==1:
                        hexDir="0"+hexDir
                    eTq2[eti2][2]=numdX(eTq2[eti2][2])+hexDir
                    opCode[eTq2[eti2][3]][0]=eTq2[eti2][2]
                eTq2[eti2][5]="Check"
                continue

for eti2 in range(len(eTq2)):
    if eTq2[eti2][5]!="Check":
        error[e1][0]="ERROR 003"
        error[e1][1]=eTq2[eti2][4]
        e1+=1

error=error[:e1]
error=errUnion(e1,error)
a1=0

for segunda_impresion in range(arch_12):
    while opCode[a1][2]!='Gato':
        Ar_2[segunda_impresion][1]=str(Ar_2[segunda_impresion][1])+str(opCode[a1][0])
        if a1<op-1:
            a1+=1
        else:
            break
    if a1<op-1:
        Ar_2[segunda_impresion][1]=str(Ar_2[segunda_impresion][1])+str(opCode[a1][0])
        a1+=1

for segunda_impresion2 in range(arch_12):
    Ar_2[segunda_impresion2][1]=Ar_2[segunda_impresion2][1][2:]

for lineaop in range(op):
    for lineadir in range(actual_dir):
        if opCode[lineaop][1]+1==momento_dirCcion[lineadir][1]:
            dirMom_op[dir_y_op][0]=str(format(momento_dirCcion[lineadir-1][0],'X'))+" ("+str(opCode[lineaop][0])
            dirMom_op[dir_y_op][1]=opCode[lineaop][1]
            dir_y_op+=1

Achivo_LST=numPuntos(Achivo_LST)+".LST"                                                                                           #Abrir los arch_1s .lst y .s19
direccion_arch_s19=numPuntos(Achivo_LST)+".S19"

arch_1=open(Achivo_LST,"w")
arch_2=open(direccion_arch_s19,"w")

dirC=0
dir_y_op=0
w=e1
e1=0

for linea in range(numLineas):                                                                                                                                #Escribir en los arch_1s
    x=0
    s=0
    if programaLin[linea].count("END") >=1:
        arch_1.write(str(linea+1)+" :\t\t\t\t"+programaLin[linea])
        break
    if len(dir1)>0:
        if dir1[dirC][1]==linea:
            arch_1.write(str(linea+1)+" :\t\t"+str(dir1[dirC][0])+"\t\t"+programaLin[linea])
            dire=" "
            x=1
            s=1
            if dirC<len(dir1)-1:
                dirC+=1
    if dirMom_op[dir_y_op][1]==linea:
        if len(dirMom_op[dir_y_op][0].split()[1])>=8:
            arch_1.write(str(linea+1)+" :\t"+dirMom_op[dir_y_op][0]+")    :\t\t"+programaLin[linea])
        else:
            arch_1.write(str(linea+1)+" :\t"+dirMom_op[dir_y_op][0]+")    :\t\t"+programaLin[linea])                                  #lineas para escribir datos en los arch_1s
            x=1
            dire=dirMom_op[dir_y_op][0][:4]
        if dir_y_op<len(dirMom_op)-1:
            dir_y_op+=1
            s=1
    if w>=1 and s==1:
        if error[e1][1]==linea:
            arch_1.write(error[e1][0]+"\n")                                                                                           #Escribe el Error en la linea que se encontro
            if e1<len(error)-1:                                                                                                        #el numero de Error
                e1+=1
    if x==0 and s==0:
        if len(programaLin[linea])<=1:
            arch_1.write(str(linea+1)+" :\t\t\t\t"+programaLin[linea])
        else:
            arch_1.write(str(linea+1)+" :\t\t\t\t"+programaLin[linea])

if HAY_END==1:                                                                                                                           #Pregunta si hay final en el programa
    w+=1
    arch_1.write("\n"+sin_end+"\n")

for segunda_impresion2 in range(arch_12):                                                                                               #Escritura del arch_1 .s19
    a1=ceil(len(Ar_2[segunda_impresion2][1])/32)
    x=0
    for impresion_arch_1 in range(a1):
        arch_2.write("<"+format(int(Ar_2[segunda_impresion2][0])+int(impresion_arch_1*16),'X')+">  ")
        if x<a1-1:
            s=0
            while s<=15:
                y=Ar_2[segunda_impresion2][1][:2]
                Ar_2[segunda_impresion2][1]=Ar_2[segunda_impresion2][1][2:]
                arch_2.write(y+"  ")
                s+=1
            arch_2.write("\n")
            x+=1
            continue
        if x==a1-1:
            s=0
            wile=len(Ar_2[segunda_impresion2][1])/2
            while s<wile:
                y=Ar_2[segunda_impresion2][1][:2]
                Ar_2[segunda_impresion2][1]=Ar_2[segunda_impresion2][1][2:]
                arch_2.write(y+"  ")
                s+=1
            arch_2.write("\n")
            break

print("\nLa compilacion se  relizó correctamente.Se encontraron",w,"errores en el codigo")
print("LOS ARCHIVOS .LST y .S19 SE CREARON CORRECTAMENTE")
print("SI EL ARCHIVO CONIENE ERORRES SE PUEDEN VISUALIZAR EN EL ARCHIVO: "+ Achivo_LST)
arch_2.close()
arch_1.close()
codigo.close()                                                                                                                            #Cerrar los arch_1s
