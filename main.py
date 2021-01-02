async def get_join_position(ctx, user_id):
    """
    Gets the join position from the given user id
    Returns 0 for the person who owns/created the server
    if you don't want that, just add 1 to the output number
    you can use the following return statement to do so:
    return (int(position_list.index(str(user_id)) + 1 )
    """
    seq = " ".join(["{}-{}".format(x.joined_at.strftime("%Y-%m-%d"), x.id) for x in ctx.message.guild.members]) #all join dates in a single string
    sl = sorted(seq.split(), key=lambda x: tuple(map(int, x[0:].split("-"))), reverse=False) #sort them
    position_list = [] 
    for _ in sl:
        position_list.append(_.split("-")[-1]) #only append user ids to the position_list
    return position_list.index(str(user_id)) #get index of the given id from the position_list 