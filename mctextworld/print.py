print("Human: How to obtain stick?\nAI: The code for obtaining stick is as bellows:\ndef obtain_stick(inventory = {}):\n    mine({'log':2}, null); # action 1: mine 2 log without tool \n    craft({'planks':6}, {'log':2}, null); # action 2: craft 6 planks from 2 log\n    craft({'stick':2}, {'planks':1}, null); # action 3: craft 2 stick from 1 plank\n    return 'stick'\nHuman: I succeed on step 1.\nHuman: I succeed on step 2.\n")