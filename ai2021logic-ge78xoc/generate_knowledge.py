from field_var import field_var

def generate_knowledge(conf):
    kb = []
    new_proposition = ""
    
    for i in range(len(conf)):
        if conf[i] == 'empty':
            new_proposition = field_var(i,0) # Vi0 
            kb.append(new_proposition)
        elif conf[i] == 'stop':
            new_proposition = field_var(i,len(conf) - conf.count('empty')) # Vi4
            kb.append(new_proposition)
        elif conf[i] == 'right of way':
            new_proposition = field_var(i,1) # Vi1
            kb.append(new_proposition)
        else:
            if 'right of way' in conf:             # 如果有right of way标识，则 所有的conf[i] == '' 的情况都 令为2
                new_proposition = field_var(i,2)
                kb.append(new_proposition)
            else:
                new_proposition = field_var(i,1)    # 如果没有right of way标识，则 所有的conf[i] == '' 的情况都 令为1
                kb.append(new_proposition)
    
    RBL_index = [n for n,value in enumerate(conf) if value==''] # 获取conf列表中的''，对应的index
    
    # 两个 conf[i] == '' 且 有 'right of way' 的情况
    if len(RBL_index) == 2 and 'right of way' in conf:
        if RBL_index == [0, 3]:
            new_proposition = field_var(RBL_index[0],2) + " & " + field_var(RBL_index[1],2) + " ==> " + field_var(RBL_index[1],3)
        else:
            new_proposition = field_var(RBL_index[0],2) + " & " + field_var(RBL_index[1],2) + " ==> " + field_var(RBL_index[0],3) 
    kb.append(new_proposition)
    
    # 两个 conf[i] == '' 且 无 'right of way' 的情况
    if len(RBL_index) == 2 and 'right of way' not in conf:
        if RBL_index == [0, 3]:
            new_proposition = field_var(RBL_index[0],1) + " & " + field_var(RBL_index[1],1) + " ==> " + field_var(RBL_index[1],2)
        else:
            new_proposition = field_var(RBL_index[0],1) + " & " + field_var(RBL_index[1],1) + " ==> " + field_var(RBL_index[0],2)
    kb.append(new_proposition)
    
    # 三个 conf[i] == '' 且 有 'right of way' 的情况
    if len(RBL_index) == 3 and 'right of way' in conf: 
        ROW_index = conf.index('right of way')
        new_proposition = field_var(RBL_index[0],2) + " & " + field_var(RBL_index[1],2) + " & " + field_var(RBL_index[2],2) + " ==> " + field_var(RBL_index[ROW_index - 3],4) + " & " + field_var(RBL_index[ROW_index - 2],3)
    kb.append(new_proposition)
    
    # 三个 conf[i] == '' 且 无 'right of way' 的情况
    if len(RBL_index) == 3 and 'right of way' not in conf: 
        if 'empty' in conf:
            Empty_or_Stop_index = conf.index('empty')
        else:
            Empty_or_Stop_index = conf.index('stop')  # 找到剩余的那个索引
        new_proposition = field_var(RBL_index[0],1) + " & " + field_var(RBL_index[1],1) + " & " + field_var(RBL_index[2],1) + " ==> " + field_var(RBL_index[Empty_or_Stop_index - 3],3) + " & " + field_var(RBL_index[Empty_or_Stop_index - 2],2)
    kb.append(new_proposition)
    
    # try with 5 example configurations
    #new_proposition = field_var(2,2) + " & " + field_var(3,2) + " ==> " + field_var(2,3)
    #kb.append(new_proposition)  # intersection1 = ['right of way','empty','','']
    
    #new_proposition = field_var(0,1) + " & " + field_var(1,1) + " ==> " + field_var(0,2)
    #kb.append(new_proposition)  # intersection2 = ['', '', 'empty', 'empty'] # intersection3 = ['','','stop', 'empty']
     
    #new_proposition = field_var(1,2) + " & " + field_var(2,2) + " ==> " + field_var(1,3)
    #kb.append(new_proposition)  # intersection4 = ['stop','','','right of way']
    
    #new_proposition = field_var(0,1) + " & " + field_var(2,1) + " & " + field_var(3,1) + " ==> " + field_var(3,2) + " & " + field_var(2,3)
    #kb.append(new_proposition)  # intersection5 = ['','stop','','']
    
    return kb
