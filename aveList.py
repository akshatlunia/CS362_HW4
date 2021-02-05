def aveList(v_list):
    ave = 0
    if type(v_list) is not list:
        return "not a list"
    if(len(v_list) == 0):
        return "list not populated"
    for i in v_list:
        if(type(i) != int and type(i) != float):
            return "input not numbered list"
        elif(isinstance(v_list[i-1], int) or isinstance(v_list[i-1], float)):
            ave += v_list[i-1]
        else:
            return "input not numbered list"
    ave = ave/len(v_list)
    return ave
