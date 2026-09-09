DISCORD_EPOCH = 1420070400000

def snowflake_to_time(id):
    return (id >> 22) + DISCORD_EPOCH

def time_difference(id1, id2):
    return abs(snowflake_to_time(id1) - snowflake_to_time(id2)) / 1000