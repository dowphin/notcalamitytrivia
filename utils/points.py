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
    save_scores(scores)

def read_points(user_id):
    scores = load_scores()
    user_id = str(user_id)
    return scores[user_id]

def sort_points():
    scores = load_scores()

    sorted_scores = {k: v for k,v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

    return sorted_scores
