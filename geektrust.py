from shanfamily import ShanFamily
import os
import sys
import argparse

def main():
    if(len(sys.argv)==1 ):
        print('Filename not passed as argument')
    elif( len(sys.argv)>2 ):
        print('Invalid number of inputs')
    else:

        input_file = sys.argv[1]
        # parse the file and process the command
        if (os.path.isfile(input_file)!=True):
            print(input_file+" is an invalid file")
        else:
            readfile=open(input_file, 'r') 
            lines=readfile.readlines()
            if(len(lines)==0):
                print('No input to process')
            else:
                    family=ShanFamily()
                    for i in range(0,len(lines)):
                        line=lines[i]
                        input=line.strip('\n').split(' ') 
                        if (len(input)==0):
                            print('Line number '+str(i)+' is empty')
                        elif (input[0]=='GET_RELATIONSHIP'):
                            if(len(input)==3):
                                result=family.GET_RELATIONSHIP(input[1],input[2])
                                if(result!='PERSON_NOT_FOUND' and ('NOT_FOUND' in result)):
                                    print('NONE')
                                else:
                                    print(result)
                            else:
                                print('Invalid number of arguments for GET_RELATIONSHIP')
                        elif (input[0]=='ADD_CHILD'):
                            if(len(input)==4):
                                print(family.ADD_CHILD(input[1],input[2],input[3]))
                            else:
                                print('Invalid number of arguments for ADD_CHILD')
                        elif (input[0]=='ADD_SPOUSE'):
                            if(len(input)==3):
                                print(family.ADD_SPOUSE(input[1],input[2]))
                            else:
                                print('Invalid number of arguments for ADD_SPOUSE')
                        else:
                            print('Invalid Command')
        # print the output

if __name__ == "__main__":
    main()