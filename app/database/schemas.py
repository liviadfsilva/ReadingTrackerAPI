def individual_data(log):
    data = {"id": str(log["_id"])}
    
    data.update({
        key: value for key, value in log.items()
        if key in ["title", "author", "status", "start_reading_date", "finish_reading_date"] and value is not None
    })
    
    return data
    
def all_data(logs):
    return [individual_data(log) for log in logs]