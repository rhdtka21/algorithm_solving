import requests
from bs4 import BeautifulSoup
#test crawling

Name = "qxt"

hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
teamMate = {}

def Is_Gaming(Name):
    req = requests.get('https://www.op.gg/summoner/spectator/userName=' + Name, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    if len(soup.select('script')) > 1:
        teamMate['SummonerName'] = []
        teamMate['Champion'] = []
        teamMate['played'] = []

        for i in soup.select('a.Link'):
            teamMate['SummonerName'].append(i.text.strip())
        
        
        for j in soup.select('div[class=recomm-ingame-champion]'):
            teamMate['Champion'].append(j.text)
        return True
        
    else:
        return False

def parseOPGG(Name):
    Container = {}
    Container
    SummonerName = ""
    Ranking = ""

    Tier = []
    LP = []
    Wins = []
    Losses = []
    Ratio = []

    Container['is_gaming'] = is_gaming
    url = 'https://www.op.gg/summoner/userName=' + Name
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    for i in soup.select('div[class=SummonerName]'):
        SummonerName = i.text
    Container['SummonerName'] = SummonerName

    for i in soup.select('span[class=ranking]'):
        Ranking = i.text
    Container['Ranking'] = Ranking

    for j in soup.select('div[class=Tier]'):
        Tier.append(j.text.strip())

    Container['Tier'] = Tier
    for i in soup.select('div[class=LP]'):
        LP.append(i.text)

    Container['LP'] = LP
    for i in soup.select('span[class=Wins]'):
        if len(Wins) >= len(Tier):
            break
        Wins.append(i.text)

    Container['Wins'] = Wins
    for i in soup.select('span[class=Losses]'):
        if len(Losses) >= len(Tier):
            break
        Losses.append(i.text)

    Container['Losses'] = Losses
    for i in soup.select('span[class=Ratio]'):
        Ratio.append(i.text)

    Container['Ratio'] = Ratio
    return Container


def printSummonerInfo(Container):
    rankCase = ['솔로', '자유']
    for i in range(len(Container['Tier'])):
        if Container['SummonerName'] != '':
            print("==================================")
            if len(Container['Tier']):
                print(Container['SummonerName'] + "님의 " + rankCase[i] + "랭크 정보입니다.")
                print("==================================")
                print("티어: " + Container['Tier'][i])
                print("LP: " + Container['LP'][i])
                print("승/패: " + Container['Wins'][i] + "/" + Container['Losses'][i])
                print("승률: " + Container['Ratio'][i])
            else:
                print(Container['SummonerName'] + "님은 Unranked입니다.")
                print("==================================")

def recentGameCrawl(Name):
    url = 'https://www.op.gg/summoner/userName=' + Name
    req = requests.get(url, headers=hdr)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    Container = {}

    i = soup.select('h2.Text')[0]
    Container['MatchInfo'] = i.text.replace('\n', '').replace('\t', '').strip('\n \t')

    i = soup.select('div.Right')[0]
    Container['Time'] = i.text.replace('\n', '').replace('\t', ' ')

    i = soup.select('div.GameItemList span.Kill')[0]
    j = soup.select('div.GameItemList span.Death')[0]
    k = soup.select('div.GameItemList span.Assist')[0]
    Container['KDA'] = i.text + '/' + j.text + '/' + k.text

    i = soup.select('div.KDARatio')[0]
    Container['KDARatio'] = i.text.replace('\n', '').replace('\t', '')

    i = soup.select('div.Stats')[0]
    Container['Stats'] = i.text.replace('\n', '').replace('\t', '')

    return Container

def printRecentGameInfo(Container):
    print("==================================")
    idx = Container['MatchInfo'].index("·")
    print(Container['MatchInfo'][:idx] + Container['MatchInfo'][idx+1:])
    idx = Container['Time'].index("초")
    print(Container['Time'][:idx+1] + ' ' + Container['Time'][idx+1:])
    idx = Container['Stats'].index("CS")
    print("KDA " + Container['KDA'] + ' ' +Container['Stats'][idx:])


    


is_gaming = Is_Gaming(Name)
print(teamMate)

summonerInfo = parseOPGG(Name)
recentGameInfo = recentGameCrawl(Name)

printSummonerInfo(summonerInfo)
printRecentGameInfo(recentGameInfo)




