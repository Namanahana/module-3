from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">View a random fact!</a>'

@app.route("/about") 
def about():
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>Tentang Kami</h1>
            <p>Ini adalah halaman tentang kami. Kami adalah tim yang fantastis!</p>
        </body>
    </html>
    """

@app.route("/tentang")
def tentang():
    return '<h1>Ini tentang...</h1>'

facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/gen_pass")
def gen_pass(pass_length=5):
    elements = "+-/*!&$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)

    return password

app.run(debug=True)

