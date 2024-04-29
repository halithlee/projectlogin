from flask import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__)
mark_list=[]
Student_list = [{"Name":"Ruban","Age":21 ,"Roll_NO": 101, "Marks":[90,75,80,98,75]},
             {"Name":"Kiruba","Age":24 ,"Roll_NO": 102, "Marks":[90,75,80,98,65]},
             {"Name":"Halith","Age":23 ,"Roll_NO": 103, "Marks":[90,75,80,78,99]},
             {"Name":"Thenmozhi","Age":24 ,"Roll_NO": 104, "Marks":[94,75,80,88,35]},
             {"Name":"Deva","Age":22 ,"Roll_NO": 105, "Marks":[70,85,80,98,35]},          
             {"Name":"Eeswar","Age":25 ,"Roll_NO": 106, "Marks":[90,75,85,98,35]},
             {"Name":"Mani","Age":23 ,"Roll_NO": 107, "Marks":[80,98,35,90,75]}]

user_name="Mohammed Halith"
password="halithlee1546"

def isloggedin():
    return user_name in session

app.secret_key="abc123"

@app.route('/',methods=['GET','POST'])

def login():
    if request.method=="POST":
        Name = request.form['name']
        Password = request.form['password']
        
        if Name == user_name and Password == password:
            session['user_name'] = Name
            return redirect(url_for('home'))
        else:
            return"Authentication Failed"
    return render_template('user.html')

@app.route('/logout/')
def logout():
    session.pop('user_name',None)
    return redirect(url_for('login'))


@app.route("/home")
def home():
    return render_template("index.html",data=Student_list)

    
@app.route("/add",methods=["GET","POST"])
def add():
    if request.method=="POST":
        stu_dict={}
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        Roll_NO=request.form.get("Roll_NO")
        mark_list.append(request.form.get("sub1"))
        mark_list.append(request.form.get("sub2"))
        mark_list.append(request.form.get("sub3"))
        mark_list.append(request.form.get("sub4"))
        mark_list.append(request.form.get("sub5"))
        
        stu_dict.update({"Name":Name})
        stu_dict.update({"Age":Age})
        stu_dict.update({"Roll_NO":Roll_NO})
        stu_dict.update({"Marks":mark_list})
        Student_list.append(stu_dict)
        return redirect(url_for("home"))
    return render_template('add.html',data=Student_list)

@app.route('/edit/<string:id>',methods=['GET','POST'])
def edit(id):
    if request.method=='POST':
        
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        Roll_NO=request.form.get("Roll_NO")
        tam=request.form.get('sub1')
        eng=request.form.get('sub2')
        math=request.form.get('sub3')
        sci=request.form.get('sub4')
        soc=request.form.get('sub5')
        
        mark_list=[tam,eng,math,sci,soc]
        edit_dict=Student_list[int(id)-1]
        
        edit_dict["Name"]=Name
        edit_dict["Age"]=Age
        edit_dict["Roll_NO"]=Roll_NO
        edit_dict["Marks"]=mark_list
        
        return redirect(url_for('home'))
    
    edit_list=Student_list[int(id)-1]
    return render_template('edit.html',from_data=edit_list)

@app.route('/delete/<string:id>',methods=['GET','POST'])
def delete(id):

    Student_list.pop(int(id)-1)
    
    return redirect(url_for('home'))


if __name__=="__main__":
    app.run(debug=True)
    

