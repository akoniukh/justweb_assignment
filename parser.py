import json

file = open('data.json', 'r')
_data = json.load(file)


def update_avg(num, cnt, curr_avg):
    return round((cnt * curr_avg + num) / (cnt + 1), ndigits=2)


def parse(data):
    stars = {}
    for movie in data:
        curr_rating = float(movie["rating"])
        for star in movie["stars"].split(', '):
            if star not in stars:
                stars[star] = {"cnt": 1, "avg": curr_rating}
            else:
                stars[star]["avg"] = update_avg(curr_rating, stars[star]["cnt"], stars[star]["avg"])
                stars[star]["cnt"] += 1

    for star in sorted(stars.items(), key=lambda actor: actor[1]["cnt"], reverse=True):
        if star[1]["cnt"] < 2:
            break
        print(f"Star Name: {star[0]}\nMovies: {star[1]['cnt']} | AVG Rating: {star[1]['avg']}")


parse(_data)
