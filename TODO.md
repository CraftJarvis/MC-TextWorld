# To-Dos: reasoning, long-horizon, multi-hop, knowledge dense, etc.

1. add a hyper-parameter `fix_action_space` to control the action space:
   a. the action space is fixed: 
   b. the action space is dynamic: this depends on the current inventory of the game
2. Wrapper the observation space: 
   a. the observation space now only has inventory ... 
   ```
   observation: {
    "inventory": {"oak_log":1, },
    "position": [0,0,0],
    "biome": "forest",
   }
   ```
   b. later we will add more, e.g., location, biome, etc.
3. check the rules of the game, especially the `mine` actions 
4. visualization 

ACTION SPACE:
##########################################
# 0 no_op                                #
# ---------------------------
# Mine Groups:
# 1 oak_log | 2 birch_log | 
# ---------------------------
# Craft Groups: 
# ---------------------------
# Smelt Groups: 
# ---------------------------
#########################################
Current Observation: 
#########################################
TASK: {diamond:1} --- STEP: 0/100 
#########################################
Input: 


5. Add task.py 

object-centric task 

```tasks.json 
[
   {
      "task_name": "obtain_1_diamond",
      "description": f"Obtain {1} {diamond} from {empty inventory}",
      "initial_inventory": {},
      "object": {"diamond":1},
   }
]
```

```group.json 
[
   "wood": ["wooden_pickaxe", "wooden_axe", ....]
   "stone": []
]
```

6. load test plans 

```plan.json 

```
