from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    messages = data["messages"]
    user_name = []
    for msg in messages:
        if msg["type"] == "service":
            user_name.append(msg.get("actor"))
        if msg["type"] == "message":
            user_name.append(msg.get("from"))
    return user_name
    
print(find_all_users_name(read_data("data/result.json")))
