from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    messages = data["messages"]
    num_msg = 0
    for i in messages:
        text = i.get("text")
        if text:
            num_msg += 1
            
    return num_msg
print(find_number_of_messages(read_data("data/result.json")))