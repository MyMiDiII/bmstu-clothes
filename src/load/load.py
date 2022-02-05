from dataclasses import dataclass

@dataclass
class Load:
    fileName: str
    DATAPATH: str = './data/'

    def load(self):
        print('LOADING...')
        print('IT\'S OKAY!!!')
        
