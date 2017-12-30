from urllib.request import urlopen
from urllib.request import URLError
from urllib.request import Request
from json import loads

def getTracks(url):
    print('\n>> Getting tracks from {0}'.format(url))
    token = 'Bearer BQAwDapyI_hbbtO2X91uc_3WafowKzILVFQOGyjk40WX31ZOclN3fwZVc328ffqN2mc5tHaBEBB76rGLoilZ1xW0AHYxXLNH9AMlgQlKdjnas0RbhnhDJog_x4_pEqxiHfwrYVIomFt7ieDYZ2Fzpng15S95FFM5NA'
    request = Request(url, headers={'Authorization': token})
    try:
        response = urlopen(request)
        data = response.read()
        encoding = response.info().get_content_charset('utf8')
        return loads(data.decode(encoding))['items']
    except(URLError, e):
        print('Fail', e)

def main():
    tlUrl = 'https://api.spotify.com/v1/users/robcthegeek/playlists/2JwE2prZ0fdX82d3alpGhQ/tracks?fields=items(track(id,name,artists(name)),added_by(id))&offset=00'
    rbUrl = 'https://api.spotify.com/v1/users/rockbandofficial/playlists/1LOZfgjinUc6K2mz8wjPz3/tracks?fields=items(track(id))&offset=600'

    tlTracks = getTracks(tlUrl)
    rbTracks = getTracks(rbUrl)
    testTracks = [{'track': {'id': '7LRMbd3LEoV5wZJvXT1Lwb'}}]

    # print('\ntlTracks: ', tlTracks)
    # print('\nrbTracks: ', rbTracks)
    # print('\ntestTracks: ', testTracks)

    #testIds = list(map(lambda track:track['track']['id'], testTracks))
    rbIds = [track['track']['id'] for track in rbTracks]

    # print('\nrbIds: ', rbIds)

    #any(x.name == "t2" for x in l)

    matches = []

    for track in tlTracks:
        if any(rbId == track['track']['id'] for rbId in rbIds):
            # print('track id', track['track']['id'])
            matches.append(track)

    # print('matches', matches)

    for track in matches:
        print('\n\n*** Match: {track[name]} by {track[artists][0][name]}. Added by {added_by[id]}. ***'.format(**track))

    if len(matches) == 0:
        print('** No matches :(')
    else:
        print('*** {0} matches found. ***'.format(len(matches))) # pluralisation (1 matches)

if __name__ == '__main__':
    main()
