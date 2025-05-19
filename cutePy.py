import sys

#TO ARXEIO EISODOY TO PAIRNEI WS ORISMA OTAN TO TREXOYME
filename = sys.argv[1]

file = open(filename, 'r')

###KATASTASEIS TOY AYTOMATOY     ###GRAMMES TOY PINAKA METAVASEWN
startSTATE = 0
lordSTATE = 1
digitSTATE = 2
divisionSTATE = 3
smaller_thanSTATE = 4
larger_thanSTATE = 5
exclamatiom_markSTATE = 6
equalSTATE = 7
hash_markSTATE = 8
commentsSTATE = 9
maybe_closing_commentsSTATE = 10
quotation_markSTATE = 11


###OLOI OI XARAKTHRES THS CUTEPY    ###STHLES TOY PINAKA METAVASEWN
chars = ['blank', 'letters', 'digits', 'underscore', 'add', 'sub', 'mul', 'div', 'smaller_than', 'larger_than', 'exclamatiom_mark',
         'equal', 'question_mark', 'comma', 'colon', 'left_bracket', 'right_bracket', 'left_parenthesis', 'right_parenthesis',
         'hash_mark', 'start_of_block', 'end_of_block', 'dollar_sign', 'quotation_mark', 'next_line', 'not_accepted_symbol',
         'EOF']



###OLA TA TOKENS ME MONADIKO ARITHMO-KWDIKO TO KATHENA KSEKINONTAS APO 100
id_kwrdTOKEN = 100
digitTOKEN = 101
addTOKEN = 102
subTOKEN = 103
mulTOKEN = 104
divTOKEN = 105
smaller_equalTOKEN = 106
smallerTOKEN = 107
larger_equalTOKEN = 108
largerTOKEN = 109
differentTOKEN = 110
equalTOKEN = 111
assignmentTOKEN = 112
question_markTOKEN = 113
commaTOKEN = 114
colonTOKEN = 115
left_bracketTOKEN = 116
right_bracketTOKEN = 117
left_parenthesisTOKEN = 118
right_parenthesisTOKEN = 119
start_of_blockTOKEN = 120
end_of_blockTOKEN = 121
EOFTOKEN = 122


#DESMEUMENES LEKSEIS PROGRAMMATOS
desmeumenes_lexeis = ['#declare','if','else','while','return','print',
                      'int','input','def','or','and','not','__name__','"__main__"']

#DESMEUMENA TOKEN (telikh katastash) PROGRAMMATOS
desmeumenes_lexeisTOKEN = ['declareTOKEN', 'ifTOKEN', 'elseTOKEN', 'whileTOKEN', 'returnTOKEN', 'printTOKEN', 'intTOKEN',
                            'inputTOKEN', 'defTOKEN', 'orTOKEN', 'andTOKEN', 'notTOKEN', 'nameTOKEN', 'mainTOKEN'  ]




###OLA TA ERRORS ME MONADIKO ARITHMO-KWDIKO TO KATHENA
ERROR_notAcceptedSymbol = -1
ERROR_singleSlash = -2   
ERROR_letterAfterDigit = -3
ERROR_numberOutOfRange = -4
ERROR_identifierOver30Characters = -5
ERROR_EOFBeforeClosingComments = -6
ERROR_singleDollarSign = -7   
ERROR_singleLeftCurlyBrackets = -8    
ERROR_singleRightCurlyBrackets = -9    
ERROR_identifierStartsWithUnderscore = -10
ERROR_singleExclamationMark = -11    
ERROR_singleHashMark = -12    
ERROR_identifierStartsWithHashMarkWithoutBeingTheKeywordDeclare = -13
ERROR_singleQuotationMark = -14     
ERROR_identifierContainsQuoteMarkWithoutBeingTheKeywordMain = -15



### PINAKAS METAVASEWN APO KATHE KATASTASH SE POIA ALLH KATASTASH ME TON ERXOMO TOY ANTISTOIXOY XARAKTHRA KATHE FORA ###

transition_matrix=[
    #gia thn katastash startSTATE     
    [startSTATE, lordSTATE, digitSTATE, lordSTATE, addTOKEN, subTOKEN, mulTOKEN,
     divisionSTATE, smaller_thanSTATE, larger_thanSTATE, exclamatiom_markSTATE, equalSTATE, question_markTOKEN, commaTOKEN, colonTOKEN,
     left_bracketTOKEN, right_bracketTOKEN, left_parenthesisTOKEN, right_parenthesisTOKEN, hash_markSTATE,
     ERROR_singleLeftCurlyBrackets, ERROR_singleRightCurlyBrackets, ERROR_singleDollarSign, quotation_markSTATE,
     startSTATE, ERROR_notAcceptedSymbol, EOFTOKEN
    ],

    #gia thn katastash lordSTATE
    [id_kwrdTOKEN, lordSTATE, lordSTATE, lordSTATE, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN,
     id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN,
     id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, id_kwrdTOKEN, lordSTATE, id_kwrdTOKEN,
     ERROR_notAcceptedSymbol, id_kwrdTOKEN
    ],

    #gia thn katastash digitSTATE
    [digitTOKEN, ERROR_letterAfterDigit, digitSTATE, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN,
     digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN,
     digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, digitTOKEN, ERROR_notAcceptedSymbol, digitTOKEN
    ],

    #gia thn katastash divisionSTATE
    [ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash,
     ERROR_singleSlash, divTOKEN, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash,
     ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash,
     ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_singleSlash, ERROR_notAcceptedSymbol,
     ERROR_singleSlash
    ],


    #gia thn katastash smaller_thanSTATE
    [smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN,
     smallerTOKEN, smallerTOKEN, smallerTOKEN, smaller_equalTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN,
     smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN, smallerTOKEN,
     ERROR_notAcceptedSymbol, smallerTOKEN
    ],

    #gia thn katastash larger_thanSTATE
    [largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN,
     largerTOKEN, largerTOKEN, larger_equalTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN,
     largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, largerTOKEN, ERROR_notAcceptedSymbol,
     largerTOKEN
    ],

    #gia thn katastash exclamatiom_markSTATE
    [ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark,
     ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark,
     ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark, differentTOKEN,
     ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark,
     ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark,
     ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark, ERROR_singleExclamationMark,
     ERROR_singleExclamationMark, ERROR_notAcceptedSymbol, ERROR_singleExclamationMark
    ],

    #gia thn katastash equalSTATE
    [assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN,
     assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, equalTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN,
     assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, assignmentTOKEN,
     assignmentTOKEN, assignmentTOKEN, assignmentTOKEN, ERROR_notAcceptedSymbol, assignmentTOKEN
    ],

    #gia thn katastash hash_markSTATE
    [ERROR_singleHashMark, lordSTATE, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark,
     ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark,
     ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark, ERROR_singleHashMark,
     ERROR_singleHashMark, ERROR_singleHashMark, start_of_blockTOKEN, end_of_blockTOKEN, commentsSTATE, ERROR_singleHashMark,
     ERROR_singleHashMark, ERROR_notAcceptedSymbol, ERROR_singleHashMark
    ],

    #gia thn katastash commentsSTATE
    [commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE,
     commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE,
     commentsSTATE, commentsSTATE, maybe_closing_commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE,
     commentsSTATE, commentsSTATE, ERROR_EOFBeforeClosingComments
    ],

    #gia thn katastash maybe_closing_commentsSTATE
    [commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE,
     commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE, commentsSTATE,
     commentsSTATE, commentsSTATE, maybe_closing_commentsSTATE, commentsSTATE, commentsSTATE, startSTATE, commentsSTATE,
     commentsSTATE, commentsSTATE, ERROR_EOFBeforeClosingComments
    ],

    #gia thn katastash quotation_markSTATE
    [ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, lordSTATE, ERROR_singleQuotationMark, 
     ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, 
     ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, 
     ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, 
     ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, ERROR_singleQuotationMark, 
     ERROR_notAcceptedSymbol, ERROR_singleQuotationMark
    ]

]


family = ''
###DHMIOYRGEI TA DIAFORETIKA FAMILIES GIA KATHE TOKEN
def initfamily(current_state):
        global family

        if(current_state == id_kwrdTOKEN):
                family = 'FAMILY: identifier'
        elif(current_state == digitTOKEN):
                family = 'FAMILY: number'
        elif(current_state == addTOKEN or current_state == subTOKEN):
                family = 'FAMILY: addOperator'
        elif(current_state == mulTOKEN or current_state == divTOKEN):
                family = 'FAMILY: mulOperator'
        elif(current_state == smallerTOKEN or current_state == smaller_equalTOKEN or current_state == largerTOKEN or current_state == larger_equalTOKEN or current_state == differentTOKEN or current_state == equalTOKEN):
                family = 'FAMILY: relOperator'
        elif(current_state == assignmentTOKEN):
                family = 'FAMILY: assignment'
        elif(current_state == commaTOKEN or current_state == question_markTOKEN or current_state == colonTOKEN):
                family = 'FAMILY: delimiter'
        elif(current_state == left_bracketTOKEN or current_state == right_bracketTOKEN or current_state == left_parenthesisTOKEN or current_state == right_parenthesisTOKEN or current_state == start_of_blockTOKEN or current_state == end_of_blockTOKEN):
                family = 'FAMILY: groupSymbol'
        elif(current_state == EOFTOKEN):
                family = 'FAMILY: EOF'
        else:
                family = 'FAMILY: unknown'

        return family

###ELEGXEI KAI TYPWNEI OLA TA LATHH
def errorMessages(current_line, word_unit):
        if(current_state == ERROR_notAcceptedSymbol):
                print("***ERROR(lex)***: Found a not accepted symbol ( " + word_unit + " ) in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleSlash):
                print("***ERROR(lex)***: Found a single / in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_letterAfterDigit):
                print("***ERROR(lex)***: Found a letter character after a digit character ( " + word_unit + " ) in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_numberOutOfRange):
                print("***ERROR(lex)***: The number ' " + word_unit + " ' is not inside the accepted range of [-((2^32)-1), (2^32)-1)] in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_identifierOver30Characters):
                print("***ERROR(lex)***: Found an identifier with over 30 characters ( " + word_unit + " ) in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_EOFBeforeClosingComments):
                print("***ERROR(lex)***: Comments begin correctly with #$ but we get EOF before they end in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleDollarSign):
                print("***ERROR(lex)***: Found a single $ in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleLeftCurlyBrackets):
                print("***ERROR(lex)***: Found a single { in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleRightCurlyBrackets):
                print("***ERROR(lex)***: Found a single } in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_identifierStartsWithUnderscore):
                print("***ERROR(lex)***: Found the word ' " + word_unit + " ' starting with _ in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleExclamationMark):
                print("***ERROR(lex)***: Found a single ! in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleHashMark):
                print("***ERROR(lex)***: Found a single # in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_identifierStartsWithHashMarkWithoutBeingTheKeywordDeclare):
                print("***ERROR(lex)***: Found the identifier ' " + word_unit + " ' starting with # (NOT #declare) in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_singleQuotationMark):
                print("***ERROR(lex)***: Found a single \" in line: " + str(current_line))
                exit(-1)
        elif(current_state == ERROR_identifierContainsQuoteMarkWithoutBeingTheKeywordMain):
                print("***ERROR(lex)***: Found the identifier ' " + word_unit + " ' containing \" (NOT \"__main__\") in line: " + str(current_line))
                exit(-1)
        return()


line = 1  ##arxika eimai sthn 1h grammh


def lex():
        global line
        global current_state
        word_unit = ''                #lektikh monada arxika einai kenh
        current_state = startSTATE    #trexousa katastash arxika sto start
        current_line = line           #trexoysa grammh kwdika toy arxeioy filename

### RESULT einai to apotelesma poy epistrefetai se lista kathws exoyme 4 pragmata na epistrepsoyme se kathe klhsh ths lex
        result=[]

        while(0 <= current_state <= 11 ):
                char_read = file.read(1)  #diavazw ena xaraktira
                #print('char read: ', char_read)
                if (char_read == ' ' or char_read == '\t' ):
                        char = chars[0]
                elif ('a'<= char_read <= 'z' or 'A' <= char_read <= 'Z'):
                        char = chars[1]
                elif ('0'<= char_read <= '9'):
                        char = chars[2]
                elif (char_read == '_'):
                        char = chars[3]
                elif (char_read == '+'):
                        char = chars[4]
                elif (char_read == '-'):
                        char = chars[5]
                elif (char_read == '*'):
                        char = chars[6]
                elif (char_read == '/'):
                        char = chars[7]
                elif (char_read == '<'):
                        char = chars[8]
                elif (char_read == '>'):
                        char = chars[9]
                elif (char_read == '!'):
                        char = chars[10]
                elif (char_read == '='):
                        char = chars[11]
                elif (char_read == ';'):
                        char = chars[12]
                elif (char_read == ','):
                        char = chars[13]
                elif (char_read == ':'):
                        char = chars[14]
                elif (char_read == '['):
                        char = chars[15]
                elif (char_read == ']'):
                        char = chars[16]
                elif (char_read == '('):
                        char = chars[17]
                elif (char_read == ')'):
                        char = chars[18]
                elif (char_read == '#'):
                        char = chars[19]
                elif (char_read == '{'):
                        char = chars[20]
                elif (char_read == '}'):
                        char = chars[21]
                elif (char_read == '$'):
                        char = chars[22]
                elif (char_read == '"'):
                        char = chars[23]
                elif (char_read == '\n'):
                        current_line += 1    #ean diavasw char allagh grammhs paw sthn epomenh seira
                        char = chars[24]
                elif (char_read == ''):
                        char = chars[26]
                else:
                        char = chars[25]     #not_accepted_symbol

                positionofchar = chars.index(char)
                # nea current_state einai ean sthn trexousa katastash diabasw ton xarakthra char
                current_state = transition_matrix[current_state][positionofchar]

###SXHMATISE LEKTIKH MONADA PROSTHETONTAS TON XARAKTHRA POY DIABAZEIS KATHE FORA, EKTOS KAI AN EIMASTE SE SXOLIO 'H STHN ARXH GIA NA MHN PROSTHETEI TA KENA
                if(current_state != commentsSTATE and current_state != maybe_closing_commentsSTATE and current_state != startSTATE):
                        word_unit += char_read
                else:
                        word_unit = ''

                ###ELEGXW AN EINAI PANW APO 30 XARAKTHRES ENA ANAGNWRISTIKO
                while(current_state == id_kwrdTOKEN and len(word_unit)>30):
                        char = file.seek(file.tell()-1,0)
                        word_unit = word_unit[:-1]
                        current_state = ERROR_identifierOver30Characters

###OPISTHODROMISH    %%% GINETAI EAN EIMAI SE KATASTASEIS POU KATANALWNW TON EPOMENO XARAKTHRA GIA NA BRW TO TOKEN
        if(current_state == id_kwrdTOKEN or current_state == digitTOKEN or current_state == smallerTOKEN or current_state == largerTOKEN 
           or current_state == assignmentTOKEN or current_state == ERROR_singleSlash or current_state == ERROR_singleExclamationMark 
           or current_state == ERROR_singleHashMark or current_state == ERROR_singleQuotationMark):

                if(char_read == '\n'):
                        current_line -=1
                char = file.seek(file.tell()-1,0)   
                word_unit = word_unit[:-1]


###ELEGXW AN EINAI DESMEYMENH LEKSI
        if(current_state == id_kwrdTOKEN):
                for i in range(len(desmeumenes_lexeis)):
                        if(word_unit == desmeumenes_lexeis[i]):
                                result.append('FAMILY: keyword')
                                current_state = desmeumenes_lexeisTOKEN[i]


                ###ELEGXW AN KSEKINAEI APO # ENW DEN EINAI DESMEYMENH LEKSI
                if(word_unit[0] == '#' and word_unit != desmeumenes_lexeis[0] ):       #desmeumenes_lexeis[0] einai to '#declare'
                        current_state = ERROR_identifierStartsWithHashMarkWithoutBeingTheKeywordDeclare
                ###ELEGXW AN KSEKINAEI APO _ ENW DEN EINAI DESMEYMENH LEKSI
                if(word_unit[0] == '_' and (word_unit not in desmeumenes_lexeis) ):
                        current_state = ERROR_identifierStartsWithUnderscore
                ###ELEGXW AN EINAI H DESMEYMENH LEKSI "__main__" POY PERIEXEI " ALLIWS ERROR
                if(word_unit != '"__main__"' and ( '"' in word_unit)):       
                        current_state = ERROR_identifierContainsQuoteMarkWithoutBeingTheKeywordMain


###ELEGXW AN EINAI MESA STA EPITREPTA ORIA ENA NOYMERO (2^32)
        if(current_state == digitTOKEN and int(word_unit) >= pow(2,32)):                    
                current_state = ERROR_numberOutOfRange


###TYPWSE PITHANA ERRORS
        errorMessages(current_line, word_unit)
        
## TI EPISTREFEI H SYNARTHSH LEX
## result = ['FAMILY: ______', 'token pou sxhmatisthke', 'LINE', 'kwdikos kathe token' ]
        # result[0]
        if(current_state != id_kwrdTOKEN ):
                if(word_unit not in desmeumenes_lexeis):
                        result.append(initfamily(current_state))
                        exit
        else:
                result.append(initfamily(current_state))
                exit

        # result[1]
        result.append(word_unit)

        # result[2]
        result.append(current_line)

        # result[3]
        if(word_unit in desmeumenes_lexeis):
                keyword_state_num = 200 + desmeumenes_lexeis.index(word_unit)  #anathesh kwdikou sta token twn desmeumenwn leksewn
                result.append(keyword_state_num)
        else:
                result.append(current_state)


        line=current_line     #gia na synexizei h arithmish grammwn apo ekei poy emeine

        print(result)        
        return result




########    PINAKAS SYMBOLWN   #########
###*****************************************************************************************************************************************************************###
### ENTITY
class Entity():
        def __init__(self, name, type, offset, nestingLevel):
                self.name = name			                 #onoma tou entity
                self.type = type        		                 #typos tou entity
                self.variable = self.Variable(offset)                    #metavlhth
                self.function = self.Function(nestingLevel)              #synarthsh
                self.parameter = self.Parameter(offset)                  #parametros
                self.temporaryVariable = self.TemporaryVariable(offset)  #proswrinh metavlhth

        #metavlhth
        class Variable:
                def __init__(self, offset):
                        self.offset = offset		     #apostash apo thn arxh tou eggrafhmatos drasthriopoihshs

        #synarthsh
        class Function: 			
                def __init__(self, nestingLevel):
                        self.startQuad = 0		     #etiketa ths 1hs 4adas tou kwdika ths synarthshs 
                        self.argList = []		     #lista parametrwn 
                        self.framelength = 0		     #mhkos eggrafhmatos drasthriopoihshs
                        self.nestingLevel = nestingLevel     #(telikos extra gia sygkrish)
        
        #parametros
        class Parameter: 
                def __init__(self, offset):
                        self.offset = offset		     #apostash apo thn arxh tou eggrafhmatos drasthriopoihshs

        #proswrinh metavlhth
        class TemporaryVariable:
                def __init__(self, offset):
                        self.offset = offset		     #apostash apo thn arxh tou eggrafhmatos drasthriopoihshs

### PROSTHIKH NEOU ENTITY
def addEntity(name, type, offset, nestingLevel):  
        newEntity = Entity(name, type, offset, nestingLevel) #ftiaxnw neo entity
        scopeList[-1].entityList.append(newEntity)           #to prosthetw sth lista me ta entities tou teleytaiou scope

### PROSTHIKH PARAMETRWN STO SCOPE THS ANTISTOIXHS SYNARTHSHS WS ENTITY
def addParameter():  
        for arg in scopeList[-2].entityList[-1].function.argList:    #kathe parametro ths synarthshs tou prohgoumenou scope
                addEntity(arg.name, 'parameter', findOffset(), 0)       #thn prosthetw ws entity 

###*****************************************************************************************************************************************************************###
### SCOPE
scopeList = []                                  #lista me ola ta scopes
class Scope():
        def __init__(self, name):
                self.name = name		#onoma tou scope
                self.nestingLevel = 0           #vathos fwliasmatos, arxika einai 0
                self.entityList = []		#lista apo entities

### PROSTHIKH NEOU SCOPE
def addScope(name):
        newScope = Scope(name)                           #ftiaxnw neo scope

        if(scopeList):                                   #ean yparxei toulaxiston ena scope
                newScope.nestingLevel = scopeList[-1].nestingLevel + 1    #to vathos fwliasmatos tou neou scope einai auto tou teleytaiou scope + 1

        scopeList.append(newScope)                       #to prosthetw sth lista me ta scopes

### DIAGRAFH SCOPE 
def deleteScope(): 
        scopeList[-1].entityList.clear()                 #adiazw th lista me ta entities tou scope pou diagrafw

        del scopeList[-1]                                #diagrafw to idio to scope

###*****************************************************************************************************************************************************************###
### ARGUMENT
class Argument():
	def __init__(self, name):
		self.name = name	        #onoma tou scope

### PROSTHIKH NEOU ARGUMENT
def addArgument(name): 
	newArgument = Argument(name)                     #ftiaxnw neo argument
	scopeList[-1].entityList[-1].function.argList.append(newArgument)  #to prosthetw sth lista me ta arguments ths synarthshs tou teleutaiou scope
	

###****************************************************************************************************************************************************************###
### YPOLOGISMOS OFFSET GIA TA ENTITIES
def findOffset():
        offset = 12                                      #arxika einai 12
        for ent in (scopeList[-1].entityList):           #gia kathe entity tou teleutaiou scope 
                if(ent.type == 'variable' or ent.type == 'parameter' or ent.type=='temporary variable'): #mono gia tous typous pou exoun offset
                        offset += 4                      #ypologise to
               
        return offset

### YPOLOGISMOS FRAMELENGTH GIA TA FUNCTIONS
def findFramelength():
        # ypologizei to framelength ths synarthshs (afou exoume vrei to offset gia oles tis metavlites ths) kai to eisagei sthn synarthsh
        scopeList[-2].entityList[-1].function.framelength = findOffset()
        
### ANAZHTHSH SCOPE KAI ENTITY THS EGGRAFHS NAME
def searchEntity(name):
        lastScope=scopeList[-1]                         #teleutaio-pio prosfato scope
        while (scopeList):                              #oso yparxoun scope
                for el in lastScope.entityList:         #gia kathe entity
                        if(el.name == name):            #ean exei to idio onoma me auto pou psaxnoume
                                scope = lastScope       #enhmerwse to scope
                                entity = el             #enhmerwse to entity
                                return (scope, entity)  #epestrepse ta

                p = scopeList.index(lastScope)
                lastScope = scopeList[p-1]        #phgaine sto prohgoumeno scope
        
        print("***ERROR***: "+name+" not found")  #ean den vrethei typwse error message           


###*****************************************************************************************************************************************************************###
### TYPWNEI TON PINAKA SYMBOLWN STO ARXEIO pinakas_symbolwn.symb
def printSymb():
        file2.write("*************************************************************************************\n")
        file2.write("_____________________________________________________________________________________\n")
        
        lastScope=scopeList[-1]                          #teleutaio-pio prosfato scope
        while (scopeList):                               #oso yparxoun scope
                for sl in scopeList:                     #gia kathe scope
                        file2.write("*SCOPE*:  name: " + lastScope.name + "\t\t |nestingLevel: " + str(lastScope.nestingLevel) + "\n") #typwse to scope
                        for el in lastScope.entityList:  #gia kathe entity
                                if(el.type == 'variable'):               #typwse th metavlhth
                                        file2.write("\t*ENTITY*:  name: " + el.name + "\t\t |type: " + el.type + "\t\t |offset: " + str(el.variable.offset) + "\n")
                                elif(el.type == 'function'):             #typwse th synarthsh
                                        file2.write("\t*ENTITY*:  name: " + el.name + "\t |type: " + el.type + "\n")
                                        for al in el.function.argList:   #gia kathe argument ths synarthshs
                                                file2.write("\t\t*ARGUMENT*:  name: " + al.name + "\n")  #typwse to argument
                                elif(el.type == 'parameter'):            #typwse th parametro
                                        file2.write("\t*ENTITY*:  name: " + el.name +"\t\t |type: " + el.type + "\t\t |offset: " + str(el.parameter.offset) + "\n")
                                elif(el.type == 'temporary variable'):   #typwse th proswrinh metavlhth
                                        file2.write("\t*ENTITY*:  name: " + el.name +"\t\t |type: " + el.type + "\t |offset: " + str(el.temporaryVariable.offset) + "\n")
                        file2.write("_____________________________________________________________________________________\n")

                        p = scopeList.index(lastScope)
                        lastScope = scopeList[p-1]       #phgaine sto prohgoumeno scope
                          
                break
        file2.write("*************************************************************************************\n\n\n")
       
        



########    ENDIAMESOS KWDIKAS   #########

global listOfQuads  
listOfQuads = []    #krataei oles tis 4ades
quadCounter = 1     #prwth 4ada exei ton arithmo 1

tempListOfQuads = []

### epistrefei ton arithmo ths epomenhs 4adas pou prokeitai na paraxthei ###
def nextquad():
        global quadCounter
        return quadCounter

### dhmiourgei thn epomenh 4ada (op, operand1, operand2, target) ###
def genquad(op, x, y, z):
        global quadCounter
        
        quadList = [nextquad(), op, x, y, z]   #prosthetw sthn arxh ths 4adas (op, x, y, z) kai ton monadiko arithmo ths

        quadCounter += 1                       #auksanw ton monadiko arithmo ths epomenhs 4adas
        listOfQuads.append(quadList)           #prosthetw thn 4ada pou eftiaksa sth lista me oles tis 4ades
        tempListOfQuads.append(quadList)
        return quadList

### dhmiourgei kai epistrefei mia nea proswrinh metavlhth ths morfhs %1, %2, ..., %N ###
counter = 1
def newtemp(): 
        global counter 

        temp = "%" + str(counter)              #proswrinh metavlhth %1
        counter += 1                           #aukshsh tou arithmou ths proswrinhs metavlhths

        addEntity(temp, 'temporary variable', findOffset(), 0)  #edw dhlwnoume nea metavlhth gia ayto thn prosthetw ws entity
        
        return temp

### dhmiourgei mia kenh lista etiketwn 4adwn ###
def emptylist():
        emptyQuadList = []
        return emptyQuadList

### dhmiourgei mia lista etiketwn 4adwn pou periexei mono to x ###
def makelist(x):
        xlist = [x]
        return xlist

### dhmiourgei mia lista etiketwn 4adwn apo thn synenwsh twn listwn list1 kai list2 ###
def merge(list1, list2):
        mergedlist = list1+list2
        return mergedlist 

### h lista list apoteleitai apo deiktes se 4ades twn opoiwn to teleutaio teloumeno den einai symplhrwmeno ###
### h backpatch episkeptetai mia mia tis 4ades autes kai tis symplhrwnei me thn etiketa z ###
def backpatch(list, z):
        global listOfQuads
        for i in range(len(list)):   #gia kathe asymplhrwth 4ada
                for j in range(len(listOfQuads)):    #dietrekse th lista me oles tis 4ades
                        if(list[i] == listOfQuads[j][0]):   #ean vriskomai sth swsth tetrada(dhl thn asymplhrwth poy mou exei ypodeiksei h list)
                                listOfQuads[j][4] = z       #symplhrwnw thn teleytaia thesh me z

        return



###syntaktikos kai endiamesos kwdikas
def syn():
        global l
        l = lex()
        global temp_line

        def startRule():

                addScope('main')    #edw ksekinaei h metafrash ths main

                def_main_part()
                call_main_part()

        def def_main_part():
                global l

                def_main_function()
                while(l[1] == 'def'):
                        def_main_function()

        def def_main_function():
                global l
                global temp_line

                if(l[1] == 'def'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == id_kwrdTOKEN):    
                                if(l[1][0:5] == 'main_'):
                                        name = l[1]
                                        l = lex()
                                        
                                        if(l[3] == left_parenthesisTOKEN):
                                                l = lex()
                                                
                                                if(l[3] == right_parenthesisTOKEN):
                                                        l = lex()
                                                        
                                                        if(l[3] == colonTOKEN):
                                                                l = lex()
                                                                
                                                                if(l[3] == start_of_blockTOKEN):
                                                                        l = lex()
                                                                       
                                                                        addEntity(name, 'function', 0, scopeList[-1].nestingLevel+1)   #edw synantame dhlwsh neas synarthshs
                                                                        addScope(name)    #edw ksekinaei h metafrash mias neas synarthshs 

                                                                        declarations()
                                                                        while(l[1] == 'def'):
                                                                                def_function()
                                                                        
                                                                        genquad('begin_block', name, '_', '_')

                                                                        statements()
                                                                        findFramelength()  #ypologismos framelength gia thn main
                                                                        genquad('end_block', name, '_', '_')

                                                                        printSymb()     #typwnw ton pinaka symbolwn prin diagrapsw to scope
                                                                        fin()           #klhsh ths fin gia na grapsei ton teliko kwdika 
                                                                        deleteScope()   #diagrafw to scope

                                                                        if(l[3] == end_of_blockTOKEN):
                                                                                l = lex()
                                                                                
                                                                        else:
                                                                                print('***ERROR(syn)***:{def_main_function()}: Missing end of block statement "#}" in line: ', line)
                                                                                exit(-1)
                                                                else:
                                                                        print('***ERROR(syn)***:{def_main_function()}: Missing start of block statement "#{" in line: ', line)
                                                                        exit(-1)
                                                        else:
                                                                print('***ERROR(syn)***:{def_main_function()}: Missing colon ":" in line: ', temp_line)
                                                                exit(-1)
                                                else:
                                                        print('***ERROR(syn)***:{def_main_function()}: Missing right parenthesis ")" in line: ', temp_line)
                                                        exit(-1)
                                        else:
                                                print('***ERROR(syn)***:{def_main_function()}: Missing left parenthesis "(" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{def_main_function()}: Function\'s name does not start with \'main_\' in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{def_main_function()}: Missing function name in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{def_main_function()}: Program doesn\'t start with def statement in line: ', line)
                        exit(-1)

        def def_function():
                global l

                if(l[1] == 'def'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == id_kwrdTOKEN):
                                id = l[1]
                                l = lex()
                                
                                if(l[3] == left_parenthesisTOKEN):
                                        l = lex()
                                        
                                        addEntity(id, 'function', 0, scopeList[-1].nestingLevel+1)   #edw synantame dhlwsh neas synarthshs

                                        id_list("ARG")

                                        if(l[3] == right_parenthesisTOKEN):
                                                l = lex()
                                                
                                                if(l[3] == colonTOKEN):
                                                        l = lex()
                                                        
                                                        if(l[3] == start_of_blockTOKEN):
                                                                l = lex()

                                                                addScope(id)     #edw ksekinaei h metafrash mias neas synarthshs 
                                                                addParameter()   #edw synantame tis parametrous ths synarthshs
                                                                
                                                                declarations()
                                                                while(l[1] == 'def'):
                                                                        def_function()
                                                                
                                                                genquad('begin_block', id, '_', '_')   ####to eipa id anti gia name??
                                                                
                                                                statements()
                                                                findFramelength()  #ypologismos framelength gia thn main
                                                                genquad('end_block', id, '_', '_')

                                                                printSymb()     #typwnw ton pinaka symbolwn prin diagrapsw to scope
                                                                fin()           #klhsh ths fin gia na grapsei ton teliko kwdika 
                                                                deleteScope()   #diagrafw to scope
                                                                
                                                                if(l[3] == end_of_blockTOKEN):
                                                                        l = lex()
                                                                        
                                                                else:
                                                                        print('***ERROR(syn)***:{def_function()}: Missing end of block statement "#}" in line: ', line)
                                                                        exit(-1)
                                                        else:
                                                                print('***ERROR(syn)***:{def_function()}: Missing start of block statement "#{" in line: ', line)
                                                                exit(-1)
                                                else:
                                                        print('***ERROR(syn)***:{def_function()}: Missing colon ":" in line: ', temp_line)
                                                        exit(-1)
                                        else:
                                                print('***ERROR(syn)***:{def_function()}: Missing right parenthesis ")" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{def_function()}: Missing left parenthesis "(" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{def_function()}: Missing function name in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{def_function()}: Missing "def" statement in line: ', temp_line)
                        exit(-1)

        def declarations():
                global l

                while(l[1] == '#declare'):
                        declaration_line()

        def declaration_line():
                global l

                if(l[1] == '#declare'):
                        l = lex()
                        
                        id_list("VAR")

        def statement():
                global l

                if(l[3] == id_kwrdTOKEN or l[1] == 'print' or l[1] == 'return'):
                        simple_statement()
                elif(l[1] == 'if' or l[1] == 'while'):
                        structured_statement()
                else:
                        print('***ERROR(syn)***:{statement()}: Incorrect statement in line: ', line)
                        exit(-1)

        def statements():
                global l

                statement()
                while(l[3] == id_kwrdTOKEN or l[1] == 'print' or l[1] == 'return' or l[1] == 'if' or l[1] == 'while'):
                       statement()

        def simple_statement():
                global l

                if(l[3] == id_kwrdTOKEN):
                        assignment_stat()
                elif(l[1] == 'print'):
                        print_stat()
                elif(l[1] == 'return'):
                        return_stat()

        def structured_statement():
                global l

                if(l[1] == 'if'):
                        if_stat()
                elif(l[1] == 'while'):
                        while_stat()


        def assignment_stat():
                global l
                # S-> id:=E{P1} #

                if(l[3] == id_kwrdTOKEN):
                        token = l[1]
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == assignmentTOKEN):
                                l = lex()
                                
                                if(l[1] == 'int'):
                                        l = lex()
                                        
                                        if(l[3] == left_parenthesisTOKEN):
                                                l = lex()
                                                
                                                if(l[1] == 'input'):
                                                        l = lex()

                                                        # S-> input(id){P1} #
                                                        ###{P1}###
                                                        genquad('in', token, '_', '_')

                                                        if(l[3] == left_parenthesisTOKEN):
                                                                l = lex()
                                                                
                                                                if(l[3] == right_parenthesisTOKEN):
                                                                        l = lex()
                                                                        
                                                                        if(l[3] == right_parenthesisTOKEN):
                                                                                l = lex()
                                                                                
                                                                                if(l[3] == question_markTOKEN):
                                                                                        l = lex()
                                                                                        
                                                                                else:
                                                                                        print('***ERROR(syn)***:{assignment_stat()}: Missing ";" in line: ', temp_line)
                                                                                        exit(-1)
                                                                        else:
                                                                                print('***ERROR(syn)***:{assignment_stat()}: Missing right parenthesis ")" in line: ', temp_line)
                                                                                exit(-1)
                                                                else:
                                                                        print('***ERROR(syn)***:{assignment_stat()}: Missing right parenthesis ")" in line: ', temp_line)
                                                                        exit(-1)
                                                        else:
                                                                print('***ERROR(syn)***:{assignment_stat()}: Missing left parenthesis "(" in line: ', temp_line)
                                                                exit(-1)
                                                else:
                                                        print('***ERROR(syn)***:{assignment_stat()}: Missing "input" in line: ', temp_line)
                                                        exit(-1)
                                        else:
                                                print('***ERROR(syn)***:{assignment_stat()}: Missing left parenthesis "(" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        ###{P1}###
                                        Eplace = expression()
                                        genquad('=', Eplace, '_', token)

                                        if(l[3] == question_markTOKEN):
                                                l = lex()
                                                
                                        else:
                                                print('***ERROR(syn)***:{assignment_stat()}: Missing ";" in line: ', temp_line)
                                                exit(-1)
                        else:
                                print('***ERROR(syn)***:{assignment_stat()}: Missing assignment "=" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{assignment_stat()}: Missing identifier in line: ', temp_line)
                        exit(-1)

        def print_stat():
                global l
                # S-> print(E){P2} #

                if(l[1] == 'print'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == left_parenthesisTOKEN):
                                l = lex()
                                
                                ###{P2}###
                                Eplace = expression()
                                genquad('out', Eplace, '_', '_')

                                if(l[3] == right_parenthesisTOKEN):
                                        l = lex()
                                        
                                        if(l[3] == question_markTOKEN):
                                                l = lex()
                                                
                                        else:
                                                print('***ERROR(syn)***:{print_stat()}: Missing ";" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{print_stat()}: Missing right parenthesis ")" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{print_stat()}: Missing left parenthesis "(" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{print_stat()}: Missing "print" in line: ', temp_line)
                        exit(-1)

        def return_stat():
                global l
                # S-> return(E){P1} #

                if(l[1] == 'return'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == left_parenthesisTOKEN):
                                l = lex()
                                
                                ###{P1}###
                                Eplace = expression()
                                genquad('retv', Eplace, '_', '_')

                                if(l[3] == right_parenthesisTOKEN):
                                        l = lex()
                                        
                                        if(l[3] == question_markTOKEN):
                                                l = lex()
                                                
                                        else:
                                                print('***ERROR(syn)***:{return_stat()}: Missing ";" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{return_stat()}: Missing right parenthesis ")" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{return_stat()}: Missing left parenthesis "(" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{return_stat()}: Missing "return" in line: ', temp_line)
                        exit(-1)

        def if_stat():
                global l
                # S-> if B then {P1} S1 {P2} TAIL {P3} #
                # TAIL-> else S2 | TAIL-> e #

                if(l[1] == 'if'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == left_parenthesisTOKEN):
                                l = lex()
                                
                                ###{P1}###
                                B = condition()
                                backpatch(B[0], nextquad())

                                if(l[3] == right_parenthesisTOKEN):
                                        l = lex()
                                        
                                        if(l[3] == colonTOKEN):
                                                l = lex()
                                        
                                                if(l[3] == start_of_blockTOKEN):
                                                        l = lex()
                                                
                                                        statements()

                                                        ###EITE BRW { META APO : ###
                                                        ###{P2}###
                                                        ifList = makelist(nextquad())
                                                        genquad('jump', '_', '_', '_')
                                                        backpatch(B[1], nextquad())

                                                        if(l[3] == end_of_blockTOKEN):
                                                                l = lex()
                                                                
                                                        else:
                                                                print('***ERROR(syn)***:{if_stat()}: Missing end of block statement "#}" in line: ', line)
                                                                exit(-1)
                                                else:
                                                        statement()

                                                        ###EITE DEN BRW { META APO : ###
                                                        ###{P2}###
                                                        ifList = makelist(nextquad())
                                                        genquad('jump', '_', '_', '_')
                                                        backpatch(B[1], nextquad())


                                                if(l[1] == 'else'):
                                                        temp_line = l[2]
                                                        l = lex()
                                                        
                                                        if(l[3] == colonTOKEN):
                                                                l = lex()
                                                                
                                                                if(l[3] == start_of_blockTOKEN):
                                                                        l = lex()
                                                                        
                                                                        statements()

                                                                        ###EITE BRW { META APO : ###
                                                                        ###{P3}###
                                                                        backpatch(ifList, nextquad())

                                                                        if(l[3] == end_of_blockTOKEN):
                                                                                l = lex()
                                                                                
                                                                        else:
                                                                                print('***ERROR(syn)***:{if_stat()}: Missing end of block statement "#}" in line: ', line)
                                                                                exit(-1)
                                                                else:
                                                                        statement()

                                                                        ###EITE DEN BRW { META APO : ###
                                                                        ###{P3}###
                                                                        backpatch(ifList, nextquad())
                                                        else:
                                                                print('***ERROR(syn)***:{if_stat()}: Missing ":" in line: ', temp_line)
                                                                exit(-1)

                                                else:
                                                        #ean den exw else kane backpatch
                                                        backpatch(ifList, nextquad())  

                                        else:
                                                print('***ERROR(syn)***:{if_stat()}: Missing ":" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{if_stat()}: Missing right parenthesis ")" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{if_stat()}: Missing left parenthesis "(" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{if_stat()}: Missing "if" in line: ', temp_line)
                        exit(-1)

        def while_stat():
                global l
                # S-> while {P1} B do {P2} S1 {P3} #

                if(l[1] == 'while'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == left_parenthesisTOKEN):
                                l = lex()
                                
                                ###{P1}###
                                Bquad = nextquad()
                                B = condition()

                                if(l[3] == right_parenthesisTOKEN):
                                        l = lex()
                                        
                                        if(l[3] == colonTOKEN):
                                                l = lex()

                                                ###{P2}###  
                                                backpatch(B[0], nextquad())
                                                
                                                if(l[3] == start_of_blockTOKEN):
                                                        l = lex()
                                                        
                                                        statements()

                                                        ###EITE BRW { META APO : ###
                                                        ###{P3}###
                                                        genquad('jump', '_', '_', Bquad)
                                                        backpatch(B[1], nextquad())

                                                        if(l[3] == end_of_blockTOKEN):
                                                                l = lex()
                                                                
                                                        else:
                                                                print('***ERROR(syn)***:{while_stat()}: Missing end of block statement "#}" in line: ', line)
                                                                exit(-1)
                                                else:
                                                        
                                                        statement()
                                                        
                                                        ###EITE DEN BRW { META APO : ###
                                                        ###{P3}###
                                                        genquad('jump', '_', '_', Bquad)
                                                        backpatch(B[1], nextquad())

                                        else:
                                                print('***ERROR(syn)***:{while_stat()}: Missing ":" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{while_stat()}: Missing right parenthesis ")" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{while_stat()}: Missing left parenthesis "(" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{while_stat()}: Missing "while" in line: ', temp_line)
                        exit(-1)

        def id_list(switch):
                global l

                if(l[3] == id_kwrdTOKEN):
                        name = l[1]
                        l = lex()
                        
                        if(switch == "ARG"):
                                addArgument(name)   #edw synantame dhlwsh parametrou synarthshs
                        else:
                                addEntity(name, 'variable', findOffset(), 0)   #edw synantame dhlwsh neas metavlhths

                        while(l[3] == commaTOKEN):
                                l = lex()
                                
                                if(l[3] == id_kwrdTOKEN):
                                        name = l[1]
                                        l = lex()

                                        if(switch == "ARG"):
                                                addArgument(name)   #edw synantame dhlwsh parametrou synarthshs
                                        else:
                                                addEntity(name, 'variable', findOffset(), 0)   #edw synantame dhlwsh neas metavlhths
                                        
                                else:
                                        print('***ERROR(syn)***:{id_list()}: Missing identifier in line: ', line)
                                        exit(-1)

        def expression():
                global l
                # E-> T1(+T2{P1})* {P2} #

                optional_sign()
                T1place = term()

                while(l[3] == addTOKEN or l[3] == subTOKEN):
                        addOrSubSIGN = ADD_OP()
                        T2place = term()

                        ###{P1}###
                        w = newtemp()
                        genquad(addOrSubSIGN, T1place, T2place, w)
                        T1place = w

                ###{P2}###
                Eplace = T1place 
                return Eplace 

        def ADD_OP():
                global l

                if(l[3] == addTOKEN or l[3] == subTOKEN):
                        addOrSubOp = l[1]
                        l = lex()
                return addOrSubOp
                        

        def term():
                global l
                # E-> F1(xF2{P1})* {P2} #

                F1place = factor()

                while(l[3] == mulTOKEN or l[3] == divTOKEN):
                        mulOrDivSIGN = MUL_OP()
                        F2place = factor()

                        ###{P1}###
                        w = newtemp()
                        genquad(mulOrDivSIGN, F1place, F2place, w)
                        F1place = w

                ###{P2}###
                Tplace = F1place 
                return Tplace 

        def MUL_OP():
                global l

                if(l[3] == mulTOKEN or l[3] == divTOKEN):
                        mulOrDivOp = l[1]
                        l = lex()
                return mulOrDivOp
        

        def factor():
                global l

                if(l[3] == digitTOKEN):
                        Fplace = l[1]             #krataw th lektikh monada
                        l = lex()
                        
                elif(l[3] == left_parenthesisTOKEN):
                        l = lex()
                        
                        # F-> (E){P1} #
                        ###{P1}###
                        Eplace = expression()
                        Fplace = Eplace           #krataw to expression

                        if(l[3] == right_parenthesisTOKEN):
                                l = lex()
                                
                        else:
                                print('***ERROR(syn)***:{factor()}: Missing right parenthesis ")" in line: ', line)
                                exit(-1)

                elif(l[3] == id_kwrdTOKEN):
                        # F-> id{P2} #
                        temp_f = l[1]             #krataw th lektikh monada
                        l = lex()
                        
                        ###{P2}###
                        Fplace = idtail(temp_f)   #krataw to idtail ths lektikhs monadas

                else:
                        print('***ERROR(syn)***:{factor()}: Missing INTEGER or expression or identifier in line: ', line)
                        exit(-1)

                return Fplace

        def idtail(assign_v):
                global l

                if(l[3] == left_parenthesisTOKEN):
                        l = lex()
                        
                        actual_par_list()

                        w = newtemp()
                        genquad('par', w, 'RET', '_')
                        genquad('call', assign_v, '_', '_')

                        if(l[3] == right_parenthesisTOKEN):
                                l = lex()

                                return w
                        
                        else:
                                print('***ERROR(syn)***:{idtail()}: Missing right parenthesis ")" in line: ', line)
                                exit(-1)
                else:
                        return assign_v
                                

        def actual_par_list():
                global l

                if(l[3] == digitTOKEN or l[3] == left_parenthesisTOKEN or l[3] == id_kwrdTOKEN):

                        a = expression()
                        genquad('par', a, 'CV', '_')

                        while(l[3] == commaTOKEN):
                                l = lex()
                                
                                a = expression()
                                genquad('par', a, 'CV', '_')

        def optional_sign():
                global l

                if(l[3] == addTOKEN or l[3] == subTOKEN):
                        ADD_OP()

        def condition():
                global l
                # B-> Q1{P1} (or{P2}Q2{P3})* #

                Btrue = []   
                Bfalse = []  

                #kathe condition (sygkrish dld) dhmiourgei 2 4ades
                Q1 = bool_term()

                ###{P1}###
                Btrue = Q1[0]    #mia gia otan einai true h sygkrish
                Bfalse = Q1[1]   #kai mia gia otan einai false h sygkrish


                while(l[1] == 'or'):
                        l = lex()

                        ###{P2}###
                        backpatch(Bfalse, nextquad())
                        
                        Q2 = bool_term()

                        ###{P3}###
                        Btrue = merge(Btrue, Q2[0])  #sygxwneysh sth lista true twn 4adwn pou den mporoun na symplhrwthoun kai antistoixoun se alithi apotimhsh logikhs prakshs      
                        Bfalse = Q2[1]  #h lista false periexei thn 4ada h opoia antistoixei se mh alithi apotimhsh ths logikhs prakshs

                return Btrue, Bfalse
        

        def bool_term():
                global l
                # Q-> R1{P1} (and{P2}R2{P3})* #

                Qtrue = []
                Qfalse = []

                R1 = bool_factor()

                ###{P1}###
                Qtrue = R1[0]
                Qfalse = R1[1]

                while(l[1] == 'and'):
                        l = lex()

                        ###{P2}###
                        backpatch(Qtrue, nextquad())
                        
                        R2 = bool_factor()

                        ###{P3}###
                        Qfalse = merge(Qfalse, R2[1])
                        Qtrue = R2[0]

                return Qtrue, Qfalse
        

        def bool_factor():
                global l
                Rtrue = []
                Rfalse = []

                if(l[1] == 'not'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == left_bracketTOKEN):
                                l = lex()
                                
                                # R-> not(B){P1} #
                                B = condition()

                                if(l[3] == right_bracketTOKEN):
                                        l = lex()

                                        ###{P1}###
                                        Rtrue = B[1]    #B.false
                                        Rfalse = B[0]   #B.true
                                        
                                else:
                                        print('***ERROR(syn)***:{bool_factor()}: Missing right bracket "]" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{bool_factor()}: Missing left bracket "[" in line: ', temp_line)
                                exit(-1)

                elif(l[3] == left_bracketTOKEN):
                        temp_line = l[2]
                        l = lex()
                        
                        # R-> (B){P2} #
                        B = condition()

                        if(l[3] == right_bracketTOKEN):
                                l = lex()

                                ###{P2}###
                                Rtrue = B[0]
                                Rfalse = B[1]
                                        
                        else:
                                print('***ERROR(syn)***:{bool_factor()}: Missing right bracket "]" in line: ', temp_line)
                                exit(-1)

                else:
                        # R-> E1 relop E2{P3} #
                        E1place = expression()
                        relop = REL_OP()
                        E2place = expression()

                        ###{P3}###
                        Rtrue = makelist(nextquad())
                        genquad(relop, E1place, E2place, '_')
                        Rfalse = makelist(nextquad())
                        genquad('jump', '_', '_', '_')

                return Rtrue, Rfalse

        def REL_OP():
                global l

                if(l[3] == smaller_equalTOKEN or l[3] == smallerTOKEN or l[3] == larger_equalTOKEN or l[3] == largerTOKEN or l[3] == differentTOKEN or l[3] == equalTOKEN):
                        relop = l[1]
                        l = lex()
                else:
                        print('***ERROR(syn)***: Missing "<=" or "<" or ">=" or ">" or "!=" or "=="  in line: ', line)
                        exit(-1)

                return relop

        def call_main_part():
                global l

                if(l[1] == 'if'):
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[1] == '__name__'):
                                l = lex()
                                
                                if(l[3] == equalTOKEN):
                                        l = lex()
                                        
                                        if(l[1] == '"__main__"'):      
                                                l = lex()
                                                
                                                if(l[3] == colonTOKEN):
                                                        l = lex()
                                                        
                                                        genquad('begin_block', '"__main__"', '_', '_')

                                                        main_function_call()
                                                        while(l[3] == id_kwrdTOKEN):
                                                                main_function_call()

                                                        genquad('halt', '_', '_', '_')   #halt prin to end_block ths main
                                                        genquad('end_block', '"__main__"', '_', '_')

                                                        printSymb()     #typwnw ton pinaka symbolwn prin diagrapsw to scope
                                                        fin()           #klhsh ths fin gia na grapsei ton teliko kwdika 
                                                        deleteScope()   #diagrafw to scope

                                                else:
                                                        print('***ERROR(syn)***:{call_main_part()}: Missing ":" in line: ', temp_line)
                                                        exit(-1)
                                        else:
                                                print('***ERROR(syn)***:{call_main_part()}: Missing "__main__" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{call_main_part()}: Missing "==" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{call_main_part()}: Missing "__name__" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{call_main_part()}: Missing "if" in line: ', line)
                        exit(-1)

        def main_function_call():
                global l

                if(l[3] == id_kwrdTOKEN):
                        id = l[1]
                        temp_line = l[2]
                        l = lex()
                        
                        if(l[3] == left_parenthesisTOKEN):
                                l = lex()
                                
                                if(l[3] == right_parenthesisTOKEN):
                                        l = lex()
                                        
                                        if(l[3] == question_markTOKEN):
                                                l = lex()

                                                genquad('call', id, '_', '_')
                                                
                                        else:
                                                print('***ERROR(syn)***:{main_function_call()}: Missing ";" in line: ', temp_line)
                                                exit(-1)
                                else:
                                        print('***ERROR(syn)***:{main_function_call()}: Missing right parenthesis ")" in line: ', temp_line)
                                        exit(-1)
                        else:
                                print('***ERROR(syn)***:{main_function_call()}: Missing left parenthesis "(" in line: ', temp_line)
                                exit(-1)
                else:
                        print('***ERROR(syn)***:{main_function_call()}: Missing name of function in line: ', temp_line)
                        exit(-1)


        startRule()




########    TELIKOS KWDIKAS   #########

### v string, tr string
def loadvr(v,tr): 

        if(v.isdigit()):  #v stathera
                file3.write("li "+tr+","+v+"\n")  #li tr,v

        else:  #v katholikh metavliti
                (scope,entity) = searchEntity(v)

                #ean anhkei sto kyriws programma dld thn main
                if(scope.nestingLevel == 0 and entity.type == 'variable'):  #variable
                        file3.write("lw "+tr+",-"+str(entity.variable.offset)+"(gp) \n")           #lw tr,-offset(gp)         

                #an h v exei dhlwthei sth synarthsh pou ekteleitai ayth th stigmh (topikh metavliti, typikh parametros pou pernaei me timh, proswrinh metavliti)
                elif(scope.nestingLevel == scopeList[-1].nestingLevel): 
                        if(entity.type =='variable'):                       #variable
                                file3.write("lw "+tr+",-"+str(entity.variable.offset)+"(sp) \n")   #lw tr,-offset(sp)

                        elif(entity.type =='parameter'):                    #parameter
                                file3.write("lw "+tr+",-"+str(entity.parameter.offset)+"(sp) \n")  #lw tr,-offset(sp)

                        elif(entity.type =='temporaryVariable'):            #temporary variable
                                file3.write("lw "+tr+",-"+str(entity.temporaryVariable.offset)+"(sp) \n")  #lw tr,-offset(sp)
                                
                #an h v exei dhlwthei se progono ws topikh metavlhth ekei h typikh parametros pou pernaei me timh
                elif(scope.nestingLevel < scopeList[-1].nestingLevel): 
                        if(entity.type == 'variable'):                      #variable
                                gnlvcode(v)                                                        #gnlvcode()
                                file3.write("lw "+tr+",(t0) \n")                                   #lw tr,(t0)
                        elif(entity.type == 'parameter'):                   #parameter
                                gnlvcode(v)                                                        #gnlvcode()
                                file3.write("lw "+tr+",(t0) \n")                                   #lw tr,(t0)

### tr string, v string
def storerv(tr,v): 
        (scope,entity) = searchEntity(v)

        #ean h v einai katholikh metavlhth dld anhkei sto kyriws programma dld thn main
        if(scope.nestingLevel == 0 and entity.type == 'variable'): #variable
                file3.write("sw "+tr+",-"+str(entity.variable.offset)+"(gp) \n")                   #sw tr,-offset(gp)
                
        #ean h v einai topikh metavliti h typikh parametros poy pernaei me vathos fwliasmatos iso me to trexon h proswrinh metabliti
        elif(scope.nestingLevel == scopeList[-1].nestingLevel):
                if(entity.type == 'variable'):                     #variable
                        file3.write("sw "+tr+",-"+str(entity.variable.offset)+"(sp) \n")           #sw tr,-offset(sp)

                elif(entity.type == 'temporaryVariable'):          #temporary variable
                        file3.write("sw "+tr+",-"+str(entity.temporaryVariable.offset)+"(sp) \n")  #sw tr,-offset(sp)
                                
                elif(entity.type == 'parameter'):                  #parameter
                        file3.write("sw "+tr+",-"+str(entity.parameter.offset)+"(sp) \n")          #sw tr,-offset(sp)

        #ean h v einai topikh metavliti h typikh parametros poy pernaei me vathos fwliasmatos mikrotero apo to trexon
        elif(scope.nestingLevel < scopeList[-1].nestingLevel):
                if(entity.type == 'variable'):                     #variable
                        gnlvcode(v)                                                                #gnlvcode(v)
                        file3.write("sw "+tr+",(t0) \n")                                           #sw tr,(t0)

                elif(entity.type == 'parameter'):                  #parameter
                        gnlvcode(v)                                                                #gnlvcode(v)
                        file3.write("sw "+tr+",(t0) \n")                                           #sw tr,(t0)

### name onoma metavlitis
def gnlvcode(name):  

        file3.write("lw t0,-4(sp) \n")                 #lw t0,-4(sp)   stoiva tou gonea

        (scope,entity) = searchEntity(name)  #thelw to scope kai entity ths metavlitis

        #oses fores xreiastei
        #dld osh einai h apostash apo to scope pou eimai twra ews to scope pou vrethike h metavliti
        apostash = scopeList[-1].nestingLevel - scope.nestingLevel; 

        for i in range(0, apostash-1):       #-1 giati gia ton gonea exw hdh grapsei
                #stoiva tou progonou poy exei th metavliti
                file3.write("lw t0,-4(t0) \n")         #lw t0,-4(t0)

        if(entity.type == 'variable'):                 #variable
                file3.write("addi t0,t0,-"+str(entity.variable.offset)+"\n")   #addi t0,t0,-offset    dieuthinsh ths mh topikhs metavlitis
        elif(entity.type == 'parameter'):              #parameter
                file3.write("addi t0,t0,-"+str(entity.parameter.offset)+"\n")  #addi t0,t0,-offset    dieuthinsh ths mh topikhs metavlitis


def findRelop(string, i):
        branch = ""
        if(string == "=="):
                branch = "beq"
        elif(string == "!="):
                branch = "bnq"
        elif(string == ">"):
                branch = "bgt"
        elif(string == "<"):
                branch = "blt"
        elif(string == ">="):
                branch = "bge"
        elif(string == "<="):
                branch = "ble"
        
        loadvr(tempListOfQuads[i][2],"t1")   #loadvr(x,t1)
        loadvr(tempListOfQuads[i][3],"t2")   #loadvr(y,t2)
        file3.write(branch+",t1,t2,"+str(tempListOfQuads[i][4])+"\n")   #branch,t1,t2,z
		
def findOp(str, i):
        op = ""
        if(str == "+"):
                op = "add"
        elif(str == "-"):
                op = "sub"
        elif(str == "*"):
                op = "mul"
        elif(str == "//"):
                op = "div"

        loadvr(tempListOfQuads[i][2],"t1")   #loadvr(x,t1)
        loadvr(tempListOfQuads[i][3],"t2")   #loadvr(y,t2)
        file3.write(op+" t1,t1,t2 \n")       #op t1,t1,t2
        storerv("t1",tempListOfQuads[i][4])  #storervr(t1,z)


### ANOIGMA ARXEIOY GIA TELIKO KWDIKA ###
file3 = open('telikos.asm', 'w')
file3.write("L0:\n")
file3.seek(17,0)   #afhnw 17 xarakthres gia na xwraei to L0:\n b(jump) xx\n

def fin():  
        global tempListOfQuads

        for i in range(len(tempListOfQuads)):   #diatrexei oles tis 4ades pou exoun dhmiourghthei ews otan kleithei

                file3.write("L" +str(tempListOfQuads[i][0])+ ": \n")   #L label 

                # jump,"_","_",label
                if(tempListOfQuads[i][1] == "jump"): 
                        file3.write("b(jump) "+str(tempListOfQuads[i][4])+"\n")
                # beq,x,y,z
                elif(tempListOfQuads[i][1] == "=="): 
                        findRelop("==", i)
                # bne,x,y,z
                elif(tempListOfQuads[i][1] == "!="): 
                        findRelop("!=", i)
                # bgt,x,y,z
                elif(tempListOfQuads[i][1] == ">"): 
                        findRelop(">", i)
                # blt,x,y,z
                elif(tempListOfQuads[i][1] == "<"): 
                        findRelop("<", i)
                # bge,x,y,z
                elif(tempListOfQuads[i][1] == ">="):
                        findRelop(">=", i)
                # ble,x,y,z
                elif(tempListOfQuads[i][1] == "<="): 
                        findRelop("<=", i)	
                # =,x,"_",z
                elif(tempListOfQuads[i][1] == "="): 
                        loadvr(tempListOfQuads[i][2],"t1")      #loadvr(x, t1)
                        storerv("t1",tempListOfQuads[i][4])     #storerv(t1, z)
                # add x,y,z
                elif(tempListOfQuads[i][1] == "+"): 
                        findOp("+", i)
                # sub x,y,z
                elif(tempListOfQuads[i][1] == "-"): 
                        findOp("-", i)
                # mul x,y,z
                elif(tempListOfQuads[i][1] == "*"): 
                        findOp("*", i)
                # div x,y,z
                elif(tempListOfQuads[i][1] == "//"):
                        findOp("//", i)
                # retv "_","_",x
                elif(tempListOfQuads[i][1] == "retv"):        
                        loadvr(tempListOfQuads[i][2],"t1")      #loadvr(x,t1)
                        file3.write("lw t0,-8(sp) \n")          #lw t0,-8(sp)
                        file3.write("sw t1,(t0) \n")            #sw t1,(t0)
                        # kai termatizei amesws h synarthsh
                        file3.write("lw ra,(sp) \n")            #lw ra,(sp)     pairnoume th dieuthinsi epistrofhs ths synarthshs kai thn vazoume ston ra
                        file3.write("jr ra \n")                 #jr ra          mesw tou ra epistrefoume sthn kalousa synarthsh
                # par,x,CV,_
                elif(tempListOfQuads[i][1] == "par" and tempListOfQuads[i][3] == "CV"):  
                        file3.write("addi fp,sp,framelength \n")             #framelength?? den to vrhkame***
                        loadvr(tempListOfQuads[i][2],"t0")                   #loadvr(x, t0)
                        file3.write("sw t0,-"+str(12+4*i)+"(fp) \n" )        #sw t0,-(12+4*i)(fp)
                        i=i+1                                                #i=aukswn arithmos ths parametrou
                # par,x,RET,_
                elif(tempListOfQuads[i][1] == "par" and tempListOfQuads[i][3] == "RET"):     
                        file3.write("addi fp,sp,framelength \n")             #framelength?? den to vrhkame** 
                        (scope,entity)=searchEntity(tempListOfQuads[i][2])   #psaxnw thn proswrinh metavliti x gia na vrw to offset ths
                        file3.write("addi t0,sp,-"+ str(entity.temporaryVariable.offset) +"\n" )  #addi t0,sp,-offset
                        file3.write("sw t0,-8(fp) \n")                                            #sw t0,-8(fp)
                # call,_,_,f
                elif(tempListOfQuads[i][1] == "call"): 
                        (scope,entity)=searchEntity(tempListOfQuads[i][2])
                        if (scopeList[-1].nestingLevel == entity.function.nestingLevel):      #kalousa kai klitheisa exoun idio vathos fwliasmatos
                                file3.write("lw t0,-4(sp)\n")   #lw t0,-4(sp)
                                file3.write("sw t0,-4(fp)\n")   #sw t0,-4(fp)
                        elif (scopeList[-1].nestingLevel != entity.function.nestingLevel):    #kalousa kai klitheisa exoun diaforetiko vathos fwliasmatos
                                file3.write("sw sp,-4(fp)\n")   #sw t0,-4(fp)
                        file3.write("addi sp,sp,"+ str(entity.function.framelength) +"\n")    #addi sp,sp,framelength
                        file3.write("jal "+str(tempListOfQuads[i][4])+"\n")                   #jal f
                        file3.write("addi sp,sp,"+ str(entity.function.framelength) +"\n")    #addi sp,sp,-framelength
                #klhsh synarthshs
                # begin_block/end_block oxi sthn main
                elif(tempListOfQuads[i][1] == "begin_block" and scopeList[-1].nestingLevel != 0):   
                        file3.write("sw ra,(sp) \n")            #sw ra,(sp)
                elif(tempListOfQuads[i][1] == "end_block" and scopeList[-1].nestingLevel != 0):  
                        file3.write("lw ra,(sp) \n")            #lw ra,(sp)
                        file3.write("jr ra \n")                 #jr ra
                #arxh programmatos kai kyriws programma
                # begin_block mesa sthn main
                elif(tempListOfQuads[i][1] == "begin_block" and scopeList[-1].nestingLevel == 0):  
                        #den metafrazetai to kyriws programma 1o kai gia ayto xreiazomai jump sthn 1h etiketa tou kyriws programmatos
                        file3.seek(5, 0)   #phnaine sthn arxh tou file3
                                           #grapse to jump
                        file3.write("b(jump) "+ str(tempListOfQuads[i][0]) +"\n")  #jump sthn 4ada pou exei to begin_block ths main 
                        file3.seek(0, 2)   #phnaine sto telos tou file3
                
                        file3.write("addi sp,sp,"+ str(findOffset()) +"\n")   #addi sp,sp,framelength     katevazoume ton sp kata framelength ths main
                        file3.write("mv gp,sp \n")                            #move gp,sp      shmeiwnoume ston gp to eggrafhma drasthriopoihshs ths main
                #eisodos dedomenwn
                elif(tempListOfQuads[i][1] == "in"): 
                        file3.write("li a7,5 \n")            #li a7,5
                        file3.write("ecall \n")              #ecall 
                #eksodos dedomenwn
                elif(tempListOfQuads[i][1] == "out"): 
                        loadvr(tempListOfQuads[i][2],"t1")   #lw  ... 
                        file3.write("li a7,1 \n")            #li a7,1
                        file3.write("ecall \n")              #ecall
                        file3.write("la a0,str_nl \n")       #la a0,str_nl
                        file3.write("li a7,4 \n")            #li a7,4
                        file3.write("ecall \n")              #ecall
                # halt,_,_,_
                elif(tempListOfQuads[i][1] == "halt"): 
                        file3.write("li a0,0 \n")            #li a0,0
                        file3.write("li a7,93 \n")           #li a7,93
                        file3.write("ecall \n")              #ecall

        tempListOfQuads = []   #thn adeiazw gia na parw tis epomenes 4ades mexri na ksanaklithei 



def intt(file1):
        'Write listOfQuads at intFile.int'
        for quad in listOfQuads:
                for i in quad:
                        file1.write(str(i) + "   ") 
                file1.write("\n") 

file1 = open('endiamesos_kwdikas.int', 'w')
file2 = open('pinakas_symbolwn.symb', 'w')

syn()
print("*****FINISHED WITHOUT ERRORS*****")


intt(file1)
file1.close()
file2.close()
file3.close()

