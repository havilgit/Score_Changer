import requests
score = input("score: ")
nickname = raw_input("nickname ")
gameMode = input("gameMode:(1,2,3)")
data={"score":score,"nickname":nickname,"gameid":"145","gameMode":gameMode}
r = requests.post('http://www.littlebigplay.com/submitAir.php',data)


