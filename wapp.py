# IMPORTS

##############################################################################
# Users Initialisations
import pickle ## Data Handle

"""
LOGIN = {"Admin":"Admin"}

with open("Users.ec",'wb') as f:
    pickle.dump(LOGIN, f)
"""

with open("Users.ec",'rb') as f:
    LOGIN = pickle.load(f)

USERS = list(LOGIN.keys())

##############################################################################

# FLASK
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import webbrowser

# Other Imports 
import os
import shutil

# app initialise
app = Flask(__name__)

# Web Pages

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# Home
@app.route("/")
def home():
    # LOGIN/SIGN UP
    return render_template('junc.html')
    #return ("<a href='/PL'>Login</a> / <a href='/PS'>Sign Up</a>")

@app.route("/PL")
def PL():
    return render_template('Login.html')#,string_variable="") 
@app.route("/PS")
def PS():
    return render_template('signup.html') 

@app.route('/login', methods=['POST'])
def home_Login():
    
    global use 
    
    PU = str(request.form['username'])
    PP = str(request.form['password'])
    print("ello")
    
    try:
        if PU in USERS:
            if PP == LOGIN[PU]:
                use = PU
                try:
                    os.mkdir(use)
                except:
                    pass
                return redirect(url_for('uploads_file'))#,user = PU))
            else:
                return redirect(url_for('invalid_user'))#,string_variable="Invalid Username or Password")
        else:
            return redirect(url_for('invalid_user'))#,string_variable="Invalid Username or Password")'''
    except:
        return redirect(url_for('invalid_user'))

@app.route("/invalid_user")#, methods=['POST'])
def invalid_user():
    return "Invalid User name or Password\n<a href='/PL'>Press here to Login again</a> <a href='/PS'>else Sign Up here</a>  "


@app.route("/signup", methods=['POST'])
def home_Signup():
    
    PU = str(request.form['username'])
    PP = str(request.form['password'])
    print("ello")

    if PU in USERS:
        return "Username already taken.<a href='/PS'>Press here</a> to try again"
    else:
        LOGIN[PU] = PP
        with open("Users.ec",'wb') as f:
            pickle.dump(LOGIN, f)
        return "Account created.<a href='/PL'>Press here</a> to Login"

'''
@app.route("/<user>/upload/")
def upload(user):
    return "upload"
'''
@app.route('/upload')
def uploads_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   global filename,fn
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      f.save(secure_filename(filename))
      '''
      try:
          os.remove("test.mp3")
      except Exception as e:
            print("\nerror occured : ",e,"\n")
      '''
      filename = filename.replace(" ","_")
      fn = filename
      os.rename(filename, "test.mp3")
      
      return redirect(url_for('shutdown'))

@app.route("/<user>/upload/convert")
def convert(user):
    return "convert"
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    global k,fn, use
    filename = "/"+fn[:fn.rfind(".")]+".mp4"
    
    if k and filename not in os.listdir(use):
        shutdown_server()
        return 'Please wait while video is being processed'
    else:
        
        endname = use+"/"+fn[:fn.rfind(".")]+".mp4"
        print("lol",filename)
        
        if filename not in os.listdir(use):
            #return redirect(url_for('get_file',path = 'my_videof.mp4'))
            
            try: 
                shutil.rmtree("temp")
                #os.remove("temp.mp4") 
                print("\nTemp files deleted.\n")
            except Exception as e:
                print("\nerror occured : ",e,"\n")
            """
            try:
                os.mkdir(use)
            except:
                pass
            """
            #filename = fn
            #endname = use+"/"+filename[:filename.rfind(".")]+".mp4"
            
            #endname = use+"/"+fn[:fn.rfind(".")]+".mp4"
            try:
                os.rename("my_videof.mp4", endname)
            except:
                pass
              
            return redirect(url_for('get_file',path = endname))
        else:
            return redirect(url_for('get_file',path = endname))
                
            #return redirect(url_for('get_file',path = 'my_videof.mp4'))

@app.route("/myfiles")
def myfiles():
    global use
    s = ''
    for i in os.listdir(use):
        s+="<a href='/myfiles/select/"+i+"'"+">"+i+'</a><br>'
        #s+=i+"<br>"
    s+="<a href='/upload'>back</a>"
    return s

@app.route("/myfiles/select/<var>")
def myfiles_select(var):
    global fn
    
    fn = var
    return redirect(url_for('shutdown'))

if __name__ == '__main__':
    try:
        os.remove("test.mp3")
    except:
        pass
    
    k = True
    filename = ''
    fn= ""
    app.run()

print("hello")
try:
    exec(open("./update.py").read())
    exec(open("./camrec.py").read())
except Exception as e:
    print("\nerror occured : ",e,"\n")
    
@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    UPLOAD_DIRECTORY = ''
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

if __name__ == '__main__':
    k = False
    webbrowser.open_new_tab('http://localhost:5000/shutdown')
    app.run()