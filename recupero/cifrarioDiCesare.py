from string import ascii_lowercase

def caesar_cypher_encrypt(s, key)->str:
    lista=list(ascii_lowercase)
    parola=""
    for carattere in s:
        i=lista.index(carattere)
        i+=key
        i%=len(lista)
        parola+=lista[i]
    return parola


def caesar_cypher_decrypt(s, key)->str:
    lista=list(ascii_lowercase)
    parola=""
    for carattere in s:
        i=lista.index(carattere)
        i-=key
        i%=len(lista)
        parola+=lista[i]
    return parola

original = "hello"
key = 3
encrypted = caesar_cypher_encrypt(original, key)
decrypted = caesar_cypher_decrypt(encrypted, key)
print("Test 1 - Encrypt:", encrypted)   
print("Test 1 - Decrypt:", decrypted)