# app.py
from config.dependencies import service

def main():
    fundos = service.get_all()
    for fundo in fundos:
        print(fundo.__dict__)

if __name__ == '__main__':
    main()
