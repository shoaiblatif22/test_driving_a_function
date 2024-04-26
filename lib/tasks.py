def tasks(list):

    for item in list:
        keyword = "#TODO"
        if keyword not in list:
            return "no tasks to be completed"
        else:
            return list
