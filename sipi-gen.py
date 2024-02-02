from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__, template_folder='templates')

def genstr(length): #a function that would generate a random word of letters and numbers
    s = string.ascii_letters + string.digits
    return ''.join(random.choice(s) for i in range(length))

@app.route('/') #the default endpoint
def index():
    return render_template("home.html")

@app.route('/generate', methods=['POST']) 
def generate():
    #/generate endpoint:it generates random values for each key in the sipi form 
    name = genstr(random.randint(1,15))
    challenge = genstr(random.randint(1,15))
    statement = genstr(random.randint(1,15))
    hmws = [genstr(random.randint(1,15)) for i in range(random.randint(1,20))]
    survey = [genstr(random.randint(1,15)) for i in range(random.randint(1,20))]
    persona = genstr(random.randint(1,15))
    data_exp = genstr(random.randint(1,15))
    tools_array = [genstr(random.randint(1,15)) for i in range(random.randint(1,20))]
    vp = genstr(random.randint(1,15))
    bm = genstr(random.randint(1,15))
    ethics = genstr(random.randint(1,15))

    result = { #stores the generated values in a python dictionary
"Project Name": name,
"SDG": challenge,
"Problem": statement,
"HMWS": hmws,
"survey": survey,
"Persona": persona,
"data": data_exp,
"tech tools": tools_array,
"Value proposition": vp,
"Business model": bm,
"ETHICS": ethics    
}
    global prompt
    prompt = request.form.get('input_prompt') #makes a request to retrieve the value of the text input 
    return jsonify(result) #returning the dictionary in a .JSON format
if __name__ == '__main__':
    app.run()
