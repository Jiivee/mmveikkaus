from app import db, app
from app import app



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))
    active = db.Column(db.Boolean())
    match_bets = db.relationship("MatchBet")
    total_points = db.Column(db.Integer)
    role = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.total_points = 0
        self.role = 0
        self.create_bets()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)

    def create_bets(self):
        matches = Match.query.all()
        for match in matches:
            self.match_bets.append(MatchBet(match))

    def make_admin(self):
        self.role = 1


class Match(db.Model):
    __tablename__ = 'match'
    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    home_team = db.relationship("Team", foreign_keys=[home_team_id])
    away_team = db.relationship("Team", foreign_keys=[away_team_id])
    time = db.Column(db.DateTime)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    group = db.relationship("Group")
    home_goals = db.Column(db.Integer)
    away_goals = db.Column(db.Integer)

    def __init__(self, home_team, away_team, group, time):
        self.home_team = home_team
        self.away_team = away_team
        self.group = group
        self.time = time
        self.home_goals = None
        self.away_goals  = None
        self.mark = None


    def set_goals(self, home_goals, away_goals):
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.check_mark()
        self.calculate_user_points()
        db.session.commit()


    def check_mark(self):
        if self.home_goals > self.away_goals:
            self.mark = '1'
        elif self.home_goals < self.away_goals:
            self.mark = '2'
        else:
            self.mark = 'X'


    def calculate_user_points(self):
        bets = MatchBet.query.filter(MatchBet.match==self).all()
        for bet in bets:
            points = 0
            right_answers = 0
            if self.home_goals == bet.bet_home_goals:
                points += 1
                right_answers += 1
            if self.away_goals == bet.bet_away_goals:
                points += 1
                right_answers += 1
            if self.mark == bet.mark:
                points += 2
                right_answers += 1
            if right_answers == 3:
                points += 1
            user = User.query.filter(User.id==bet.user_id).first()
            user.total_points -= bet.points
            bet.set_points(points)
            user.total_points += points

    def get_date(self):
        date = self.time.strftime("%d.%m.%Y")
        return date

    def get_time(self):
        time = self.time.strftime("%H:%M")
        return time



class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1))
    teams = db.relationship("Team", foreign_keys="Team.group_id")
    winner_id = db.Column(db.Integer)
    runner_up_id = db.Column(db.Integer)

    def __init__(self, name=None):
        self.name = name
        self.winner_id = None
        self.runner_up_id = None

    def set_winner_id(self, id):
        self.winner_id = id

    def set_runner_up_id(self, id):
        self.runner_up_id = id


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    short = db.Column(db.String(3))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    quarter_finalist_id = db.Column(db.Integer, db.ForeignKey('knockout_teams.id'))
    semi_finalist_id = db.Column(db.Integer, db.ForeignKey('knockout_teams.id'))
    gold_id = db.Column(db.Integer, db.ForeignKey('knockout_teams.id'))
    silver_id = db.Column(db.Integer, db.ForeignKey('knockout_teams.id'))
    bronze_id = db.Column(db.Integer, db.ForeignKey('knockout_teams.id'))

    def __init__(self, name, short):
        self.name = name
        self.short = short


class KnockoutTeams(db.Model):
    __tablename__ = 'knockout_teams'
    id = db.Column(db.Integer, primary_key=True)
    qf_teams = db.relationship("Team", foreign_keys="Team.quarter_finalist_id")
    sf_teams = db.relationship("Team", foreign_keys="Team.semi_finalist_id")
    gold = db.relationship("Team", uselist=False, foreign_keys="Team.gold_id")
    silver = db.relationship("Team", uselist=False, foreign_keys="Team.silver_id")
    bronze = db.relationship("Team", uselist=False, foreign_keys="Team.bronze_id")

    def __init__(self):
        pass

    def add_qf_team(self, team):
        self.qf_teams.append(team)

    def add_sf_team(self, team):
        self.sf_teams.append(team)

    def add_gold(self, team):
        self.gold = team

    def add_silver(self, team):
        self.silver = team

    def add_bronze(self, team):
        self.bronze = team

class MatchBet(db.Model):
    __tablename__ = 'match_bet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    match = db.relationship("Match", uselist=False, foreign_keys=[match_id])
    bet_home_goals = db.Column(db.Integer)
    bet_away_goals = db.Column(db.Integer)
    mark = db.Column(db.String(1))
    points = db.Column(db.Integer)

    def __init__(self, match):
        self.match = match
        self.points = 0


    def make_bet(self, home_goals, away_goals, mark):
        self.bet_home_goals = home_goals
        self.bet_away_goals = away_goals
        self.mark = mark
        print 'bet made'
        print self.bet_home_goals
        print MatchBet.query.filter(MatchBet.id==self.id).first().bet_home_goals
        print db.session.query(MatchBet).filter(MatchBet.id==self.id).first().bet_home_goals
        return self

    def set_points(self, points):
        self.points = points

    def __repr__(self):
        return '<MatchBet ' + str(self.id) + ' ' + str(self.bet_home_goals) + '-' + str(self.bet_away_goals) + ' mark: ' + str(self.mark) + ' points: ' + str(self.points) +'>'
