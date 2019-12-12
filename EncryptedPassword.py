class EncryptedPassword():
    """Class that can be used to either provide a password/username to be encrypted 
    OR to load a previously encypted password from file. Repo with source: https://github.com/jirvingphd/gridsearch_with_keras_models_custom_scorer   
    NOTE: Once you have encrypted your password and saved to bin files, you do not need to provide the password again. 
    Make sure to delete your password from the notebook after. 
    - If encrypting a password, a key file and a password file will be saved to disk. 
        - Default Key Filename: '..\\encryption_key.bin',
        - Default Password Filename: '..\\encrypted_pwd.bin'
        - Default Username Filename: '..\\encrypted_username.bin'
    
    The string representations of the unencrypted password are shielded from displaying, when possible. 
    


    - If opening and decrypting key and password files, pass filenames during initialization. 
    
    
    Example Usage:
    >> # To Encrypt, with default folders:
    >> my_pwd EncryptedPassword('my_password')
    
    >> # To Encrypt With custom folders
    >> my_pwd = EncryptedPassword('my_password',filename_for_key='..\folder_outside_repo\key.bin',
                                    filename_for_password = '..\folder_outside_repo\key.bin')
                                    
                                    
    >> # To open and decrypt files (from default folders):
    >> my_pwd = EncryptedPassword(from_file=True)
    
    >> # To open and decrypt files (from custom folders):
    >> my_pwd = EncryptedPassword(from_file=True, 
                                filename_for_key='..\folder_outside_repo\key.bin',
                                filename_for_password = '..\folder_outside_repo\key.bin')
                                    
        
    """
    
    ## Default username
    username = 'NOT PROVIDED'
    
    ## the .password property is designed so it will not display an unencrypted password. 
    @property ## password getter 
    def password(self):
        # if the encrypyted password already exists, print the encrypted pwd (unusable without key)
        if hasattr(self,'_encrypted_password_'):
            print('Encrypted Password:')
            return self._encrypted_password_
        else:
            raise Exception('Password not yet encrypted.')
    
    ## the .password property cannot be set by a user
    @password.setter ## password setter
    def password(self,password):
        raise Exception('.password is read only.')
        
               
    ## 
    def __init__(self,username=None,password=None,from_file=False, encrypt=True,
                filename_for_key='..\\encryption_key.bin',
                filename_for_password='..\\encrypted_pwd.bin',
                filename_for_username = '..\\encrypted_username.bin'):
        """Accepts either a username and password to encyrypt, 
        or loads a previously encrypyed password from file.
        
        Args:
            username (str): email username.
            password (str): email password (note: if have 2-factor authentication on email account, 
                will need app-specific password).
            from_file (bool): whether to load the user credentials from file
            encrypt (bool): whether to encrypt provided password. Default=True
            
            filename_for_key (str): filepath for key.bin (default is'..\\encryption_key.bin')
            filename_for_password: filepath for password.bin (default is'..\\encryption_pwd.bin')
            filename_for_username: filepath for username.bin (default is'..\\encrypted_username.bin')
            """
        
        ## Save filenames 
        self.filename_for_key = filename_for_key
        self.filename_for_password = filename_for_password
        self.filename_for_username = filename_for_username
        
        ## If user passed a username, set username
        if username is not None:
            self.username = username
        
        ## If no password is provided:
        if (password is None):
            
            ##  if load from file if `from_file`=True
            if (from_file==True):
                
                try: ## Load in the key, password, username files
                    self.load_from_file(key_filename=filename_for_key,
                                    password_filename=filename_for_password,
                                        username_filename=filename_for_username)
                except:
                    raise Exception('Something went wrong. Do the key and password files exist?')
            
            ## If no password provided, and from_file=False, raise error
            else:
                raise Exception('Must either provide a password to encrypt, or set from_file=True')
        
        
        ## If the user DOES provide a password
        else:
            self._password_ = password # set the private attribute for password
            
            ## Encrypt the password
            if encrypt:
                self.encrypt_password()
                
                
    def encrypt_password(self, show_encrypted_password=False):
        """Encrypt the key, username, and password and save to external files."""
         ## Get filenames to use.
        filename_for_key= self.filename_for_key
        filename_for_password=self.filename_for_password
        filename_for_username = self.filename_for_username

        ## Import cryptography and generate encryption key
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        self._key_ = key

        ## Create the cipher_suit from key for encrypting/decrypting
        cipher_suite = Fernet(key)
        self._cipher_suite_ = cipher_suite
 
        ## ENCRYPT PASSWORD
        # Get password and change to byte encoding
        password = self._password_
        password_to_encrypt = bytes(password,'utf-8') #password must be in bytes format
        
        # Use the encryption suite to encrypt the password and save to self
        ciphered_pwd = cipher_suite.encrypt(password_to_encrypt)
        self._encrypted_password_ = bytes(ciphered_pwd).decode('utf-8')
        
        # Print encrypyted password if true
        if show_encrypted_password:
            print('Encrypyted Password:')
            print(self._encrypted_password_)
        
        
        ## ENCRYPT USERNAME
        username = self.username
        username_to_encrypt = bytes(username,'utf-8')
        ciphered_username = cipher_suite.encrypt(username_to_encrypt)
        self._encrypted_username_ = bytes(ciphered_username).decode('utf-8')
        
        ## TEST DECRYPTION
        # decrypt password and username
        unciphered_pwd = cipher_suite.decrypt(ciphered_pwd)
        unciphered_username = cipher_suite.decrypt(ciphered_username)
        
        ## Decode from bytes to utf-8
        password_decoded = unciphered_pwd.decode('utf-8')
        username_decoded = unciphered_username.decode('utf-8')
        
        # Check if decoded text matches input text
        check_pwd = password_decoded==password
        check_user = username_decoded==username
        
        ## If everything matches, warn user to delete their exposed password
        if  check_pwd & check_user:
            self._password_ = password_decoded 
            print('[!] Make sure to delete typed password above from class instantiation.')
        else:
            raise Exception('Decrypted password and input password/username do not match. Something went wrong.')

        ## SAVE KEY, PASSWORD, AND USERNAME TO BIN FILES
        ## Specify binary files (outside of repo) for storing key and password files
        with open(filename_for_key,'wb') as file:
            file.write(key)

        with open(filename_for_password,'wb') as file:
            file.write(ciphered_pwd)
            
        with open(filename_for_username,'wb') as file:
            file.write(ciphered_username)

        # Display filepaths for user.
        print(f'[io] Encryption Key saved as {filename_for_key}')
        print(f'[io] Encrypted Password saved as {filename_for_password}')
        print(f'[io] Encrypted Username saved as {filename_for_username}')

            
    
    def load_from_file(self,key_filename,password_filename,
                      username_filename):
        """Load in the encrypted password from file. """
        
        from cryptography.fernet import Fernet
        
        ## Load Key 
        with open(key_filename,'rb') as file:
            for line in file:
                key = line

        ## Make ciphere suite from key
        cipher_suite = Fernet(key)
        self._cipher_suite_ = cipher_suite

        ## Load password
        with open(password_filename,'rb') as file:
            for line in file:
                encryptedpwd = line
        self._encrypted_password_ = encryptedpwd
        
        ## Decrypt password
        unciphered_text = (cipher_suite.decrypt(encryptedpwd))
        plain_text_encrypted_password = bytes(unciphered_text).decode('utf-8')
        self._password_ = plain_text_encrypted_password
        
        ## Load username
        with open(username_filename,'rb') as file:
            for line in file:
                username = line
        unciphered_username = (cipher_suite.decrypt(username))
        plan_text_username = bytes(unciphered_username).decode('utf-8')
        self.username = plan_text_username
        
    def __repr__(self):
        """Controls the printout when the object is the final command in a cell.
        i.e:
        >> pwd =EncrypytedPassword(username='me',password='secret')
        >> pwd
        """
        password = self._password_
        msg = f'[i] Password is {len(password)} chars long.'
        return msg

    def __str__(self):
        """Controls the printout when the object is printed.
        i.e:
        >> pwd =EncrypytedPassword(username='me',password='secret')
        >> print(pwd)
        """
        password = self._password_
        msg = f'[i] Password is {len(password)} chars long.'
        return msg 
    
    
"""
## Create EncrypyedPassword object (only need to do this step 1 time from any notebook in the repo)
# enc_pwd = EncryptedPassword(username='james.irving.phd@gmail.com',password='')

## note: to be extra safe, i'm loading in the raw password from an external text file
with open('../encrypt_me.txt') as f: raw_text_pwd=f.read() 
    
# I might forget to delete it before sharing this if i typed it lol
enc_pwd = EncryptedPassword(username='james.irving.phd@gmail.com',password=raw_text_pwd)
"""

def email_notification(password_obj=None,subject='GridSearch Finished',msg='The GridSearch is now complete.'):
    """Sends email notification from gmail account using previously encrypyted password  object (an instance
    of EncrypytedPassword). 
    Args:
        password_obj (EncryptedPassword object): EncryptedPassword object with username/password.
        subject (str):Text for subject line.
        msg (str): Text for body of email. 

    Returns:
        Prints `Email sent!` if email successful. 
    """
    ## Display instructions if no password_obj 
    if password_obj is None:
        print('Must pass an EncrypytedPassword object.')
        print('>> pwd_obj = EncryptedPassword(username="my_username",password="my_password")')
        print('>> send_email(encrypted_password_obj=pwd_obj)')
        raise Exception('Must pass an EncryptedPassword.')
    
    # import required packages
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email import encoders
    
    ## Get username and password from password_obj
    gmail_user = password_obj.username
    gmail_password = password_obj._password_
    
    ## WRITE EMAIL
    message = MIMEMultipart()
    message['Subject'] =subject
    message['To'] = gmail_user
    message['From'] = gmail_user
    body = msg
    message.attach(MIMEText(body,'plain'))
    text_message = message.as_string()


    # Send email request
    try:
        with  smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            
            server.login(gmail_user,gmail_password)
            server.sendmail(gmail_user,gmail_user, text_message)
            server.close()
            print('Email sent!')
        
    except Exception as e:
        print(e)
        print('Something went wrong')