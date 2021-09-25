import logging
import json
import pickle
from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def parasite1(dataI):
    res=[]
    for room in dataI:
        copy = room['grid']
        sgrid =  pickle.loads(pickle.dumps(copy, -1))
        sgrid1 = pickle.loads(pickle.dumps(copy, -1))
        
        
        interestedIndividuals = room['interestedIndividuals']
        ii = {}
        for i in interestedIndividuals:
            ii[i]=-1
        startInfected = []
        startnonInfected = []
        rowLen = len(sgrid) -1
        rowLen1 = rowLen+1
        colLen = len(sgrid[0]) -1
        colLen1 = colLen+1
        for r in range(0,rowLen1):
            # print(r)
            for c in range(0,colLen1):
                # print(c)
                var = sgrid[r][c]
                # print (var)
                if var == 3:
                    startInfected = [[r,c]]
                elif var == 1:
                    startnonInfected.append([r,c])
                elif var == 2:
                    sgrid[r][c] = 0
                    sgrid1[r][c] = 0
                    
        canStillInfect = True
        infectedA = startInfected[:]
        allinfectedA = startInfected[:]
        noninfectedA = startnonInfected[:]
        
        newInfectedA = []
        tick = 0
        while canStillInfect:
            tick += 1
            for i in infectedA:
                cur_pos_r = i[0]
                cur_pos_c = i[1]
        
                left_pos = [cur_pos_r,cur_pos_c-1]
                right_pos = [cur_pos_r,cur_pos_c+1]
                up_pos = [cur_pos_r-1,cur_pos_c]
                down_pos = [cur_pos_r+1,cur_pos_c]
                
                if left_pos[0] in range(0,rowLen+1) and left_pos[1] in range(0,colLen+1):
                    who_l = sgrid[left_pos[0]][left_pos[1]]
                else:
                    who_l = 0
                if right_pos[0] in range(0,rowLen+1) and right_pos[1] in range(0,colLen+1):
                    who_r= sgrid[right_pos[0]][right_pos[1]]
                else:
                    who_r =0
                if up_pos[0] in range(0,rowLen+1) and up_pos[1] in range(0,colLen+1):
                    who_u= sgrid[up_pos[0]][up_pos[1]]
                else:
                    who_u = 0
                if down_pos[0] in range(0,rowLen+1) and down_pos[1] in range(0,colLen+1):
                    who_d= sgrid[down_pos[0]][down_pos[1]]
                else:
                    who_d = 0
                # print(left_pos)
                # print(right_pos)
                # print(up_pos)
                # print(down_pos)
                # print("-----")
                # print(who_l)
                # print(who_r)
                # print(who_u)
                # print(who_d)
                # # canInfect = who_l+who_r+who_u+who_d
                # if canInfect > 1:
                if who_l == 1 :
                    sgrid[left_pos[0]][left_pos[1]] = 3
                    newInfectedA.append(left_pos)
                    str_join = str(left_pos[0]) +","+ str(left_pos[1])
                    noninfectedA.remove(left_pos)
                    if str_join in ii:
                        ii[str_join]=tick
                        
                if who_r == 1 :
                    sgrid[right_pos[0]][right_pos[1]] = 3
                    newInfectedA.append(right_pos)
                    str_join = str(right_pos[0]) +","+ str(right_pos[1])
                    noninfectedA.remove(right_pos)
                    if str_join in ii:
                        ii[str_join]=tick
        
                if who_u == 1 :
                    sgrid[up_pos[0]][up_pos[1]] = 3
                    newInfectedA.append(up_pos)
                    str_join = str(up_pos[0]) +","+ str(up_pos[1])
                    noninfectedA.remove(up_pos)
                    if str_join in ii:
                        ii[str_join]=tick
        
                if who_d == 1 :
                    sgrid[down_pos[0]][down_pos[1]] = 3
                    newInfectedA.append(down_pos)
                    str_join = str(down_pos[0]) +","+ str(down_pos[1])
                    noninfectedA.remove(down_pos)
                    if str_join in ii:
                        ii[str_join]=tick    
            infectedA = newInfectedA
            allinfectedA.extend(newInfectedA)
            # print(newInfectedA)
            # print("tick",tick)
            if newInfectedA == []:
                canStillInfect = False
            newInfectedA = []
            
        
        #p3
        canStillInfect = True
        infectedB = startInfected
        allinfectedB = startInfected
        noninfectedB = startnonInfected
        newInfectedB=[]
        
        tick1 = 0
        while canStillInfect:
            tick1 += 1
            for i in infectedB:
                cur_pos_r = i[0]
                cur_pos_c = i[1]
        
                left_pos = [cur_pos_r,cur_pos_c-1]
                right_pos = [cur_pos_r,cur_pos_c+1]
                up_pos = [cur_pos_r-1,cur_pos_c]
                down_pos = [cur_pos_r+1,cur_pos_c]
                ##B##
                tl_pos = [cur_pos_r-1,cur_pos_c-1]
                tr_pos = [cur_pos_r-1,cur_pos_c+1]
                bl_pos = [cur_pos_r+1,cur_pos_c-1]
                br_pos = [cur_pos_r+1,cur_pos_c+1]
                
                if left_pos[0] in range(0,rowLen+1) and left_pos[1] in range(0,colLen+1):
                    who_l = sgrid1[left_pos[0]][left_pos[1]]
                else:
                    who_l = 0
                if right_pos[0] in range(0,rowLen+1) and right_pos[1] in range(0,colLen+1):
                    who_r= sgrid1[right_pos[0]][right_pos[1]]
                else:
                    who_r =0
                if up_pos[0] in range(0,rowLen+1) and up_pos[1] in range(0,colLen+1):
                    who_u= sgrid1[up_pos[0]][up_pos[1]]
                else:
                    who_u = 0
                if down_pos[0] in range(0,rowLen+1) and down_pos[1] in range(0,colLen+1):
                    who_d= sgrid1[down_pos[0]][down_pos[1]]
                else:
                    who_d = 0
                    
                    
                ##B##
                if tl_pos[0] in range(0,rowLen+1) and tl_pos[1] in range(0,colLen+1):
                    who_tl = sgrid1[tl_pos[0]][tl_pos[1]]
                else:
                    who_tl = 0
                    
                if tr_pos[0] in range(0,rowLen+1) and tr_pos[1] in range(0,colLen+1):
                    who_tr= sgrid1[tr_pos[0]][tr_pos[1]]
                else:
                    who_tr =0
                    
                if bl_pos[0] in range(0,rowLen+1) and bl_pos[1] in range(0,colLen+1):
                    who_bl= sgrid1[bl_pos[0]][bl_pos[1]]
                else:
                    who_bl = 0
                    
                if br_pos[0] in range(0,rowLen+1) and br_pos[1] in range(0,colLen+1):
                    who_br= sgrid1[br_pos[0]][br_pos[1]]
                else:
                    who_br = 0
                    
                # print("currpos",i)
                # print("--B--")
                # print(left_pos)
                # print(right_pos)
                # print(up_pos)
                # print(down_pos)
                # print(tl_pos)
                # print(tr_pos)
                # print(bl_pos)
                # print(br_pos)
                # print("-----")
                # print(who_l)
                # print(who_r)
                # print(who_u)
                # print(who_d)
                # print(who_tl)
                # print(who_tr)
                # print(who_bl)
                # print(who_br)
                # canInfect = who_l+who_r+who_u+who_d
                # if canInfect > 1:
                if who_l == 1 :
                    sgrid1[left_pos[0]][left_pos[1]] = 3
                    newInfectedB.append(left_pos)
                    str_join = str(left_pos[0]) +","+ str(left_pos[1])
                    noninfectedB.remove(left_pos)
        
                if who_r == 1 :
                    sgrid1[right_pos[0]][right_pos[1]] = 3
                    newInfectedB.append(right_pos)
                    str_join = str(right_pos[0]) +","+ str(right_pos[1])
                    noninfectedB.remove(right_pos)
        
                if who_u == 1 :
                    sgrid1[up_pos[0]][up_pos[1]] = 3
                    newInfectedB.append(up_pos)
                    str_join = str(up_pos[0]) +","+ str(up_pos[1])
                    noninfectedB.remove(up_pos)
        
                if who_d == 1 :
                    sgrid1[down_pos[0]][down_pos[1]] = 3
                    newInfectedB.append(down_pos)
                    str_join = str(down_pos[0]) +","+ str(down_pos[1])
                    noninfectedB.remove(down_pos)
                    # print("CASD")
                ##B##
                if who_tl == 1 :
                    sgrid1[tl_pos[0]][tl_pos[1]] = 3
                    newInfectedB.append(tl_pos)
                    str_join = str(tl_pos[0]) +","+ str(tl_pos[1])
                    noninfectedB.remove(tl_pos)
        
                if who_tr == 1 :
                    sgrid1[tr_pos[0]][tr_pos[1]] = 3
                    newInfectedB.append(tr_pos)
                    str_join = str(tr_pos[0]) +","+ str(tr_pos[1])
                    noninfectedB.remove(tr_pos)
        
                if who_bl == 1 :
                    sgrid1[bl_pos[0]][bl_pos[1]] = 3
                    newInfectedB.append(bl_pos)
                    str_join = str(bl_pos[0]) +","+ str(bl_pos[1])
                    noninfectedB.remove(bl_pos)
        
                if who_br == 1 :
                    sgrid1[br_pos[0]][br_pos[1]] = 3
                    newInfectedB.append(br_pos)
                    str_join = str(br_pos[0]) +","+ str(br_pos[1])
                    noninfectedB.remove(br_pos)
                    
            infectedB = newInfectedB
            allinfectedB.extend(newInfectedB)
            # print("newinfectedb",newInfectedB)
            # print("tick",tick1)
            if newInfectedB == []:
                canStillInfect = False
            newInfectedB=[]
        #p4
        enegry = 0
        for ni in noninfectedA:
            e1 = 9999999
            for i in allinfectedA:
                x_dist = ni[0] - i [0]
                x_dist = abs(x_dist)
                y_dist = ni[1] - i [1]
                y_dist = abs(y_dist)
                total_dis = y_dist + x_dist
                if total_dis < e1:
                    e1 = total_dis
            if e1 > enegry:
                enegry = e1
                
        
        p1 = ii
        p2 = -1
        if len(noninfectedA) == 0 :
            p2 = tick-1
        p3 = -1
        if len(noninfectedB) == 0 :
            p3 = tick1-1
        p4 = 0
        if p2 == -1:
            if enegry > 0 :
                p4 = enegry-1
            
        output = {
                    "room": room['room'],
                    "p1": p1,
                    "p2": p2,
                    "p3": p3,
                    "p4": p4
                  }
        res.append(output)
    return res


@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = parasite1(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
