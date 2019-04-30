import socket
servername = 'localhost'
port = 12000

socketKlient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Metodat qe mund te implementohen nga UDP serveri jane:\n1.IPADRESA - Tregon IP-n tuaj.\n2.NUMRIIPORTIT\n3.BASHKETINGELLORE - Kthen bashketingelloret ne fjaline e dhene (BASHKETINGELLORE teksti)\n4.PRINTIMI - Printon fjalen qe ju e jepni (PRINTIMI tekti)\n5.EMRIKOMPJUTERIT - Emri i Hostuesit.\n6.KOHA - Kthen Kohen e tanishme \n7.LOJA - 7 numra te rastesishem ne intervalin[1-49].\n8.FIBONACCI - (FIBONACCI numri)\n9.KONVERTIMI - Konvertime te ndryshme: \n KilowattToHorsepower, HorsepowerToKilowatt, DegreesToRadians, RadiansToDegrees, GallonsToLiters, LitersToGallons ( KONVERTIMI emriKonvertimit numri )\n10.VALIDEMAIL - tregon a eshte valide nje email (VALIDEMAIL email)\n11.PERSERITJA - tregon sa shkronja jane perseritur ne tekst PERSERITJA text)\nJU LUTEMI SHKRUANI EMRAT E METODAVE ME TE MEDHA!\n" )
socketKlient.connect((servername,port))

while True:
 data = input("Ju lutem shenoni nje metode: ")
 socketKlient.sendall(str.encode(data))
 pergjigja = socketKlient.recv(1024).decode()
 print('Te dhenat e pranuar nga serveri:', repr(pergjigja))
