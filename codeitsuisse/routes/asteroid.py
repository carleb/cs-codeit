import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def asteroid1(var1):
    final_res = []
    for test1 in var1:
# test1 = "CCCAAABBBAAACCC"

    
        possible_start = []
    
    
        for i in range(0,len(test1)-1):
            current = test1[i]
            nextt = test1[i+1]
            # print(current)
            # print(nextt) 
            if current == nextt:
                possible_start.append(i)
        
        possible_start = possible_start[1:]
        possible_start = possible_start[:len(possible_start)-1]
        
        test_res = {}
        max_score = 0
        for origin in possible_start:
        # origin = 7
        
            left = test1[:origin]
            left = list(left)
            left.reverse()
            right = test1[origin:]
            right= list(right)
            
            total_score = 0
            round_counter = 0
            
            mutiplier_set = {}
            for i in range(0,len(left)):
                astro = left[i]
                if astro not in mutiplier_set:
                    mutiplier_set[astro] = [i]
                else:
                    mutiplier_set[astro].append(i)
                    
            for i in range(0,len(right)):
                astro = right[i]
                if astro not in mutiplier_set:
                    mutiplier_set[astro] = [i]
                else:
                    mutiplier_set[astro].append(i)
                    
            for astro in mutiplier_set:
                unsorted = mutiplier_set[astro] 
                # print(unsorted)
                sort = sorted(unsorted)
                
                # print(sort)
                
                splited_set = {}
                list_id = 0
                prev = sort[0]
                for i in sort:
                    if (i - prev) <= 1:
                        if list_id not in splited_set:
                            splited_set[list_id] = [i]
                        else:
                            splited_set[list_id].append(i)
                    else:
                        list_id += 1
                        splited_set[list_id] = [i]
                    prev = i
                mutiplier_set[astro] =  splited_set
                
            for astro_type in mutiplier_set:
                streaks = mutiplier_set[astro_type]
                for streak in streaks:
                    streak_len = len(streaks[streak])
                    if streak_len <=6:
                        streak_mutiplier = 1
                    elif streak_len >= 10:
                        streak_mutiplier = 2
                    else:
                        streak_mutiplier = 1.5
                    total_score += (streak_len*streak_mutiplier)
        
            if total_score > max_score:
                max_score = total_score
            
            if max_score not in test_res:
                test_res[max_score] = []
            test_res[max_score].append(origin)
            
        ## geting origin
        best_origins = test_res[max_score]
        
    
        res_origin = best_origins[(len(best_origins))//2] ## any of the best origin is okay
        # print("origin",res_origin)
        # print("score",max_score)
        into_final_res = {
                        "input": test1,
                        "score": max_score,
                        "origin": res_origin
                      }
        final_res.append(into_final_res)                    
    return final_res



def testFunction1(input):
    return str(input)


@app.route('/asteroid', methods=['POST'])
def asteroid():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = asteroid1(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result)


