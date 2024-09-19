from flask import *
import mysql.connector
import os
import pickle

class user():
    _db = mysql.connector.connect(host="localhost",user="root",password="",database="eeg_project")
    _curr = _db.cursor()
    def register(self,u_name,u_email,u_password):
        query = "INSERT INTO users(u_name,u_email,u_password) VALUES('"+u_name+"','"+u_email+"','"+u_password+"')"
        self._curr.execute(query)
        if self._db.commit() == False:
            return(0)
        else:
            return(1)
        
    def login(self,u_name,u_password):
        query = "SELECT u_id,u_name,u_email,u_password FROM users WHERE (u_name = '"+u_name+"' or u_email = '"+u_name+"') and u_password = '"+u_password+"';"
        self._curr.execute(query)
        data = self._curr.fetchone()
        print(data)
        if data:
            session['u_loggedIn'] = True          
            session['u_id'] = data[0]            
            return(1)
        else:
            return(0)
        
    def model_predict(self,input1,input2,input3,output):
        query = "INSERT INTO records(u_id,r_input1,r_input2,r_input3,r_ouput,r_dateCreated) VALUES('"+str(session['u_id'])+"','"+input1+"','"+input2+"','"+input3+"','"+output+"',NOW())"
        self._curr.execute(query)
        if self._db.commit() == False:
            return(0)
        else:
            return(1)
        
    def predicted_data(self):
        query = "SELECT * FROM records WHERE u_id = '"+str(session['u_id'])+"'"
        self._curr.execute(query)
        data = self._curr.fetchall()
        return data
    
    def contact(self,c_name,c_email,c_message):
        query = "INSERT INTO contact(c_name,c_email,c_msg,c_date_time) VALUES('"+c_name+"','"+c_email+"','"+c_message+"',NOW())"
        self._curr.execute(query)
        if self._db.commit() == False:
            return(0)
        else:
            return(1)