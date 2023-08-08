from flask import Flask, render_template, request
import client as client

app = Flask(__name__)

#DEFAULT ROUTE
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')

#Initiate the connection
@app.route("/start_connection", methods=['GET', 'POST'])
def initiate():
    if(request.method=='POST'):
        ip = request.form.get('ip')
        port = request.form.get('port')
        client.set_parameters(ip,port)
        res = client.connect_socket()
        print(res)
        return render_template('mouse.html')
    return render_template('index.html')

#Performing actions
@app.route("/left_click", methods=['GET', 'POST'])
def leftclick():
    if(request.method=='POST'):
        client.perform_operation('left')
        return render_template('mouse.html')
    return render_template('mouse.html')

@app.route("/right_click", methods=['GET', 'POST'])
def rightclick():
    if(request.method=='POST'):
        client.perform_operation('right')
        return render_template('mouse.html')
    return render_template('mouse.html')

@app.route("/left_arrow", methods=['GET', 'POST'])
def leftarrow():
    if(request.method=='POST'):
        client.perform_operation('left_arrow')
        return render_template('mouse.html')
    return render_template('mouse.html')

@app.route("/right_arrow", methods=['GET', 'POST'])
def rightarrow():
    if(request.method=='POST'):
        client.perform_operation('right_arrow')
        return render_template('mouse.html')
    return render_template('mouse.html')

@app.route("/scroll_up", methods=['GET', 'POST'])
def scrollup():
    if(request.method=='POST'):
        client.perform_operation('scroll,500')
        return render_template('mouse.html')
    return render_template('mouse.html')

@app.route("/scroll_down", methods=['GET', 'POST'])
def scrolldown():
    if(request.method=='POST'):
        client.perform_operation('scroll,-500')
        return render_template('mouse.html')
    return render_template('mouse.html')

@app.route("/exit", methods=['GET', 'POST'])
def exit_client():
    if(request.method=='POST'):
        client.perform_operation('exit')
        return render_template('mouse.html')
    return render_template('mouse.html')

if __name__=='__main__':
    app.run(debug=True, port=2581)
