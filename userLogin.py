# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:45:26 2021

@author: mjvat
"""

import system_catalog_users

class UserLogin():
    
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        
    def system():
        
        system = system_catalog_users()
        return system
        
    def validateUser(self, username, password):
        
        if username == system.correct_username:
            if password == system.correct_password:
                return session_login.loginSuccessful()
            
        return session_login.loginFailed()
    
    def loginSuccessful():
        
        return session_login.authentication_successful
    
    def loginFailed(): 
        
        return session_login.authentication_failed
    
if __name__ == '__main__':
    
    session_login = UserLogin()
    session_login.username = input('Username: ')
    session_login.password = input('Password: ')
    
    system = system_catalog_users()
    session_login.validateUser(session_login.username, session_login.password)
    
    
    