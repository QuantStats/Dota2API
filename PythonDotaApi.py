import dota2api

#get your API ID from Valve from
#https://developer.valvesoftware.com/wiki/Steam_Web_API
#an account registration is free

api_id = 'abc12345' #replace this string with your API ID
api = dota2api.Initialise(api_id)

match = api.get_live_league_games()

spec_total = 0

print('***Live matches stats***')

for j in range(0, len(match['games'])):
    spec_no = match['games'][j]['spectators']
    spec_total = spec_no+spec_total
    print('Match_' + str(j+1) + ': ' + str(spec_no))

print('Total number of spectators = ' + str(spec_total))


