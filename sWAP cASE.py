#!/usr/bin/env python
# coding: utf-8

# In[2]:


def swap_case(s):
    con_s = [i.upper() if i.islower() else i.lower() for i in s]
    upd_s = "".join(con_s)
    return upd_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

