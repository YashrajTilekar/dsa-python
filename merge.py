def merge(L : list[int] ,p : int ,q : int ,r : int) -> None:
    """_summary_

    Args:
        L (list[int]): List of integers
        p (int): Index in L
        q (int): Index in L
        r (int): Index in L
    
    Post Condition:
        L[p...r] is sorted
    
    Pre Condition:
    0 <= p <= q < r < len(L)
    """
    N1 = q - p + 1  #length of L[p..q]
    N2 = r - q      # length of L[q+1 ... r]

    #Build Sub-list 1
    #L1[0..N1-1] = L[p...q]
    L1 = []
    i = 0
    while i < N1:
        L1.append(L[p + i])
        i = i + 1