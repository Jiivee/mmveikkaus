# -*- coding: utf-8 -*-

from app import db
from app.models import Team, Match, Group
from app.models import KnockoutTeams, User, MatchBet
import os
from datetime import datetime
_basedir = os.path.abspath(os.path.dirname(__file__))
os.remove(os.path.join(_basedir, 'app.db'))
db.drop_all()
db.create_all()

alankomaat  = Team(u'Alankomaat', u'ned')
algeria  = Team(u'Algeria', u'alg')
argentiina  = Team(u'Argentiina', u'arg')
australia  = Team(u'Australia', u'aus')
belgia  = Team(u'Belgia', u'bel')
bosnia_ja_hertsegovina  = Team(u'Bosnia ja Hertsegovina', u'bih')
brasilia  = Team(u'Brasilia', u'bra')
chile  = Team(u'Chile', u'chi')
costa_rica  = Team(u'Costa Rica', u'crc')
ecuador  = Team(u'Ecuador', u'ecu')
englanti  = Team(u'Englanti', u'eng')
espanja  = Team(u'Espanja', u'esp')
etela_korea  = Team(u'Etelä-Korea', u'kor')
ghana  = Team(u'Ghana', u'gha')
honduras  = Team(u'Honduras', u'hon')
iran  = Team(u'Iran', u'irn')
italia  = Team(u'Italia', u'ita')
japani  = Team(u'Japani', u'jpn')
kamerun  = Team(u'Kamerun', u'cmr')
kolumbia  = Team(u'Kolumbia', u'col')
kreikka  = Team(u'Kreikka', u'gre')
kroatia  = Team(u'Kroatia', u'cro')
meksiko  = Team(u'Meksiko', u'mex')
nigeria  = Team(u'Nigeria', u'nga')
norsunluurannikko  = Team(u'Norsunluurannikko', u'civ')
portugali  = Team(u'Portugali', u'por')
ranska  = Team(u'Ranska', u'fra')
saksa  = Team(u'Saksa', u'ger')
sveitsi  = Team(u'Sveitsi', u'sui')
uruguay  = Team(u'Uruguay', u'uru')
venaja  = Team(u'Venäjä', u'rus')
yhdysvallat  = Team(u'Yhdysvallat', u'usa')
db.session.add(alankomaat)
db.session.add(algeria)
db.session.add(argentiina)
db.session.add(australia)
db.session.add(belgia)
db.session.add(bosnia_ja_hertsegovina)
db.session.add(brasilia)
db.session.add(chile)
db.session.add(costa_rica)
db.session.add(ecuador)
db.session.add(englanti)
db.session.add(espanja)
db.session.add(etela_korea)
db.session.add(ghana)
db.session.add(honduras)
db.session.add(iran)
db.session.add(italia)
db.session.add(japani)
db.session.add(kamerun)
db.session.add(kolumbia)
db.session.add(kreikka)
db.session.add(kroatia)
db.session.add(meksiko)
db.session.add(nigeria)
db.session.add(norsunluurannikko)
db.session.add(portugali)
db.session.add(ranska)
db.session.add(saksa)
db.session.add(sveitsi)
db.session.add(uruguay)
db.session.add(venaja)
db.session.add(yhdysvallat)

group_a = Group('A')
group_a.teams.append(brasilia)
group_a.teams.append(kroatia)
group_a.teams.append(meksiko)
group_a.teams.append(kamerun)
db.session.add(group_a)
group_b = Group('B')
group_b.teams.append(espanja)
group_b.teams.append(alankomaat)
group_b.teams.append(chile)
group_b.teams.append(australia)
db.session.add(group_b)
group_c = Group('C')
group_c.teams.append(kolumbia)
group_c.teams.append(kreikka)
group_c.teams.append(norsunluurannikko)
group_c.teams.append(japani)
db.session.add(group_c)
group_d = Group('D')
group_d.teams.append(uruguay)
group_d.teams.append(costa_rica)
group_d.teams.append(englanti)
group_d.teams.append(italia)
db.session.add(group_d)
group_e = Group('E')
group_e.teams.append(sveitsi)
group_e.teams.append(ecuador)
group_e.teams.append(ranska)
group_e.teams.append(honduras)
db.session.add(group_e)
group_f = Group('F')
group_f.teams.append(argentiina)
group_f.teams.append(bosnia_ja_hertsegovina)
group_f.teams.append(iran)
group_f.teams.append(nigeria)
db.session.add(group_f)
group_g = Group('G')
group_g.teams.append(saksa)
group_g.teams.append(portugali)
group_g.teams.append(ghana)
group_g.teams.append(yhdysvallat)
db.session.add(group_g)
group_h = Group('H')
group_h.teams.append(belgia)
group_h.teams.append(algeria)
group_h.teams.append(venaja)
group_h.teams.append(etela_korea)
db.session.add(group_h)

matches = []
matches.append(Match(brasilia, kroatia, group_a, datetime(2014, 6, 12, 23, 00)))
matches.append(Match(meksiko, kamerun, group_a, datetime(2014, 6, 13, 19, 00)))
matches.append(Match(espanja, alankomaat, group_b, datetime(2014, 6, 13, 22, 00)))
matches.append(Match(chile, australia, group_b, datetime(2014, 6, 14, 01, 00)))
matches.append(Match(kolumbia, kreikka, group_c, datetime(2014, 6, 14, 19, 00)))
matches.append(Match(uruguay, costa_rica, group_d, datetime(2014, 6, 14, 22, 00)))
matches.append(Match(englanti, italia, group_d, datetime(2014, 6, 15, 01, 00)))
matches.append(Match(norsunluurannikko, japani, group_c, datetime(2014, 6, 15, 04, 00)))
matches.append(Match(sveitsi, ecuador, group_e, datetime(2014, 6, 15, 19, 00)))
matches.append(Match(ranska, honduras, group_e, datetime(2014, 6, 15, 22, 00)))
matches.append(Match(argentiina, bosnia_ja_hertsegovina, group_f, datetime(2014, 6, 16, 01, 00)))
matches.append(Match(saksa, portugali, group_g, datetime(2014, 6, 16, 19, 00)))
matches.append(Match(iran, nigeria, group_f, datetime(2014, 6, 16, 22, 00)))
matches.append(Match(ghana, yhdysvallat, group_g, datetime(2014, 6, 17, 01, 00)))
matches.append(Match(belgia, algeria, group_h, datetime(2014, 6, 17, 19, 00)))
matches.append(Match(brasilia, meksiko, group_a, datetime(2014, 6, 17, 22, 00)))
matches.append(Match(venaja, etela_korea, group_h, datetime(2014, 6, 18, 01, 00)))
matches.append(Match(australia, alankomaat, group_b, datetime(2014, 6, 18, 19, 00)))
matches.append(Match(espanja, chile, group_b, datetime(2014, 6, 18, 22, 00)))
matches.append(Match(kamerun, kroatia, group_a, datetime(2014, 6, 19, 01, 00)))
matches.append(Match(kolumbia, norsunluurannikko, group_c, datetime(2014, 6, 19, 19, 00)))
matches.append(Match(uruguay, englanti, group_d, datetime(2014, 6, 19, 22, 00)))
matches.append(Match(japani, kreikka, group_c, datetime(2014, 6, 20, 01, 00)))
matches.append(Match(italia, costa_rica, group_d, datetime(2014, 6, 20, 19, 00)))
matches.append(Match(sveitsi, ranska, group_e, datetime(2014, 6, 20, 22, 00)))
matches.append(Match(honduras, ecuador, group_e, datetime(2014, 6, 21, 01, 00)))
matches.append(Match(argentiina, iran, group_f, datetime(2014, 6, 21, 19, 00)))
matches.append(Match(saksa, ghana, group_g, datetime(2014, 6, 21, 22, 00)))
matches.append(Match(nigeria, bosnia_ja_hertsegovina, group_f, datetime(2014, 6, 22, 01, 00)))
matches.append(Match(belgia, venaja, group_h, datetime(2014, 6, 22, 19, 00)))
matches.append(Match(etela_korea, algeria, group_h, datetime(2014, 6, 22, 22, 00)))
matches.append(Match(yhdysvallat, portugali, group_g, datetime(2014, 6, 23, 01, 00)))

matches.append(Match(australia, espanja, group_b, datetime(2014, 6, 23, 19, 00)))
matches.append(Match(alankomaat, chile, group_b, datetime(2014, 6, 23, 19, 00)))
matches.append(Match(kamerun, brasilia, group_a, datetime(2014, 6, 23, 23, 00)))
matches.append(Match(kroatia, meksiko, group_a, datetime(2014, 6, 23, 23, 00)))
matches.append(Match(italia, uruguay, group_d, datetime(2014, 6, 24, 19, 00)))
matches.append(Match(costa_rica, englanti, group_d, datetime(2014, 6, 24, 19, 00)))
matches.append(Match(japani, kolumbia, group_c, datetime(2014, 6, 24, 23, 00)))
matches.append(Match(kreikka, norsunluurannikko, group_c, datetime(2014, 6, 24, 23, 00)))
matches.append(Match(nigeria, argentiina, group_f, datetime(2014, 6, 25, 19, 00)))
matches.append(Match(bosnia_ja_hertsegovina, iran, group_f, datetime(2014, 6, 25, 19, 00)))
matches.append(Match(honduras, sveitsi, group_e, datetime(2014, 6, 25, 23, 00)))
matches.append(Match(ecuador, ranska, group_e, datetime(2014, 6, 25, 23, 00)))
matches.append(Match(yhdysvallat, saksa, group_g, datetime(2014, 6, 26, 19, 00)))
matches.append(Match(portugali, ghana, group_g, datetime(2014, 6, 26, 19, 00)))
matches.append(Match(etela_korea, belgia, group_h, datetime(2014, 6, 26, 23, 00)))
matches.append(Match(algeria, venaja, group_h, datetime(2014, 6, 26, 23, 00)))
print "matches created"
for match in matches:
    db.session.add(match)
print "matches added"

db.session.commit()

print "db saved"

joni = User('joni', 'joni', 'joni')
joni.make_admin()
db.session.add(joni)
db.session.commit()


#############################
#############################
# TESTS
#############################
#############################
'''
knockout = KnockoutTeams()
knockout.add_qf_team(brasilia)
knockout.add_qf_team(englanti)
knockout.add_qf_team(ranska)
knockout.add_qf_team(saksa)
knockout.add_qf_team(belgia)
knockout.add_qf_team(argentiina)
knockout.add_qf_team(italia)

knockout.add_sf_team(brasilia)
knockout.add_sf_team(englanti)
knockout.add_sf_team(saksa)
knockout.add_sf_team(italia)

knockout.add_gold(englanti)
knockout.add_silver(brasilia)
knockout.add_bronze(saksa)

db.session.add(knockout)
db.session.commit()

game = Match.query.filter(Match.id==1).first()
game.set_goals(3, 2)
game = Match.query.filter(Match.id==2).first()
game.set_goals(1, 1)
game = Match.query.filter(Match.id==3).first()
game.set_goals(0, 0)
game = Match.query.filter(Match.id==4).first()
game.set_goals(0, 10)

matches = Match.query.all()
for match in matches:
    print str(match.id) + ': ' + match.home_team.name + ' ' + str(match.home_goals) + ' - ' + str(match.away_goals) + ' ' + match.away_team.name + ', Group: ' + match.group.name

groups = Group.query.all()
for group in groups:
    print group.name
    for team in group.teams:
        print team.name

knock = KnockoutTeams.query.first()
print 'Quarter finalists:'
for team in knock.qf_teams:
    print team.name
print 'Semi finalists:'
for team in knock.sf_teams:
    print team.name
print 'Winner:' + knock.gold.name
print 'Second:' + knock.silver.name
print 'Third:' + knock.bronze.name


#############################
#############################
# USER TESTS
#############################
#############################

joni = User('joni', 'joni.vayrynen@gmail.com', 'joni')
joni2 = User('Joni2', 'joni.vayrynen2@gmail.com', '123456')
db.session.add(joni)
db.session.add(joni2)
db.session.commit()

jb = User.query.filter(User.name=='joni').first().match_bets
for bet in jb:
    bet.make_bet(1, 2, 'X')

jb = User.query.filter(User.name=='Joni2').first().match_bets
for bet in jb:
    bet.make_bet(2, 2, 'X')

j = User.query.filter(User.name=='joni').first()
print 'total points:' + str(j.total_points)

Match.query.filter(Match.id==1).first().set_goals(1, 1)
Match.query.filter(Match.id==2).first().set_goals(2, 2)
Match.query.filter(Match.id==3).first().set_goals(3, 2)
Match.query.filter(Match.id==4).first().set_goals(3, 4)

j = User.query.filter(User.name=='joni').first()
print 'total points joni:' + str(j.total_points)

j = User.query.filter(User.name=='Joni2').first()
print 'total points joni2:' + str(j.total_points)

for bet in User.query.filter(User.name=='joni').first().match_bets:
    if bet.points != 0:
        print bet.points
'''
