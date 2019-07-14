#!/usr/bin/python
import os
import random
import sys
import curses

rr = '\033[0m'  # reset
bold = '\033[01m'
d = '\033[02m'  # disable
ul = '\033[04m'  # underline
reverse = '\033[07m'
st = '\033[09m'  # strikethrough
invis = '\033[08m'  # invisible
white = '\033[0m'
cwhite = '\33[37m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lgrey = '\033[37m'
grey = '\033[90m'
lred = '\033[91m'
lgreen = '\033[92m'
yellow = '\033[93m'
lblue = '\033[94m'
pink = '\033[95m'
lcyan = '\033[96m'
bgreen = '\33[42m'
blgreen = '\33[102m'
bred = '\33[41m'
blred = '\33[101m'
borange = '\33[43m'
byellow = '\33[33m'
bcyan = '\33[44m'
blcyan = '\33[104m'
br = '\33[108m'
brown = '\33[33m'
bwhite = '\33[107'


def clear():
    for i in range(0, 5):
        os.system("clear")


def quit():
    sys.exit()

def textlogo():
    print(lpurple + bold + """
███╗   ███╗ █████╗ ██╗     ███████╗ █████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██╔████╔██║███████║██║     █████╗  ███████║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██║╚██╔╝██║██╔══██║██║     ██╔══╝  ██╔══██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  
██║ ╚═╝ ██║██║  ██║███████╗██║     ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                                    
""" + rr)

def random_logo():
    x = random.randint(1, 3)
    if x == 1:
        logo1()
    elif x == 2:
        logo2()
    elif x == 3:
        logo3()
    options()


def logo1():
    print(lgreen + """
                                ██████         ██████
                           █████████████████████████
                         ████            ██
                  ██████████
             █████████████
            ███                                       ████
           ███                      ███        █████████
                                      ███████████

                
        ██████████████████████████
          ██████████████████████
          ██████████████████████
          ██████████████████████
          ██████████████████████
          ██████████████████████
          ██████████████████████
         ██████ ████████  ██████
        █████     █████     █████
        ████       ███       ████
       ████                   ████
      █████                   █████
     █████████████    ██████████████
     ████████████      █████████████
    ████████████        █████████████
   █████████████         █████████████
  ███████████████      ████████████████
 ███████████████████████████████████████
  █████████████████████████████████████
           ███████████████████
""" + rr)


def logo2():
    print(lred + """

                            ████                            
                      ████████████████                      
                    █████          █████                    
                   ████              ████                   
                  ████                ████                  
                 █████                █████                 
  ███      ██████████████████████████████████████      ███  
   ████   ████             ██████             ████   ████   
     ████████               ████               ████████     
       ██████               ████               ██████       
         ████               ████               ████         
          ███               ████               ███          
          ███               ████               ███          
          ███               ████               ███          
          ███               ████               ███          
        █████               ████               █████        
█████████████               ████               █████████████
         ████               ████               ████         
          ███               ████               ███          
          ████              ████              ████          
           ███              ████              ███           
          █████             ████             █████          
        █████████           ████           █████████        
      ████    █████         ████         █████    ████      
    ████        █████       ████       █████        ████    
  ████             ██████████████████████             ████  
                       ██████████████                       
""")


def logo3():
    print(lgrey + """
           ██                ██████                         
             ████            ██████████                     
              █████              █████████                  
              ███████              ██████████               
              ███████                ██████████             
 █           ████████                 ███████████           
 ███        █████████                 █████████████         
  ███████████████████                   ████████████        
    ███████████████████                  ████████████       
      ███████████████████          ████    ███████████     
                █████████       ████████        ██████████  
                  █████      ███████████         ██████████ 
                          █████████████          ████████   
                        ████████████               ███      
                      ████████████                          
                   █████████████                            
                 ████████████      █████                    
               ████████████      █████████                  
            █████████████         ██████████            
          ████████████              ███████████████████     
        ████████████                  ███████████████████   
     █████████████                    █████████████   ████  
   █████████████                      █████████         ██  
 █████████████                        ████████              
████████████                           ██████               
 ████████                              ██████               
    ███                                  █████              
                                           █████            
                                              ███           
""")
