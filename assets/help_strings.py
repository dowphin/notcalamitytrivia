from cogs.fun import slots_odds

page1 = "\nNote that commands only work in dedicated channels\n### **!trivia**\nRuns trivia!\n### **!gamble**\nGambles slots for now."

page2 = "\nNote that commands only work in dedicated channels\n### **!add_question**\nAdds a question to the trivia sheet\n### **!delete_question**\nDeletes a question from the trivia sheet"

trivia_description = "\nContinuously sends trivia questions for the user to answer. Tracks points earned and time taken to answer.\n### **!points**\nDisplays your points earned from trivia\n### **!leaderboard**\nShows the top 10 most dedicated users of this bot"

points_description = "Displays your points earned from trivia"

leaderboard_description = "Shows the top 10 most dedicated users of this bot"

gamble_description = "Currently only contains slots. Run !help gamble slots to find out more."

slots_description = (f"Rolls a 3 x 5 grid of items. Your odds of rolling an item are:\n\n:pear:: `{slots_odds[0] * 100}%`\n:tangerine:: `{slots_odds[1] * 100}%`\n:strawberry:: `{slots_odds[2] * 100}%`\n:lemon:: `{slots_odds[3] * 100}%`\n:grapes:: `{slots_odds[4] * 100}%`\n:watermelon:: `{slots_odds[5] * 100}%`\n<:mystic_slime:1546711607269130342>: `{slots_odds[6] * 100}%`\n\nThere are also various possible patterns but I'm too lazy to explain those through a python string. Good luck!")

add_question_description = "adding qs"

delete_question_description = "deleting qs"