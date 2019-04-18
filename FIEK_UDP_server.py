
import socket
import random
import datetime
import math
import sys

host= "127.0.0.1"
port= 12000


serverSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
serverSocket.bind((host, port))

print("UDP serveri eshte gati per te marre kerkese.")


def IPADRESA():
  return("Ip Adresa e Klientit eshte: "+ address[0])

def NUMRIPORTIT():
  return("Numri i Portit eshte:"+str(address[1]))


def EMRIKOMPJUTERIT():
  EmriHostit = socket.gethostname()
  return("Emri i kompjuterit ose i Hostit eshte:"+EmriHostit)


def BASHKETINGELLORE(teksti):
  bashketingelloret = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'Z'}
  num = 0
  for i in teksti:
   if i in bashketingelloret:
    num+=1
  pergjigjja = "Teksti permban "+str(num)+" bashketingellore"
  return pergjigjja

def PRINTIMI(teksti):
  fjaliaP = teksti.strip()
  return fjaliaP

def KOHA():
  Koha = datetime.datetime.now().strftime('%Y.%m.%d %I:%M:%S %p')
  return str(Koha)

def LOJA():
   numrat=[]
   for i in range(7):
    numrat.append(random.randint(1,49))
   return str(numrat)

 
def FIBONACCI(teksti):
  num=int(teksti)
  if(num==0 or num==2):
   rezultati=num
  else:
   numriPare = 0
   numriDyte = 1
   rezultati = 0
   for i in range(2,num+1):
       rezultati=numriPare+numriDyte
       numriPare=numriDyte
       numriDyte=rezultati
   return str(rezultati)

def KONVERTIMI(teksti, num):
  if(teksti=="KilowattToHorsepower"):
   return str(num / 0.745699872)
  elif(teksti=="HorsepowerToKilowatt"):
   return str(num*0.745699872)
  elif(teksti=="DegreesToRadians"):
   return str(num*math.pi/180)
  elif(teksti=="RadiansToDegrees"):
   return str(num*180/math.pi)
  elif(teksti=="GallonsToLiters"):
   return str(num*3.78541)
  elif(teksti=="LitersToGallons"):
   return str(num/3.78541)
  else:
   return("Nuk eshte dhene nje opsion valid.")

def VALIDEMAIL(teksti):
  if (("@" in teksti) and ("." in teksti) and 
  (teksti.index("@") > 0) and (teksti.index(".c") > teksti.index("@"))):
    return("Sintaksa perputhet per validim.")
  else:
    return("Sintaksa nuk perputhet per validim.")
 
def PERSERITJA(teksti1):
  teksti = teksti1.upper()
  num = 0
  for i in teksti:
    if teksti.count(i)>=2 and i!=' ':
      num += 1
      teksti=teksti.replace(i,"")
  return ("Numri i shkronjave qe perseriten ne tekst jane: "+str(num))

while True:
  try:
   kerkesa, address = serverSocket.recvfrom(1024)
   inputi1= kerkesa.decode()
   inputi=inputi1.split(" ")
  
   if sys.getsizeof(inputi1)>2 and sys.getsizeof(inputi1)<129:
    if inputi[0]=='IPADRESA':
     serverSocket.sendto(str.encode(IPADRESA()),address)
    elif inputi[0]=="NUMRIIPORTIT":
     serverSocket.sendto(str.encode(NUMRIPORTIT()),address)
    elif inputi[0]=="BASHKETINGELLORE":
     serverSocket.sendto(str.encode(BASHKETINGELLORE(inputi1[17:])),address)
    elif inputi[0]=="PRINTIMI":
     serverSocket.sendto(str.encode(PRINTIMI(inputi1[9:])),address)
    elif inputi[0]=="EMRIKOMPJUTERIT":
     serverSocket.sendto(str.encode(EMRIKOMPJUTERIT()),address)
    elif inputi[0]=='KOHA':
     serverSocket.sendto(str.encode(KOHA()),address)
    elif inputi[0]=="LOJA":
     serverSocket.sendto(str.encode(LOJA()),address)
    elif inputi[0]=="FIBONACCI":
     serverSocket.sendto(str.encode(FIBONACCI(inputi[1])),address)
    elif inputi[0]=="KONVERTIMI":
     numri = int(inputi[2])
     serverSocket.sendto(str.encode(KONVERTIMI(inputi[1],numri)),address)
    elif inputi[0]=="VALIDEMAIL":
     serverSocket.sendto(str.encode(VALIDEMAIL(inputi[1])),address)
    elif inputi[0]=="PERSERITJA":
     serverSocket.sendto(str.encode(PERSERITJA(inputi1[11:])),address)
    else:
     serverSocket.sendto("Kjo kerkese nuk ekziston".encode('utf-8'),address)
   else:
    serverSocket.sendto("Gabim".encode('utf-8'),address)
  except:
   pass


serverSocket.close()
