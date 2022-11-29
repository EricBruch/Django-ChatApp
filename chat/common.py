def get_chat_id_or_default(id):
    myId = int(id) if id else 2
    return myId if myId > 2 and myId < 6 else 2
