n= int(input())
subject = {          ''' 자료구조: 딕셔너리 사용'''
    "Algorithm": 204,
    "DataAnalysis": 207,
    "ArtificialIntelligence": 302,
    "CyberSecurity": "B101",
    "Network": 303,
    "Startup": 501,
    "TestStrategy": 105
}
for _ in range(n):
    sub = input()
    print(subject[sub])
