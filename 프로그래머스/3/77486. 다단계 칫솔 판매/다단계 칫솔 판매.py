def solution(enroll, referral, seller, amount):
    ref = dict()
    profits = dict()
    for a,b in zip(enroll,referral):
        ref[a] = b
        profits[a] = 0
    
    for seller, amount in zip(seller,amount):
        name = seller
        profit = amount * 100
        while name != "-":
            dividend = profit // 10
            if dividend < 1:
                profits[name] += profit
                break
            else:
                profits[name] += profit - dividend
                profit = dividend
                name = ref[name]
                
    return [profits[name] for name in enroll]