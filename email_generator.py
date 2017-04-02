#Problem Definition:
#Kind of email generator
#(1)Make the content user input in a email format.
#(2)Translate csv to JSON
#(3)Ask users do we need to send email for them(Use SMTP server to send gmail)
#My purpose is that to generate content in a email formate by choose your choice, because many international students don't know the format of email.
#And then, it also can translate cvs file to JSON
#In the last, we can help user to sent email by using SMTP server

#Input description:
#Input can be a file, string and list of string

#Output description:
#In the first part(Make the content user input in a email format), the output is a file, and also you can copy it.(Because I print the output)
#In the second part(translate csv file to JSON), the output is a JSON
#In the third part(Ask user to send email or not), output is a email.
import os
import csv
import json
import smtplib
def email_generator():
    name = input("Enter your name: ")
    #input can be a file,string and list of string type
    #(1)Make the content user input in a email format
    content = input("Hello " + name + ", enter the type of your content (Type 1 for file, 2 for string, 3 for list of strings): ")
    if(content == '1'): #if the input is a file type
        content2 = input('Enter your file name: ')
        content4 = input('Please enter the last name of professor: ')
        filename = content2 + '.txt'
        op = open(filename,'r')
        str_head = 'Dear Professor ' + content4 + ': '
        str_file1 = op.read()
        op_file = open('res.txt','w')
        op_file.write(str_head + '\n' + '  ' + str_file1 + '\n' + 'Best,' + '\n' + name)
        op_file.close()
        op_file = open('res.txt','r')
        file_contents = op_file.read()
        print(file_contents)#The output is a file, the content is also saved in the file that you can find it in your documents
        op_file.close()
        trans_cvs_json = input('\n' + name + ', ' "do you need translate cvs file to JSON? (Type 1 for Yes, 2 for No): ")#(2)Ask users about translating csv file to JSON
        if(trans_cvs_json == '1'):#Translate csv file to JSON
            csvfile = open('example.csv', 'r')
            jsonfile = open('example.json', 'w')
            fieldnames = ("Date","Time","Fruits","Number")
            reader = csv.DictReader( csvfile, fieldnames)
            for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write('\n')
            print("JSON SAVED!")
            #(3)Ask user to send email or not
            send_email = input("Do you need me to send meail for you? (Type 1 for Yes, 2 for No): ")
            if(send_email == '1'): #Send email
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("Timiii0109@gmail.com","77wasabl")
                msg = file_contents
                server.sendmail("Timiii0109@gmail.com", "Timiii0109@gmail.com", msg)
                server.quit()
                print("EMAIL SENT and GOOD LUCK!")
            if(send_email == '2'):#Don't send email
                print("GOOD LUCK!")
        if(trans_cvs_json == '2'):#Don't translate csv file to JSON
            send_email = input("Do you need me to send meail for me? (Type 1 for Yes, 2 for No): ")
            if(send_email == '1'):#Send email
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("Timiii0109@gmail.com","77wasabl")
                msg = file_contents
                server.sendmail("Timiii0109@gmail.com", "Timiii0109@gmail.com", msg)
                server.quit()
                print("EMAIL SENT and GOOD LUCK!")
            if(send_email == '2'):#Don't send email
                print("GOOD LUCK!")
    if(content == '2'):#if the input is a string type
        con_str = input("Enter your content: ")
        con_str2 = input("Enter your professor's last name: ")
        f = open('res.txt','w')
        str_title = 'Dear Professor ' + con_str2 + ':'
        f.write(str_title + '\n' + '    ' + con_str+ '\n' + 'Best,' + '\n' + name)
        f.close()
        f = open('res.txt','r')
        file_c = f.read()
        print(file_c)
        #The output is a file, the content is also saved in the file that you can find it in your documents
        f.close()
        #(2)Ask users about translating csv file to JSON
        trans_cvs_json = input('\n' + name + ", " "do you need translate cvs file to JSON? (Type 1 for Yes, 2 for No): ")
        if(trans_cvs_json == '1'):#Translate cvs file to JSON
            csvfile = open('example.csv', 'r')
            jsonfile = open('example.json', 'w')
            fieldnames = ("Date","Time","Fruits","Number")
            reader = csv.DictReader( csvfile, fieldnames)
            for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write('\n')
            print("JSON SAVED!")
            #(3)Ask user to send email or not
            send_email = input("Do you need me to send meail for you? (Type 1 for Yes, 2 for No): ")
            if(send_email == '1'): #Send email
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("Timiii0109@gmail.com","77wasabl")
                msg = file_c
                server.sendmail("Timiii0109@gmail.com", "Timiii0109@gmail.com", msg)
                server.quit()
                print("EMAIL SENT and GOOD LUCK!")
            if(send_email == '2'):#Don't send email
                print("GOOD LUCK!")
        if(trans_cvs_json == '2'):#Don't translate csv file to JSON
            send_email = input("Do you need me to send meail for me? (Type 1 for Yes, 2 for No): ")
            if(send_email == '1'):#Send email
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("Timiii0109@gmail.com","77wasabl")
                msg = file_c
                server.sendmail("Timiii0109@gmail.com", "Timiii0109@gmail.com", msg)
                server.quit()
                print("EMAIL SENT and GOOD LUCK!")
            if(send_email == '2'):#Don't send email
                print("GOOD LUCK!")
            
    if(content == '3'):#if the input is a list of string type
        ls_str = input("Enter your content: ")
        content3_str = str(ls_str).strip('[]')
        last_prof = input("Enter your professor's last name: ")
        file = open('res.txt','w')
        title = 'Dear Professor ' + last_prof + ':'
        file.write(title + '\n' + '    ' + content3_str + '\n' + 'Best,' + '\n' + name)
        file.close()
        file = open('res.txt','r')
        print_con = file.read()
        print(print_con)
        #The output is a file, can the content is also saved in the file that you can find it in your documents
        file.close()
        #Ask users about translating csv file to JSON
        trans_cvs_json = input('\n' + name + ", " "do you need translate cvs file to JSON? (Type 1 for Yes, 2 for No): ")
        if(trans_cvs_json == '1'):#Translate csv file to JSON
            csvfile = open('example.csv', 'r')
            jsonfile = open('example.json', 'w')
            fieldnames = ("Date","Time","Fruits","Number")
            reader = csv.DictReader( csvfile, fieldnames)
            for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write('\n')
            print("JSON SAVED!")
            #(3)Ask user to send email or not
            send_email = input("Do you need me to send meail for you? (Type 1 for Yes, 2 for No): ")
            if(send_email == '1'): #Send email
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("Timiii0109@gmail.com","77wasabl")
                msg = print_con
                server.sendmail("Timiii0109@gmail.com", "Timiii0109@gmail.com", msg)
                server.quit()
                print("EMAIL SENT and GOOD LUCK!")
            if(send_email == '2'):#Don't send email
                print("GOOD LUCK!")
        if(trans_cvs_json == '2'):#Don't translate csv file to JSON
            send_email = input("Do you need me to send meail for me? (Type 1 for Yes, 2 for No): ")
            if(send_email == '1'):#Send email
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login("Timiii0109@gmail.com","77wasabl")
                msg = print_con
                server.sendmail("Timiii0109@gmail.com", "Timiii0109@gmail.com", msg)
                server.quit()
                print("EMAIL SENT and GOOD LUCK!")
            if(send_email == '2'):#Don't send email
                print("GOOD LUCK!")
                
#Summary Description:
#My final project can obtain the data wich are strng, list of strng and file. It hard to combine three part together.
#And I choose the easy way for me to do it, which is using many if conditions.
#The results of data can be a file if user choose to no email, no translating.
#The results of data also can be a file, JSON and email if user choose to send email, translate file.


