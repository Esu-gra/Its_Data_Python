'''
Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.
'''

def merge_intervals(intervals:list[list[int]])->list:
    if not intervals:
        return []
    intervals.sort()
    fusi:list=[intervals[0]]
    for l in intervals[1:]:
        if fusi[-1][1]>=l[0]:
             fusi[-1][1]=max(fusi[-1][1],l[1])
           
        else:
             fusi.append(l)
           
    return fusi

    


    
        
  
   

        
        

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals ))
