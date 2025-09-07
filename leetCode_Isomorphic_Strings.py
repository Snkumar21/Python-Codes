class Solution: 
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        mapping_st, mapping_ts = {}, {}
        for c1, c2 in zip(s, t):
            if c1 in mapping_st:
                if mapping_st[c1] != c2:
                    return False
            else:
                if c2 in mapping_ts:
                    return False
                mapping_st[c1] = c2
                mapping_ts[c2] = c1
        return True