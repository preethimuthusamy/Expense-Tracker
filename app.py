from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/regiter", methods=['GET', 'POST'])
def register_user():
    if request.method == 'GET':
        return render_template('regiter.html')
    elif request.method == 'POST':
        data={}
        salary=0
        spend=0
        data['name'] = request.form['name']
        data['username'] = request.form['username']
        data['password'] = request.form['password']
        data['gender'] = request.form['gender']
        data['contact'] = request.form['contact']
        data['email'] = request.form['email']
        salary=int(request.form['salary'])
        spend=spend+int(request.form['clothing'])+int(request.form['eb'])+int(request.form['loan'])+int(request.form['rent'])+int(request.form['food'])
        salary=salary-spend
        return render_template('success.html', record=data,salary=salary)
if __name__ == "__main__":
        app.run(debug=True,port=8899)