letters = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
           "1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}",
           "\\","|",";","'",",",".","/","<",">","?",
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

wc = """
   ▄█    █▄       ▄████████    ▄█    █▄       ▄████████         ▄████████    ▄████████  ▄████████    ▄████████    ▄████████     ███     
  ███    ███     ███    ███   ███    ███     ███    ███        ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ ▀█████████▄ 
  ███    ███     ███    █▀    ███    ███     ███    █▀         ███    █▀    ███    █▀  ███    █▀    ███    ███   ███    █▀     ▀███▀▀██ 
 ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄███▄▄  ▄███▄▄▄            ███         ▄███▄▄▄     ███         ▄███▄▄▄▄██▀  ▄███▄▄▄         ███   ▀ 
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ▀███████████ ▀▀███▀▀▀     ███        ▀▀███▀▀▀▀▀   ▀▀███▀▀▀         ███     
  ███    ███     ███    █▄    ███    ███     ███    █▄                ███   ███    █▄  ███    █▄  ▀███████████   ███    █▄      ███     
  ███    ███     ███    ███   ███    ███     ███    ███         ▄█    ███   ███    ███ ███    ███   ███    ███   ███    ███     ███     
  ███    █▀      ██████████   ███    █▀      ██████████       ▄████████▀    ██████████ ████████▀    ███    ███   ██████████    ▄████▀   
                                                                                                    ███    ███                          
"""
#******************Devide!**************
def encrypt():
    text = str(input("Let's make some secrets! Just type out what you want to make secret! "))
    shift = int(input("enter passcode! "))
    u = []
    for x in text:
        i = letters.index(x)
        u.append(letters[(i + shift) % len(letters)])  # Updated to 47 since the length of letters is now 47
    final = ""
    for j in u:
        final = final + j
    print(final)
#******************Devide and Rule!!!**************
def decrypt():
    text_d = str(input("Give me the secret word!"))
    shift_d = int(input("enter passcode!"))
    v = []
    for y in text_d:
        i = letters.index(y)
        v.append(letters[(i - shift_d) % len(letters)])  # Updated to 47 since the length of letters is now 47
    final_d = ""
    for k in v:
        final_d = final_d + k
    print(final_d)
#******************Devide and Rule!!!**************
print(wc)
over = False
while over != True:
   choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
   if choice == "encode":
       encrypt()
       further = input("Type 'yes' if you want to go again. Otherwise type 'no'")
       if further == "yes":
           over = False
       elif further == "no":
           print("Goodbye~")
           over = True
       else:
           over = True
   elif choice == "decode":
       decrypt()
       further = input("Type 'yes' if you want to go again. Otherwise type 'no'")
       if further == "yes":
           over = False
       elif further == "no":
           print("Goodbye~")
           over = True
       else:
           over = True
   else:
       print("invalid command!")