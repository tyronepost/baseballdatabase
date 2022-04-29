import requests
import tarfile
from baseballdatabase.team import Team


def download_file(local_file):
    WRITE_BINARY = 'wb'
    URL = 'https://github.com/chadwickbureau/baseballdatabank/archive/refs/tags/v2022.2.tar.gz'

    print(f'Downloading file from {URL}...')
    data = requests.get(URL)
    with open(LOCAL_FILE, 'wb') as file:
        file.write(data.content)
    print('File downloaded.')


def extract_file(local_file):
    print(f'Extracting file...')
    file = tarfile.open(LOCAL_FILE)
    file.extractall('.')
    print('File extracted')


if __name__ == '__main__':
    LOCAL_FILE = 'baseballdatabank-2022.2.tar.gz'
    download_file(LOCAL_FILE)
    extract_file(LOCAL_FILE)

    TEAM_FRANCHISE_FILE = './baseballdatabank-2022.2/core/TeamsFranchises.csv'
    BATTING_FILE = './baseballdatabank-2022.2/core/Batting.csv'
    YEAR = '2007'
    TEAM_NAME = 'Detroit Tigers'

    team = Team(TEAM_FRANCHISE_FILE, BATTING_FILE, year=YEAR, team_name=TEAM_NAME)
    homerun_avg = team.get_homerun_avg()

    print(f'The team home run average for {TEAM_NAME} in the year {YEAR} is {homerun_avg}')
