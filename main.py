from flask import *
import random, os

app = Flask(__name__)
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

@app.route("/")
def hello_world():
    return f'<h1>DON POLLO SAID BLA BLA BLA BLE BLE BLE BLU BLU BLU🗣️🔥‼️💯</h1> <a href="/random_fact">See random fax</a>\n<a href="/random_emote">See random emote</a>\n<a href="/random_coinFlip">See random coin flip retults</a>\n<a href="/random_img">See random photos</a>'
    

@app.route("/random_fact")
def facts():
    return f'<p>{ random.choice(facts_list) }</p> <br></br ><a href="/">Return to the home pagesssssssssssssssssssssssss</a>'

@app.route("/random_emote")
def emote_func():
    emotes = ['\U0001F914', '\U0001F604', '\U0001F610', '\U0001F639', '\U0001F480', '\U0001F940', '\U0001F494']
    return random.choice(emotes)

@app.route("/random_coinFlip")
def coinFlip_func():
    flip = random.randint(0, 1)
    o = 'you got a '
    if flip == 0:
        return f'{o}tail'
    else:
        return f'{o}head'
    
@app.route("/random_img")
def dropRandomImg_func():
    img_name = random.choice(os.listdir('random_img'))
    return img_name

app.run(debug=True)