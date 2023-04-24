def crc(message, generator, crc_code='0000'): 
    if int(crc_code) == 0 :              
        crc_code = ''
        for i in range(len(generator) -1):
            crc_code = crc_code + '0'

    message = message + crc_code
    message = list(message)
    generator = list(generator)

    for i in range(len(message) - len(crc_code)):
        if message[i] == '1': # si el bit es un uno (1)
            for j in range(len(generator)):
                message[i+j] = str((int(message[i+j])+int(generator[j]))%2)       
                return ''.join(message[-len(crc_code):]) 
