import time
from time import time
import os
import save


def create_qr(program_path, user_input_formatted, user_input):
    '''Create a QR code from the users inputed data and then store it in the program path'''
    # Check if a file with name already exsists. If True ask user if they want to overwrite it. 
    # TODO Format filename to allow for URLs.
    # saved_qr_path = user_input_formatted + '.png'
    
    if os.path.exists(program_path + user_input_formatted + '.png'):
        print('⚠️  File with name: ' + '\"'+ user_input_formatted +'\"' + ' exsists already')
        overwrite_file = input('Do you want to overwrite this file? (Y/N): ').strip().lower()
        
        if overwrite_file == 'y' or 'yes':
                save.save_file(program_path, user_input_formatted, user_input)
                print(user_input_formatted + ' was overwritten.')
        
        else: 
            if overwrite_file == 'n' or 'no':
                pass
    else:
        if not os.path.exists(program_path + user_input_formatted + '.png'):
            save.save_file(program_path, user_input_formatted, user_input)     
                
    
        
