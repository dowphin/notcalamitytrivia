import json
import os

POINTS_FILE = "data/points.json"

def load_scores():
    if not os.path.exists(POINTS_FILE):
        return {}

    with open(POINTS_FILE, "r") as f:
        return json.load(f)

def save_scores(scores):
    with open(POINTS_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def add_point(user_id):

    scores = load_scores()
    user_id = str(user_id)

    if user_id not in scores:
        scores[user_id] = 0

    scores[user_id] = scores.get(user_id, 0) + 1

    scores = sort_points(scores)

    save_scores(scores)

def read_points(user_id):
    scores = load_scores()
    user_id = str(user_id)
    return scores[user_id]

def fetch_scores():

    scores = load_scores()
    return scores

def sort_points(scores): # does not scale well if more than 20 people use the bot i think

    scores_items = list(scores.items())

    for i in range (1, len(scores_items)):
        current = scores_items[i]
        j = i - 1

        while j >= 0 and scores_items[j][1] < current[1]:
            scores_items[j + 1] = scores_items[j]
            j -= 1

        scores_items[j + 1] = current

    return dict(scores_items)