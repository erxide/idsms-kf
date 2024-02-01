from datetime import datetime

def timestamp_to_dico(timestamp):
    if timestamp is not None or isinstance(timestamp, float):
        timestamp_obj = datetime.utcfromtimestamp(timestamp)
        return {'date/hour': f"{timestamp_obj.day}-{timestamp_obj.month}-{timestamp_obj.year} {timestamp_obj.hour}:{timestamp_obj.minute}:{timestamp_obj.second}"}
    else:
         return 'euh probleme sur le timestamp bro'
