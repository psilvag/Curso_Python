import json
from exceptions import gameTypeFileError

def open_json_to_dict(path:str)->dict:
    """
    Converte json to dict
    args:
        path: str:   path file
    return:   dict:  info from player
    """
    if(path.endswith(".json")):
        with open(path,"r") as info_player:
            data=json.load(info_player)
            return data
    raise gameTypeFileError()
    




    