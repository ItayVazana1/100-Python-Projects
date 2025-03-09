# Day 8 - Caesar Cipher Generator


gui_title = """
        CCCCCCCCCCCCC                                                                                                                                          
     CCC::::::::::::C                                                                                                                                          
   CC:::::::::::::::C                                                                                                                                          
  C:::::CCCCCCCC::::C                                                                                                                                          
 C:::::C       CCCCCC  aaaaaaaaaaaaa       eeeeeeeeeeee        ssssssssss     aaaaaaaaaaaaa   rrrrr   rrrrrrrrr                                                 
C:::::C                a::::::::::::a    ee::::::::::::ee    ss::::::::::s    a::::::::::::a  r::::rrr:::::::::r                                               
C:::::C                aaaaaaaaa:::::a  e::::::eeeee:::::eess:::::::::::::s   aaaaaaaaa:::::a r:::::::::::::::::r                                              
C:::::C                         a::::a e::::::e     e:::::es::::::ssss:::::s           a::::a rr::::::rrrrr::::::r                                             
C:::::C                  aaaaaaa:::::a e:::::::eeeee::::::e s:::::s  ssssss     aaaaaaa:::::a  r:::::r     r:::::r                                             
C:::::C                aa::::::::::::a e:::::::::::::::::e    s::::::s        aa::::::::::::a  r:::::r     rrrrrrr                                             
C:::::C               a::::aaaa::::::a e::::::eeeeeeeeeee        s::::::s    a::::aaaa::::::a  r:::::r                                                          
 C:::::C       CCCCCCa::::a    a:::::a e:::::::e           ssssss   s:::::s a::::a    a:::::a  r:::::r                                                          
  C:::::CCCCCCCC::::Ca::::a    a:::::a e::::::::e          s:::::ssss::::::sa::::a    a:::::a  r:::::r                                                          
   CC:::::::::::::::Ca:::::aaaa::::::a  e::::::::eeeeeeee  s::::::::::::::s a:::::aaaa::::::a  r:::::r                                                          
     CCC::::::::::::C a::::::::::aa:::a  ee:::::::::::::e   s:::::::::::ss   a::::::::::aa:::a r:::::r                                                          
        CCCCCCCCCCCCC  aaaaaaaaaa  aaaa    eeeeeeeeeeeeee    sssssssssss      aaaaaaaaaa  aaaa rrrrrrr                                                          
                                                          CCCCCCCCCCCCC  iiii                      hhhhhhh                                                     
                                                       CCC::::::::::::C i::::i                     h:::::h                                                     
                                                     CC:::::::::::::::C  iiii                      h:::::h                                                     
                                                    C:::::CCCCCCCC::::C                            h:::::h                                                     
                                                   C:::::C       CCCCCCiiiiiii ppppp   ppppppppp    h::::h hhhhh           eeeeeeeeeeee    rrrrr   rrrrrrrrr   
                                                  C:::::C              i:::::i p::::ppp:::::::::p   h::::hh:::::hhh      ee::::::::::::ee  r::::rrr:::::::::r  
                                                  C:::::C               i::::i p:::::::::::::::::p  h::::::::::::::hh   e::::::eeeee:::::eer:::::::::::::::::r 
                                                  C:::::C               i::::i pp::::::ppppp::::::p h:::::::hhh::::::h e::::::e     e:::::err::::::rrrrr::::::r
                                                  C:::::C               i::::i  p:::::p     p:::::p h::::::h   h::::::he:::::::eeeee::::::e r:::::r     r:::::r
                                                  C:::::C               i::::i  p:::::p     p:::::p h:::::h     h:::::he:::::::::::::::::e  r:::::r     rrrrrrr
                                                  C:::::C               i::::i  p:::::p     p:::::p h:::::h     h:::::he::::::eeeeeeeeeee   r:::::r            
                                                   C:::::C       CCCCCC i::::i  p:::::p    p::::::p h:::::h     h:::::he:::::::e            r:::::r            
                                                    C:::::CCCCCCCC::::Ci::::::i p:::::ppppp:::::::p h:::::h     h:::::he:::::::e           r:::::r            
                                                     CC:::::::::::::::Ci::::::i p::::::::::::::::p  h:::::h     h:::::h e::::::::eeeeeeee   r:::::r            
                                                       CCC::::::::::::Ci::::::i p::::::::::::::pp   h:::::h     h:::::h  ee:::::::::::::e   r:::::r            
                                                          CCCCCCCCCCCCCiiiiiiii p::::::pppppppp     hhhhhhh     hhhhhhh    eeeeeeeeeeeeee   rrrrrrr            
                                                                                p:::::p                                                                        
                                                                                p:::::p                                                                        
                                                                               p:::::::p                                                                       
                                                                               p:::::::p                                                                       
                                                                               p:::::::p                                                                       
                                                                               ppppppppp                                                                       
"""

def encode(msg, shift_num):
    encrypted_msg = ""
    symbols_and_space = " ?!@#$%^&*()"
    low_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerical_alphabet = "0123456789"
    for letter in msg:
        if letter in low_alphabet:
            char_bank = low_alphabet
        elif letter in cap_alphabet:
            char_bank = cap_alphabet
        elif letter in numerical_alphabet:
            char_bank = numerical_alphabet
        else:
            char_bank = symbols_and_space
        for i in range(len(char_bank)):
            if letter == char_bank[i]:
                c = i + shift_num
                while c >= len(char_bank):
                    c -= len(char_bank)
                encrypted_msg += char_bank[c]
                break

    print(f"The encoded result (between the []) : [{encrypted_msg}] ")


def decode(msg, shift_num):
    is_cap = False
    original_msg = ""
    symbols_and_space = " ?!@#$%^&*()"
    low_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cap_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numerical_alphabet = "0123456789"
    for letter in msg:
        if letter in low_alphabet:
            char_bank = low_alphabet
        elif letter in cap_alphabet:
            char_bank = cap_alphabet
        elif letter in numerical_alphabet:
            char_bank = numerical_alphabet
        else:
            char_bank = symbols_and_space
        for i in range(len(char_bank)):
            if letter == char_bank[i]:
                c = i - shift_num
                while c < 0:
                    c += len(char_bank)
                original_msg += char_bank[c]
                break

    print(f"The decoded result : {original_msg}")


p_flag = True

print(gui_title)
while p_flag:
    operation = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    while True:
        if operation == "encode" or operation == "decode":
            break
        else:
            print("Invalid input - try again!")
            operation = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    massage = input("Type your massage:\n")
    shift_number = int(input("Type the shift number:\n"))

    if operation == "encode":
        encode(msg=massage, shift_num=shift_number)
    else:
        decode(msg=massage, shift_num=shift_number)

    more_op = input("To continue , type 'yes' , otherwise type somthing else..").lower()
    if more_op != 'yes':
        p_flag = False

