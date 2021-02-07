


from flask import Flask, redirect, url_for, request, render_template
import trial

app = Flask(__name__)




def mainfun(bb,ff):
      
        

    if ff=='5_3_2':#not working
        formation=trial.FORMATION_5_3_2

    if ff=='4_4_2':#working
        formation=trial.FORMATION_4_4_2
    if ff=='4_1_2_1_2':#not working
        formation=trial.FORMATION_4_1_2_1_2
    if ff=='4_2_4':#not working
        formation=trial.FORMATION_4_2_4
    if ff=='4_3_2_1':#not working
        formation=trial.FORMATION_4_3_2_1
    if ff=='3_5_2':#not working
        formation=trial.FORMATION_3_5_2

    TEMP=trial.create_temp(formation) 

    formation, ids = trial.compute_best_lineup(TEMP, formation, bb)
    
    return formation, ids

@app.route('/players.html/')
def players():
    ids=trial.allplayer()
    dictt=trial.player_details(ids)
    return render_template("players.html",dictt=dictt,n=len(ids),ids=ids)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Team.html/')
def Team():
    return render_template("Team.html")





@app.route ('/login', methods=['POST', "GET"])
def login() :
    if request.method=='POST':
        ff=request.form['ff']
        bb=int(request.form['bb'])* 10**6
        
        formation,ids=mainfun(bb,ff)
        print(len(ids))
        dictt=trial.player_details(ids)
        return render_template("team_id.html",n=len(ids),dictt=dictt ,formation=formation,ids=ids)
    else:
        user=request.args.get('ff','bb')
        return redirect (url_for('welcome', name=user) )

if __name__ == "__main__":
    app.run()


