import os
import generate
import decode

# This program generates a QR code using the inputs from the command line.
while True:

    print('⚡  Welcome to QR Generator! \n Select an option:')

    print('➡️  Enter \'1\' to create a new QR Code.')
    print('➡️  Enter \'2\' to decode a QR Code from an image file.')
    user_option = input ('Enter option: ').strip()
    if user_option == 'q':
        break

    if user_option == '1':
        print('Create a new QR Code!')
        user_input_formatted = ''
        user_input = input('⌨️  Enter data to store inside your new QR Code: ')
        for character in user_input:
            if character.isalnum():
                user_input_formatted += character
        print(user_input_formatted)

        # Set path variable
        program_path = ('python-enviroments/qr-code-generator/')
        
        # Make new directory if one is not found.
        try:
            if not os.path.exists(program_path):
                os.makedirs(program_path)
                print('Program created new directory!' + program_path)            
        except:
            print('Error creating directory ' + program_path + 'Does the program have the proper permssions to create new direcotries on this system?')
        
        # Function call to create QR
        generate.create_qr(program_path, user_input_formatted, user_input)
        print('🎉')
    
    if user_option == '2':

        print('Decode a QR Code.')
        # // TODO Implement the decode function
        
        image_file = input('Enter the location of the QR Code: ')
        
        # Fucntion call to decode a qr code
        decode.decode_qr(image_file)
