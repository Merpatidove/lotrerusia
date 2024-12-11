from flask import Flask, render_template,request
import random

app = Flask(__name__)

silinder = [0, 0, 0, 0, 0, 0]  # Jumlah tembakan
urutan = 0
rounds = 0


@app.route('/')
def home():
    global silinder
    silinder = [0, 0, 0, 0, 0, 0]    # Mereset jumlah tembakan
    return render_template("menu.html")

@app.route('/pilihkoin', methods=['POST'])
def pilihkoion():
    global silinder, jumlahpeluru, urutan, rounds
    urutan = 0
    jumlahpeluru = int(request.form.get("jumlahpeluru"))
    rounds = jumlahpeluru
    
    if (jumlahpeluru >= 1 and jumlahpeluru <=6) :
        for i in range(jumlahpeluru):
            while 1:
                silindermasuk = random.randint(0, 5)
                if(silinder[silindermasuk] == 0):
                    silinder[silindermasuk] = 1
                    break
        return render_template("pilihkoin.html")
    
    else :
        return render_template("anomali.html")

@app.route("/menu", methods=['POST'])
def initplay():           
    koin = int(request.form.get("koin"))
    gacha = random.randint(0, 1)
    filegif = ""
    if(koin == gacha):
        if(koin == 1):
            filegif="static/image/kepalakoin.gif"
        else:
            filegif="static/image/apikoin.gif"
        return render_template("koin1.html", filegif=filegif)  
    else:
        if(koin == 0):
            filegif="static/image/kepalakoin.gif"
        else:
            filegif="static/image/apikoin.gif"

        return render_template("koin2.html", filegif=filegif)


@app.route('/play')
def play():    
    global silinder, jumlahpeluru, urutan
    
    if silinder[urutan] == 1:
        result ="BOOM! Sayang sekali, ANDA MATI"
        return render_template("gameover.html", result=result)
    elif silinder[urutan] == 0:
        result = f"KOSONG! Anda selamat, untuk sekarang. Sekarang silinder ke: {urutan + 1}"
        urutan += 1
        return render_template("hasil.html", result=result)  
    urutan +=1
        
    # peluru = random.randint(1, 6)  # Mengacak posisi peluru

    # pemain = (silinder % 6) + 1  # Posisi trigger pemain

    # if peluru == pemain:
    # e:
    #     return render_template("hasil.html", result=result)
    

@app.route('/bot_shoot' )
def shoot():
    global silinder, urutan
    # silinder += 1
    # lawan = (silinder % 6) + 1  # Posisi trigger lawan
    
    if silinder[urutan] == 1:
        result ="BOOM! Selamat, LAWAN ANDA MATI."
        return render_template("win.html", result=result)
    elif silinder[urutan] == 0:
        result = f"KOSONG! Lawan anda selamat. Sekarang giliran anda. Sekarang silinder ke: {urutan + 1}"
        urutan += 1
        return render_template("giliran_plyr.html", result=result)

    # if peluru == lawan:
    #     result ="BOOM! Kamu terkejut melihat pistol itu menembak tepat di kepala lawanmu, kamu selamat, tapi tidak dengan dia."
    #     return render_template("hasilhidup.html", result=result)
    # else:
    #     result = f"Click! Lawanmu bernafas lega, tapi tidak dengamu karena selanjutnya kamu bermain. silinder ke: {silinder}"
    #     return render_template("giliranbot.html", result=result)
    

@app.route('/cheat')
def shootbot():
    global urutan, silinder
    
    if silinder[urutan] == 1:
        result = "BOOM! Tanpa berpikir panjang, kamu menembak lawanmu, LAWANMU MATI!"
        return render_template("win.html", result=result)
    elif silinder[urutan] == 0:
        urutan += 1
        result = "KOSONG! Lawanmu marah dan langsung menghabisi kamu dengan kejam!"
        return render_template("gameover2.html", result=result)

@app.route('/reroll')
def reroll():
    global rounds, urutan
    for i in range(rounds):
        while 1:
            silindermasuk = random.randint(0, 5)
            if(silinder[silindermasuk] == 0):
                silinder[silindermasuk] = 1
                break
    urutan = 0        
    return render_template("silinder.html")

@app.route('/lanjut')
def lanjut():
    return render_template("giliran_roll.html")

    
    # silinder += 1
    # lawan = (silinder % 6) + 1  # Posisi trigger lawan
    # if peluru == lawan:
    #     result = "BOOM! Tanpa berpikir panjang, kamu menembak lawanmu, alangkah terkejutnya kamu karena pistolmu menembak dan lawanmu mati. Antara dia atau kamu, dan kamu selamat"
    #     return render_template("hasilhidup.html", result=result)
    # else:
    #     result = "Click! Apa yang kau pikirkan? lawanmu langsung menyerangmu habis habisan karena curang. Kamu mati. Menghapus C:\\Windows\\System32..."
    #     return render_template("hasilmati.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
