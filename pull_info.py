import json
import csv,time,urllib.request


for i in range(1500):
    client_ID = "oveh1g6di5huekxjf7h1rxn1r4js0i"
    
    url = "https://api.twitch.tv/helix/streams"

    req = urllib.request.Request(url, headers={"Client-ID": client_ID})

    response = urllib.request.urlopen(req)

    twitch = json.loads(response.read())

    count = 0

    with open("Twitch.json", "w+") as json_file:
        json.dump(twitch, json_file, sort_keys = True, indent=4)

    with open("Twitch.json") as json_file:
        twitch = json.load(json_file)

    data = twitch['data']
    data_file = open("Twitch.csv", "a")
    csv_writer = csv.writer(data_file)

    for d in data:
        if count == 0:
            header = d.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(d.values())
    data_file.close()

    time.sleep(1800)
    



