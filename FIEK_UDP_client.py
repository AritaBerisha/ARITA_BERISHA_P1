import socket
host = 'localhost'
port =12000

ClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Metodat qe mund te implementohen nga UDP serveri jane:\n1.IPADRESA - Tregon IP-n tuaj.\n2.NUMRIIPORTIT\n3.BASHKETINGELLORE - Kthen bashketingelloret ne fjaline e dhene (BASHKETINGELLORE teksti)\n4.PRINTIMI - Printon fjalen qe ju e jepni (PRINTIMI tekti)\n5.EMRIKOMPJUTERIT - Emri i Hostuesit.\n6.KOHA - Kthen Kohen e tanishme \n7.LOJA - 7 numra te rastesishem ne intervalin[1-49].\n8.FIBONACCI\n9.KONVERTIMI - Konvertime te ndryshme: \n KilowattToHorsepower, HorsepowerToKilowatt, DegreesToRadians, RadiansToDegrees, GallonsToLiters, LitersToGallons ( KONVERTIMI emriKonvertimit numri )\n10.VALIDEMAIL - tregon a eshte valide nje email (VALIDEMAIL email)\n11.PERSERITJA - tregon sa shkronja jane perseritur ne tekst PERSERITJA text)\nJU LUTEMI SHKRUANI EMRAT E METODAVE ME TE MEDHA!\n" )

teksti = input("Kerkesa:")
ClientSocket.sendto(str.encode(teksti),(host,port))
data, address=ClientSocket.recvfrom(1024)
print('Te dhenat e pranuar nga serveri:', repr(data.decode()))

ClientSocket.close()
