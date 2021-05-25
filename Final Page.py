# IMPORTS

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
    

# FLASK
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Other Imports 
import os
import shutil

# Web Pages

# Home
@app.route("/")
def home():
    # LOGIN/SIGN UP
    #return render_template('Login.html')
    return ("<a href='/PL'>Login</a> / <a href='/PS'>Sign Up</a>")

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


@app.route("/signup")#, methods=['POST'])
def home_Signup():
    return "Signup"
    return render_template('signup.html')
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
   global filename
   if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      f.save(secure_filename(filename))
      
      os.rename(filename, "test.mp3")
      
      exec(open("./update.py").read())
      exec(open("./camrec.py").read())
      
      try: 
          shutil.rmtree("temp")
          os.remove("temp.mp4") 
          print("\nTemp files deleted.\n")
      except:
          pass
      
      endname = filename[:filename.rfind(".")]+".mp4"
      os.rename("my_videof.mp4", endname)
      
      return redirect(url_for('uploads_file',path = endname))

@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    UPLOAD_DIRECTORY = ''
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@app.route("/<user>/upload/convert")
def convert(user):
    return "convert"

    

# MAIN
if __name__ == "__main__":
    use = ''
    filename = ''
    app.run()
else:
    use = ''
    filename = ''
    app.run()
    