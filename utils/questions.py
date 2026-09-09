import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(BASE_DIR, "..", "data", "questions.db")

os.makedirs(os.path.dirname(QUESTIONS_FILE), exist_ok=True)

quest = sqlite3.connect(QUESTIONS_FILE)

cur = quest.cursor()

def create(): #debug purposes
    cur.execute("CREATE TABLE questions(question, answer)")

def clear(password): #debug purposes
    if password == "actually clear ts" + str(2**5):
        cur.execute("DROP TABLE questions")

def fetch_all(): #debug purposes
    cur.execute("SELECT rowid, question, answer FROM questions")
    for i in cur.fetchall():
        print(i)

def total_questions():
    cur.execute("SELECT COUNT(*) FROM questions")
    return cur.fetchone()[0]

def update_question(row_id, question):
    cur.execute("UPDATE questions SET question=? WHERE rowid=?", (question, row_id))
    quest.commit()

def update_answer(row_id, answer):
    cur.execute("UPDATE questions SET answer=? WHERE rowid=?", (answer, row_id))
    quest.commit()

def fetch_by_num(row_id):
    cur.execute("SELECT question, answer FROM questions WHERE rowid = ?", (row_id,))
    return cur.fetchone()

def fetch_by_question(question):
    cur.execute("SELECT rowid, question, answer FROM questions WHERE question = ?", (question,))
    return cur.fetchone()

def insert(question, answer):

    cur.execute("INSERT INTO questions VALUES (?, ?)", (question, answer.lower()))
    quest.commit()

def delete_by_row_id(row_id):

    cur.execute("DELETE FROM questions WHERE rowid = ?", (row_id,))
    quest.commit()

def answer_fix(): # cannot run this while the bot is active
    cur.execute("UPDATE questions SET answer = LOWER(answer)")

    rows = cur.execute("SELECT rowid, answer FROM questions").fetchall()

    for rowid, answer in rows:
        answers = answer.split(";")
        new_answers = [a.strip() for a in answers]
        final_new = ";".join(new_answers)
        cur.execute("UPDATE questions SET answer = ? WHERE rowid = ?", (final_new, rowid))

    quest.commit()

