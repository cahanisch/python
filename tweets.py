import json
import argparse

def main():

    p = argparse.ArgumentParser(description="Requires user to supply files to input to")

    p.add_argument("--output", required=True, nargs=3, dest='output')
    p.add_argument("--input", required=True, dest='input')

    arguments = p.parse_args()

    #build a new json file with tweet id, user id, if the tweet was favorited tell how many times, write to results.json
    with open(arguments.input, 'r') as f:
        data = f.readlines()

    fData = []

    for i in data:
        x = json.loads(i)
        tweets = {}
        tweets['tweet_id'] = x['id']
        tweets['user_id'] = x['user']['id']
        tweets['favorited'] = x['user']['favourites_count']
        fData.append(tweets)
        
    with open(arguments.output[0], 'w') as f:
        for i in fData:
            f.write(json.dumps(i)+"\n")
    #build a list of all timezones, count how many times each is found, print to tz.txt
    timezones = {}
    timezones['Unknown'] = 0
    for i in data:
        x = json.loads(i)
        if x['user']['time_zone'] is None:
            timezones['Unknown'] += 1
        elif x['user']['time_zone'] not in timezones:
            timezones[x['user']['time_zone']] = 1
        else:
            timezones[x['user']['time_zone']] += 1

    with open(arguments.output[1], 'w') as f:
        for i in timezones:
            x = timezones[i]
            f.write(str(i) + ": " + str(x) + "\n")

    #find all hashtags print to hashtags.txt
    hashtags = {}
    repeats = []
    with open(arguments.output[2], 'w') as f:
        for i in data: 
            x = json.loads(i)
            hashtags = x['entities']['hashtags']
            for j in hashtags:
                if j['text'] not in repeats:
                    repeats.append(j['text'])
                    f.write(j['text'] + "\n")
main()