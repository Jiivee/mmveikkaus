from flask import render_template, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
from forms import RegistrationForm, LoginForm
from models import  User, MatchBet, Match, Group
from datetime import datetime


@app.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    groups = Group.query.all()
    time_now = datetime.now()
    next_matches = Match.query.filter(Match.time>time_now).order_by(Match.time).limit(5)
    return render_template("index.html", form=form, current_user=current_user, groups=groups, next_matches=next_matches)


@app.route('/makebets/', methods=['GET', 'POST'])
@login_required
def betting():
    if request.method == 'POST':
        print request.form
        for i in range(1, 49): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CHANGE TO 49 AFTER TESTING
            mark = str(request.form[str(i)])
            home_goals = str(request.form['home-' + str(i)])
            away_goals = str(request.form['away-' + str(i)])
            MatchBet.query.filter(MatchBet.user_id==current_user.id, MatchBet.match_id==i).first().make_bet(home_goals, away_goals, mark)
        db.session.commit()
    bets = MatchBet.query.filter(MatchBet.user_id==current_user.id).all()
    return render_template("makebets.html", current_user=current_user, bets=bets)


@app.route('/showbets/', methods=['GET', 'POST'])
@login_required
def user_bets():
    bets = current_user.match_bets
    return render_template("bets.html", current_user=current_user, bets=bets)


@app.route('/allmatches/', methods=['GET', 'POST'])
@login_required
def all_matches():
    matches = Match.query.order_by(Match.time)
    return render_template("allmatches.html", current_user=current_user, matches=matches)


@app.route('/setresult/<id>/', methods=['GET', 'POST'])
@login_required
def set_match_result(id):
    match = Match.query.filter(Match.id==id).first()
    if current_user.role != 1:
        return redirect(url_for("all_matches"))
    if request.method == 'POST':
        print request.form
        home_goals = str(request.form['home-goals'])
        away_goals = str(request.form['away-goals'])
        match.set_goals(home_goals, away_goals)
        db.session.commit()
        return redirect(url_for("all_matches"))
    return render_template("setresult.html", current_user=current_user, match=match)


@app.route('/points/', methods=['GET', 'POST'])
@login_required
def points():
    matches = Match.query.all()
    print matches
    users = User.query.order_by(User.total_points.desc())
    return render_template("points.html", current_user=current_user, users=users)





@app.route('/register/' , methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(form.name.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(request.args.get("next") or url_for("index"))
    return render_template('register.html', current_user=current_user, form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        user = User.query.filter(User.email==user_email, User.password==user_password).first()
        login_user(user)
        return redirect(url_for("index"))
    return render_template("login.html", current_user=current_user, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


