import socket
import threading
import random
import datetime
import math
import sys

class ThreadedServer(object):

 def __init__(self, host, port):
        self.host = 'localhost'
        self.port = 12000
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print('Serveri eshte startuar ne localhost ne portin ' + str(self.port))

 def listen(self):
        self.sock.listen(5)
        print('Serveri eshte i gatshem te pranoj kerkesa')
        while True:
            socketKlienti, address = self.sock.accept()
            socketKlienti.settimeout(60)
            t=threading.Thread(target = handle_client,args = (socketKlienti, address))
            t.start()
            print(str(address[0])+" u lidh ne portin: "+str(address[1]) + ".")

def handle_client(socketKlienti, address):
 def IPADRESA():
  return("IpAdresa e Klientit eshte: "+ address[0])

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

 def PRINTIMI(fjalia):
  fjaliaP = fjalia.strip()
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
   return("Nuk eshte dhene nenmetoda e duhur.")

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
    if teksti.count(i)>=2:
      num += 1
      teksti=teksti.replace(i,"")
  return ("Numri i shkronjave qe perseriten ne tekst jane: "+str(num))

 while True:
  try:
   inputi=socketKlienti.recv(1024)
   inputi=inputi.decode()
   kerkesa=inputi.split(" ")
  
   if sys.getsizeof(inputi)>1 and sys.getsizeof(inputi)<129:
    if kerkesa[0]=='IPADRESA':
     socketKlienti.send(str.encode(IPADRESA()))
    elif kerkesa[0]=="NUMRIIPORTIT":
     socketKlienti.send(str.encode(NUMRIPORTIT()))
    elif kerkesa[0]=="BASHKETINGELLORE":
     socketKlienti.send(str.encode(BASHKETINGELLORE(inputi[17:])))
    elif kerkesa[0]=="PRINTIMI":
     socketKlienti.send(str.encode(PRINTIMI(inputi[9:])))
    elif kerkesa[0]=="EMRIKOMPJUTERIT":
     socketKlienti.send(str.encode(EMRIKOMPJUTERIT()))
    elif kerkesa[0]=='KOHA':
     socketKlienti.send(str.encode(KOHA()))
    elif kerkesa[0]=="LOJA":
     socketKlienti.send(str.encode(LOJA()))
    elif kerkesa[0]=="FIBONACCI":
     socketKlienti.send(str.encode(FIBONACCI(kerkesa[1])))
    elif kerkesa[0]=="KONVERTIMI":
     numri = int(kerkesa[2])
     socketKlienti.send(str.encode(KONVERTIMI(kerkesa[1],numri)))
    elif kerkesa[0]=="VALIDEMAIL":
     socketKlienti.send(str.encode(VALIDEMAIL(kerkesa[1])))
    elif kerkesa[0]=="PERSERITJA":
     socketKlienti.send(str.encode(PERSERITJA(inputi[11:])))
    else:
     socketKlienti.send("Kjo kerkese nuk ekziston".encode('utf-8'))
   else:
    socketKlienti.send("Gabim".encode('utf-8'))
  except:
   socketKlienti.close()
   False
  

if __name__ == "__main__":
    port_num = 12000
    ThreadedServer('',port_num).listen() 




