from flask import *
from controls.user import user
import pickle

app = Flask(__name__)
app.secret_key = 'samyak_fulzele'

userObj = user()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        u_name = request.form['username']
        u_email = request.form['email']
        conf_pass = request.form['password']
        u_pass = request.form['confirm-password']
        if conf_pass == u_pass:
            registerStatus = userObj.register(u_name,u_email,u_pass)
            if registerStatus == 1:
                register_success = True
                return render_template("index.html",register_success=register_success)
            else:
                register_fail = True
                return render_template("index.html",register_fail=register_fail)
        else:
            password_fail = True
            return render_template("index.html",password_fail=password_fail)
    else:
        return redirect(url_for('home'))

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        u_name = request.form['uname_email']
        u_pass = request.form['password']
        loginStatus = userObj.login(u_name,u_pass)
        if loginStatus == 1:
            return redirect(url_for('user_dashboard'))
        else:
            login_fail = True
            return render_template("index.html",login_fail=login_fail)
    else:
        return redirect(url_for('home'))
    
@app.route('/contact',methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        c_name = request.form['c_name']
        c_email = request.form['c_email']
        c_message = request.form['c_message']
        contactStatus = userObj.contact(c_name,c_email,c_message)
        if contactStatus == 1:
            contact_success = True
            return render_template("index.html",contact_success=contact_success)
        else:
            contact_fail = True
            return render_template("index.html",contact_fail=contact_fail)
    else:
        return redirect(url_for('home'))
    
@app.route('/user_dashboard',methods=['POST','GET'])
def user_dashboard():
    if session.get('u_loggedIn') == True:
        return render_template("user_dashboard.html",data=userObj.predicted_data())
    else:
        return redirect(url_for('login'))

@app.route('/model_predict',methods=['POST','GET'])
def model_predict():
    if session.get('u_loggedIn') == True:
        if request.method == 'POST':
            input1 = request.form['input1']
            input2 = request.form['input2']
            input3 = request.form['input3']
            model = pickle.load(open('svm_pickle_model','rb'))
            output = model.predict([[input1,input2,input3]])
            predictStatus = userObj.model_predict(input1,input2,input3,str(output[0]))
            if predictStatus == 1:
                if output[0] == 0:
                    flash("0 - Confusion Score is Low!")
                elif output[0] == 1:
                    flash("1 - Confusion Score is Medium!")
                else:
                    flash("2 - Confusion Score is High!")
                return redirect(url_for('user_dashboard'))
        return redirect(url_for('user_dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('u_loggedIn',None)
    session.pop('u_id',None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True) 