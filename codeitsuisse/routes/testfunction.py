import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def testFunction1(input):
    return str(input)
def stonk1(input):
    fin_res = []
    for test in input:
        energy = test['energy']
        capital = test['capital']
        
        
        timeline = test['timeline']
        # years = []
        
        backyears = energy//2
        farthest = 2037 - backyears 
        
        lowest_highest = {}
        for year in timeline:
            now = timeline[year]
            for stock in now:
                tickdata = now[stock]
                # print(stock)
                # print(year)
                # print(tickdata)
                if year == '2037':
                    lowestPrice = tickdata
                    highestPrice = tickdata
                    lowest_highest[stock] = [[year,lowestPrice],[year,highestPrice]]
                    
                else:
                    try:
                        record = lowest_highest[stock]
                    except:
                        lowestPrice = tickdata
                        highestPrice = tickdata
                        lowest_highest[stock] = [[year,lowestPrice],[year,highestPrice]]
                        record = lowest_highest[stock]
                    record_low = record[0]
                    record_high = record[1]
                    
                    if tickdata['price'] < record_low[1]['price']:
                        record_low = [year,tickdata]
                        
                    if tickdata['price'] > record_high[1]['price']:
                        record_high = [year,tickdata]
                    
                    lowest_highest[stock] = [record_low,record_high]
        
        percentageGain = {}
        
        for stock in lowest_highest:
            stockRow = lowest_highest[stock]
            lowPrice = stockRow[0][1]['price']
            highPrice = stockRow[1][1]['price']
            change = (100/lowPrice) * highPrice - 100
            change = round(change,5)
            # print(change)
            percentageGain[change] = stock
        
        inorder = list(percentageGain.keys())
        inorder = sorted(inorder,reverse=True)
        counter = 0
        totalTransac = []
        yearsToJump = []
        while capital > 0 and counter < len(inorder):
            stockToBuy = percentageGain[inorder[counter]]
            
            stockRecord = lowest_highest[stockToBuy]
            yearToBuy = stockRecord[0][0]
            qtyAvail = stockRecord[0][1]['qty']
            priceToBuy = stockRecord[0][1]['price']
            qty_bought = capital//priceToBuy
            yearToSell = stockRecord[1][0]
            capital = capital - (qty_bought*priceToBuy)
            # print(capital)
            transac = [stockToBuy,yearToBuy,qty_bought,yearToSell]
            if qty_bought != 0:
                totalTransac.append(transac)
            counter += 1
            
            if int(yearToBuy)not in yearsToJump:
                yearsToJump.append(int(yearToBuy))
            if int(yearToSell) not in yearsToJump:
                yearsToJump.append(int(yearToSell))
            # print(stockToBuy)
            # print(yearToBuy)
            # print(qtyAvail)
            # print(priceToBuy)
            # print(qty_bought)
            # print(yearToSell)
            # print('capitalleft',capital)
        
        yearsToJump = sorted(yearsToJump)
        
        res = []
        starting = 'j-2037-'+str(yearsToJump[0])
        
        
        res.append(starting)
        for index in range(0,len(yearsToJump)):
            year = yearsToJump[index]
            if index == 0:
                None
            else:
                tmp1 = 'j-'+str(yearsToJump[index-1])+"-"+str(yearsToJump[index])
                res.append(tmp1)
            for i in totalTransac:
                buyYear = i[1]
                whatToBuy = i[0]
                qty = i[2] 
                yearToSell = i[3]
                if buyYear == str(year):
                    tmp = "b-"+whatToBuy+"-"+str(qty)
                    # res.insert(len(res),tmp)
                    res.append(tmp)
                if yearToSell == str(year):
                    tmp = "s-"+whatToBuy+"-"+str(qty)
                    # res.insert(len(res),tmp)
                    res.append(tmp)
        

        fin_res.append(res)
    return fin_res


@app.route('/stonks', methods=['POST'])
def testFunction():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = stonk1(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result), {'Content-Type': 'application/json; charset=utf-8'}
