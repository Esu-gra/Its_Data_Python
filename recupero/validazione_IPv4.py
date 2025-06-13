'''
Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.
'''


def is_valid_ipv4(address:str)->bool:

    if len(address)!=4:
        return False
    
    for x in address:
        if not x.isdigit():
            return False
    
    n=x(int)

    if not (0<=n<=255):
        return False

    return True
    



    
      
 
    
    
            