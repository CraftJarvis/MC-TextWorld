tool_dict = {
    "wool": "iron_axe",
    "white_wool": "iron_axe",
    "leather": "iron_axe",
    "beef": "iron_axe",
    "porkchop": "iron_axe",
    "mutton": "iron_axe",
    "chicken": "iron_axe",
    "string": "iron_axe",

    "logs": "iron_axe",
    "oak_log": "iron_axe",
    "birch_log": "iron_axe",
    "acacia_log": "iron_axe",
    "jungle_log": "iron_axe",

    "cobblestone": "wooden_pickaxe",
    "iron_ore": "stone_pickaxe",
    "gold_ore": "iron_pickaxe",
    "redstone": "iron_pickaxe",
    "diamond": "iron_pickaxe",
    "obsidian": "diamond_pickaxe"
}

ground_items = ['logs', 'oak_log', 'birch_log', 'acacia_log', 'jungle_log']

test_task_set = [
    'test_sand',
    'test_obsidian',
    'test_redstone',
    'test_iron',
    'test_diamond',
    'test_gold',
    "test_dig_down",
    'test_plains',
    'test_forest',
    'test_oak_log',
    'test_birch_log',
    'test_village',
    'test_sheep',
    'test_inv',
]

block_task_set = [
    'diorite', 
    'andesite', 
    'granite', 
    'coal', 
    'lapis_lazuli', 
    'iron_ore', 
    'gold_ore', 
    'cobblestone', 
    'gravel', 
    'oak_log',
    'birch_log',
    'acacia_log',
    'jungle_log',
]

wood_task_set = [
    'oak_wood',
    'oak_slab',
    'oak_planks',
    'oak_log',
    'oak_button',
    'oak_door',
    'oak_fence_gate',
    'oak_trapdoor',
    'oak_boat',
    'oak_sign',
    'wooden_shovel',
    'wooden_pickaxe',
    'wooden_axe',
    'wooden_hoe',
    'stick',
    'wooden_sword',
    'composter',
    'barrel',
    'crafting_table',
    'chest',
    'ladder',
    'bowl',
    # add 23-09-19
    'birch_wood',
    'birch_slab',
    'birch_planks',
    'birch_log',
    'birch_button',
    'birch_door',
    'birch_fence_gate',
    'birch_trapdoor',
    'birch_boat',
    'birch_sign',
    # Add 23-09-19 !
    'acacia_wood',
    'acacia_slab',
    'acacia_planks',
    'acacia_log',
    'acacia_button',
    'acacia_door',
    'acacia_fence_gate',
    'acacia_trapdoor',
    'acacia_boat',
    'acacia_sign',
    'jungle_wood',
    'jungle_slab',
    'jungle_planks',
    'jungle_log',
    'jungle_button',
    'jungle_door',
    'jungle_fence_gate',
    'jungle_trapdoor',
    'jungle_boat',
    'jungle_sign',
]

other_wood_task_set = [
    'birch_wood',
    'birch_slab',
    'birch_planks',
    'birch_log',
    'birch_button',
    'birch_door',
    'birch_fence_gate',
    'birch_trapdoor',
    'birch_boat',
    'birch_sign',
    'acacia_wood',
    'acacia_slab',
    'acacia_planks',
    'acacia_log',
    'acacia_button',
    'acacia_door',
    'acacia_fence_gate',
    'acacia_trapdoor',
    'acacia_boat',
    'acacia_sign',
    'jungle_wood',
    'jungle_slab',
    'jungle_planks',
    'jungle_log',
    'jungle_button',
    'jungle_door',
    'jungle_fence_gate',
    'jungle_trapdoor',
    'jungle_boat',
    'jungle_sign',
]

stone_task_set = [
    'stone_shovel',
    'stone_pickaxe',
    'stone_axe',
    'stone_hoe',
    'stone',
    'charcoal',
    'smoker',
    'stone_sword',
    'furnace',
]

iron_task_set = [
    'iron_pickaxe',
    'iron_shovel',
    'iron_sword',
    "iron_trapdoor",
    "iron_door",
    "iron_ingot",
    "shield",
    "bucket",
    "rail",
    "minecart",
    "smithing_table",
    "tripwire_hook",
    'chain',
    'iron_bars',
    # Add in 23-09-18
    "hopper",
    "iron_nugget",
    "iron_leggings",
    # "iron_chestplate",
    # "iron_boots",
    "heavy_weighted_pressure_plate",
    "blast_furnace",
    "shears",
    "stonecutter",
    "iron_hoe",
    "crossbow"
]

# total 10 colors
colorful_task_set = [
    'yellow_dye',
    'red_dye',
    'magenta_dye',
    'light_gray_dye',
    'pink_dye',
    'orange_dye',
    'blue_dye',
    'white_dye',
    'light_blue_dye', # blue_dye + white_dye
    'purple_dye', # blue_dye + red_dye
    # for wools 
    'yellow_wool',
    'red_wool',
    'magenta_wool',
    'light_gray_wool',
    'pink_wool',
    'orange_wool',
    'blue_wool',
    'light_blue_wool', # white_wool + light_blue_dye
    'purple_wool', # white_wool + purple_dye
    # for bed,
    'yellow_bed',
    'red_bed',
    'magenta_bed',
    'light_gray_bed',
    'pink_bed',
    'orange_bed',
    'blue_bed',
    'light_blue_bed', # white_bed + light_blue_dye
    'purple_bed', # white_bed + purple_dye
    # for carpet
    'yellow_carpet',
    'red_carpet',
    'magenta_carpet',
    'light_gray_carpet',
    'pink_carpet',
    'orange_carpet',
    'blue_carpet',
    'light_blue_carpet', # white_carpet + light_blue_dye
    'purple_carpet', # white_carpet + purple_dye
    # for banner
    # 'yellow_banner',
    # 'red_banner',
    # 'magenta_banner',
    # 'light_gray_banner',
    # 'pink_banner',
    # 'orange_banner',
    # 'blue_banner',
    # 'light_blue_banner', # white_banner + light_blue_dye
    # 'purple_banner', # white_banner + purple_dye
]

gold_task_set = [
    'golden_pickaxe',
    'golden_shovel',
    'golden_sword',
    'golden_hoe',
    'golden_axe',
    'golden_leggings',
    'golden_chestplate',
    'golden_boots',
    'golden_helmet',
    'golden_apple',
    'clock',
    'gold_nugget',
    'gold_ingot'
]

diamond_task_set = [
    'diamond_pickaxe',
    'diamond_shovel',
    'diamond_sword',
    'diamond_hoe',
    'diamond_axe',
    'diamond_chestplate',
    'diamond_leggings',
    'diamond_helmet',
    'diamond_boots',
    'diamond',
    'jukebox',
]

redstone_task_set = [
    'redstone',
    'piston',
    "redstone_torch",
    "redstone_block",
    "activator_rail",
    "compass",
    # "detector_rail",
    "dropper",
    "note_block",
]

armor_task_set = [
    'shield',
    'iron_sword',
    'iron_chestplate',
    'iron_boots',
    'iron_leggings',
    'iron_helmet',
    'diamond_sword',
    'diamond_helmet',
    'diamond_chestplate',
    'diamond_leggings',
    'diamond_boots',
    'golden_sword',
    'golden_helmet',
    'golden_chestplate',
    'golden_leggings',
    'golden_boots',
]

animals_task_set = [
    "cooked_chicken",
    "cooked_mutton",
    "cooked_porkchop",
    "cooked_beef",
    'leather_helmet',
    'leather_chestplate',
    'leather_leggings',
    'leather_boots',
    'white_wool',
    'white_bed',
    'white_carpet',
    'white_banner',
    'loom',
    'item_frame',
    'painting',
]

sheep_task_set = ['cooked_mutton', 'white_bed', 'painting']
cow_task_set = ['cooked_beef', 'paper', 'item_frame', 'leather_helmet', 'leather_chestplate', 'leather_leggings', 'leather_boots']
chicken_task_set = ['cooked_chicken', ]
pig_task_set = ['cooked_porkchop', ]
spider_task_set = ['loom', "crossbow"]

plant_task_set = [
    "book", # leather + sugar_cane 
    "paper", # leather + sugar_cane
]

other_task_set = [
    "glass",
    "glass_bottle",
    # "tripwire_hook",
]

steve_prompts = {
    "steve": [
        "break stone blocks"
    ],
    # wood-related
    "logs": [
        "chop down the tree"
    ],
    "birch_log": [
        "chop down the birch tree",
        "chop birch tree down",
        "break birch tree"
    ],
    "oak_log": [
        "chop down the oak tree", 
        "chop oak tree down",
        "break oak tree"
    ],
    "acacia_log": [
        "chop down the acacia tree", 
        "chop acacia tree down",
        "break acacia tree"
    ],
    # plants
    "apple": [
        "break leaves"
    ],
    "seeds": [
        "collect seeds"
    ],
    "flower": [
        "break a flower"
    ],
    "yellow_flower": [
        "break a flower",
        "break a yellow flower"
    ],
    "red_flower": [
        "break a flower",
        "break a red flower"
    ],
    "magenta_flower": [
        "break a flower",
        "break a magenta flower"
    ],
    "light_gray_flower": [
        "break a flower",
        "break a light gray flower"
    ],
    "pink_flower": [
        "break a flower",
        "break a pink flower"
    ],
    "orange_flower": [
        "break a flower",
        "break a orange flower"
    ],
    "blue_flower": [
        "break a flower",
        "break a blue flower"
    ],
    "white_flower": [
        "break a flower",
        "break a white flower"
    ],
    "dandelion": [ # yellow dye
        "break a flower",
        "break a dandelion flower",
        "break a yellow flower",
    ],
    "poppy": [ # red dye
        "break a flower",
        "break a poppy flower",
        "break a red flower",
    ],
    "allium": [ # magenta dye
        "break a flower",
        "break a allium flower",
        "break a magenta flower",
    ],
    "azure_bluet": [ # light gray dye
        "break a flower",
        "break a azure bluet flower",
        "break a gray flower",
    ],
    "pink_tulip": [ # pink dye
        "break a flower",
        "break a pink tulip flower",
        "break a pink flower",
    ],
    "red_tulip": [ # red dye
        "break a flower",
        "break a red tulip flower",
        "break a red flower",
    ],
    "white_tulip": [ # light gray dye
        "break a flower",
        "break a white tulip flower",
        "break a white flower",
    ],
    "orange_tulip": [ # orange dye
        "break a flower",
        "break a orange tulip flower",
        "break a orange flower",
    ],
    "oxeye_daisy": [ # light gray dye
        "break a flower",
        "break a oxeye daisy flower",
        "break a gray flower",
    ],
    "cornflower": [ # blue dye
        "break a flower",
        "break a cornflower flower",
        "break a blue flower",
    ],
    "lily_of_the_valley": [ # white dye
        "break a flower",
        "break a lily of the valley flower",
        "break a white flower", 
    ],
    "sugar_gane": [
        "break sugar cane"
    ],
    # blocks
    "sand": [
        "mine sand",
        "get sand"
    ],
    "cobblestone": [
        # "mine cobblestone",
        "dig down",
        # "dig hole",
        # "dig down and mine stone blocks" # --> not good, jump for a long time, and do not dig down 
    ],
    "stones": [
        # "mine cobblestone",
        "dig down",
        # "dig hole",
        # "dig down and mine stone blocks" # --> not good, jump for a long time, and do not dig down 
        "dig down, mine iron ore, and mine diamond"
    ],
    # ores
    "iron_ore": [
        # "break iron_ore blocks",
        # "get iron ore",
        # "dig down and mine iron ore"
        # "find iron_ore block and break it",
        "break iron_ore blocks", # --> good 
        "break iron blocks",
        # "dig down and mine iron ore",
        # "mine iron ore with pickaxe",
        # "break blocks with pickaxe",
        # "break iron blocks with pickaxe",
        # "explore",  --> not good
        # "break the stone blocks",
        "break stone, obtain iron ore",
        # "go explore" --> not good 
        # new for iron ore
        "break the stone blocks and mine iron ore"
    ],
    "gold_ore": [
        "break gold_ore blocks",
        # "mine gold ore", # ----> not good 
        # "mine golden blocks",
        # "mine ore",
        "break stone, obtain gold ore",
    ],
    "diamond": [
        # "mine diamond",
        # "mine diamond ore",
        # "mine diamond blocks",
        # ------------------------
        # "break diamond blocks",
        # "break stone, obtain diamond",
        "mine diamond ore",
        "break stone blocks, obtain diamond",
    ],
    "obsidian": [
        # "mine obsidian",
        "break obsidian blocks",
        "break black blocks",
        "break the chest",
        "break black stones, obtain obsidian",
        "break portal blocks",
    ],
    "redstone": [
        "mine redstone",
        "mine redstone ore",
        "mine redstone blocks",
        "break stone, obtain redstone",
    ],
    "dirt": [
        "get dirt", 
        "dig hole", 
        "dig dirt", 
        "gather a ton of dirt", 
        "collect dirt"
    ],
    "sand": [
        "get sand", 
        "dig sand", 
        "gather a ton of sand", 
        "collect sand"
    ],
    # animals
    "wool": [
        "kill sheep",
        "get wool",
        "kill animals"
    ],
    "white_wool": [
        "kill sheep",
        "get wool",
        "kill animals"
    ],
    "mutton": [
        "kill sheep",
        "get mutton",
        "kill animals"
    ],
    "leather": [
        "kill cow",
        "kill animals"
    ],
    "beef": [
        "kill cow",
        "get beef",
        "kill animals"
    ],
    "porkchop": [
        "kill pig",
        "get porkchop",
        "kill animals"
    ],
    "chicken": [
        "kill chicken",
        "get chicken",
        "kill animals"
    ],
    "string": [
        "kill spider",
        "combat spider",
    ]
}

jarvis_tasks = [
    {
        "group": "test",
        "task": "test_steve",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {
                0: {
                    "type": "diamond_pickaxe",
                    "quantity": 1
                }
            }
        },
        "task_obj": {
            "steve": 1
        }
    },
    {
        "group": "test",
        "task": "test_obsidian",
        "env": {
            "biome": "portal",
            "mobs": [],
            "init_inventory": {
                0: {
                    "type": "diamond_pickaxe",
                    "quantity": 1
                }
            }
        },
        "task_obj": {
            "obsidian": 1
        }
    },
    {
        "group": "test",
        "task": "test_sand",
        "env": {
            "biome": "desert",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "sand": 1
        }
    },
    {
        "group": "test",
        "task": "test_yellow_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "yellow_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_red_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "red_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_magenta_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "magenta_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_light_gray_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "light_gray_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_pink_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "pink_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_orange_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_blue_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "blue_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_white_flower",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "white_flower": 1
        }
    },
    {
        "group": "test",
        "task": "test_dig_down",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {
                0: {
                    "type": "iron_pickaxe",
                    "quantity": 1
                }
            }
        },
        "task_obj": {
            "stones": 128
        }
    },
    {
        "group": "test",
        "task": "test_plains",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "logs": 5
        }
    },
    {
        "group": "test",
        "task": "test_forest",
        "env": {
            "biome": "forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "logs": 5
        }
    },
    {
        "group": "test",
        "task": "test_oak_log",
        "env": {
            "biome": "forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_log": 5
        }
    },
    {
        "group": "test",
        "task": "test_birch_log",
        "env": {
            "biome": "forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_log": 5
        }
    },
    {
        "group": "test",
        "task": "test_village",
        "env": {
            "biome": "village",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "logs": 3
        }
    },
    {
        "group": "test",
        "task": "test_sheep",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "logs": 3
        }
    },
    {
        "group": "test",
        "task": "test_inv",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {
                1: {
                    "type": "cobblestone",
                    "quantity": 64
                },
                2: {
                    "type": "diamond",
                    "quantity": 64
                }
            }
        },
        "task_obj": {
            "logs": 3
        }
    },
    {
        "group": "test",
        "task": "test_diamond",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {
                0: {
                    "type": "iron_pickaxe",
                    "quantity": 1
                }
            }
        },
        "task_obj": {
            "diamond": 1
        }
    },
    {
        "group": "test",
        "task": "test_redstone",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {
                0: {
                    "type": "iron_pickaxe",
                    "quantity": 1
                }
            }
        },
        "task_obj": {
            "redstone": 1
        }
    },
    {
        "group": "test",
        "task": "test_gold",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {
                0: {
                    "type": "iron_pickaxe",
                    "quantity": 1
                }
            }
        },
        "task_obj": {
            "gold_ore": 1
        }
    },
    {
        "group": "test",
        "task": "test_iron",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_ore": 1
        }
    },
    {
        "group": "hand",
        "task": "painting",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "painting": 1
        }
    },
    {
        "group": "hand",
        "task": "white_banner",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "white_banner": 1
        }
    },
    {
        "group": "building",
        "task": "oak_wood",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_wood": 1
        }
    },
    {
        "group": "building",
        "task": "birch_wood",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_wood": 1
        }
    },
    {
        "group": "building",
        "task": "oak_slab",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_slab": 1
        }
    },
    {
        "group": "building",
        "task": "birch_slab",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_slab": 1
        }
    },
    {
        "group": "building",
        "task": "oak_planks",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_planks": 1
        }
    },
    {
        "group": "building",
        "task": "birch_planks",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_planks": 1
        }
    },
    {
        "group": "building",
        "task": "oak_log",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_log": 1
        }
    },
    {
        "group": "building",
        "task": "birch_log",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_log": 1
        }
    },
    {
        "group": "building",
        "task": "glass",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "glass": 1
        }
    },
    {
        "group": "building",
        "task": "stone",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stone": 1
        }
    },
    {
        "group": "tool",
        "task": "wooden_shovel",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "wooden_shovel": 1
        }
    },
    {
        "group": "tool",
        "task": "wooden_hoe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "wooden_hoe": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "bowl",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "bowl": 1
        }
    },
    {
        "group": "tool",
        "task": "wooden_axe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "wooden_axe": 1
        }
    },
    {
        "group": "tool",
        "task": "stone_shovel",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stone_shovel": 1
        }
    },
    {
        "group": "tool",
        "task": "wooden_pickaxe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "wooden_pickaxe": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "golden_apple",
        "env": {
            "biome": "forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_apple": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "gold_nugget",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "gold_nugget": 1
        }
    },
    {
        "group": "tool",
        "task": "clock",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "clock": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_pickaxe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_pickaxe": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_chestplate",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_chestplate": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_leggings",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_leggings": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_boots",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_boots": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_helmet",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_helmet": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_axe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_axe": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_hoe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_hoe": 1
        }
    },
    {
        "group": "tool",
        "task": "stone_pickaxe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stone_pickaxe": 1
        }
    },
    {
        "group": "tool",
        "task": "stone_axe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stone_axe": 1
        }
    },
    {
        "group": "tool",
        "task": "stone_hoe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stone_hoe": 1
        }
    },
    {
        "group": "tool",
        "task": "iron_pickaxe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_pickaxe": 1
        }
    },
    {
        "group": "tool",
        "task": "diamond_shovel",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_shovel": 1
        }
    },
    {
        "group": "tool",
        "task": "iron_shovel",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_shovel": 1
        }
    },
    {
        "group": "tool",
        "task": "diamond_pickaxe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_pickaxe": 1
        }
    },
    {
        "group": "tool",
        "task": "golden_shovel",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_shovel": 1
        }
    },
    {
        "group": "redstone",
        "task": "oak_button",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_button": 1
        }
    },
    {
        "group": "redstone",
        "task": "birch_button",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_button": 1
        }
    },
    {
        "group": "redstone",
        "task": "redstone_torch",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "redstone_torch": 1
        }
    },
    {
        "group": "redstone",
        "task": "tripwire_hook",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "tripwire_hook": 1
        }
    },
    {
        "group": "redstone",
        "task": "iron_trapdoor",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_trapdoor": 1
        }
    },
    {
        "group": "redstone",
        "task": "iron_door",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_door": 1
        }
    },
    {
        "group": "redstone",
        "task": "redstone_block",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "redstone_block": 1
        }
    },
    {
        "group": "redstone",
        "task": "oak_door",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_door": 1
        }
    },
    {
        "group": "redstone",
        "task": "birch_door",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_door": 1
        }
    },
    {
        "group": "redstone",
        "task": "oak_fence_gate",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_fence_gate": 1
        }
    },
    {
        "group": "redstone",
        "task": "birch_fence_gate",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_fence_gate": 1
        }
    },
    {
        "group": "redstone",
        "task": "oak_trapdoor",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_trapdoor": 1
        }
    },
    {
        "group": "redstone",
        "task": "birch_trapdoor",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_trapdoor": 1
        }
    },
    {
        "group": "brewing",
        "task": "cauldron",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "cauldron": 1
        }
    },
    {
        "group": "brewing",
        "task": "glass_bottle",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "glass_bottle": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "diamond",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond": 1
        }
    },
    {
        "group": "decoration",
        "task": "jukebox",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jukebox": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "stick",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stick": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "gold_ingot",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "gold_ingot": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "paper",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "paper": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "iron_ore",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_ore": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "iron_ingot",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_ingot": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "charcoal",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "charcoal": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "book",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "book": 1
        }
    },
    {
        "group": "miscellaneous",
        "task": "bucket",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "bucket": 1
        }
    },
    {
        "group": "transportation",
        "task": "rail",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "rail": 1
        }
    },
    {
        "group": "transportation",
        "task": "oak_boat",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_boat": 1
        }
    },
    {
        "group": "transportation",
        "task": "birch_boat",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_boat": 1
        }
    },
    {
        "group": "transportation",
        "task": "minecart",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "minecart": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "cooked_chicken",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "chicken"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "cooked_chicken": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "cooked_mutton",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "cooked_mutton": 1
        }
    },
    {
        "group": "animals",
        "task": "white_wool",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "white_wool": 1
        }
    },
    {
        "group": "animals",
        "task": "white_bed",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "white_bed": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "cooked_porkchop",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "pig"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "cooked_porkchop": 1
        }
    },
    {
        "group": "foodstuffs",
        "task": "cooked_beef",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "cooked_beef": 1
        }
    },
    {
        "group": "occupation_block",
        "task": "loom",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "spider"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "loom": 1
        }
    },
    {
        "group": "occupation_block",
        "task": "smithing_table",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "smithing_table": 1
        }
    },
    {
        "group": "occupation_block",
        "task": "barrel",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "barrel": 1
        }
    },
    {
        "group": "occupation_block",
        "task": "composter",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "composter": 1
        }
    },
    {
        "group": "occupation_block",
        "task": "smoker",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "smoker": 1
        }
    },
    {
        "group": "equipment",
        "task": "shield",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "shield": 1
        }
    },
    {
        "group": "decorations",
        "task": "item_frame",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "item_frame": 1
        }
    },
    {
        "group": "equipment",
        "task": "leather_helmet",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "leather_helmet": 1
        }
    },
    {
        "group": "equipment",
        "task": "leather_chestplate",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "leather_chestplate": 1
        }
    },
    {
        "group": "equipment",
        "task": "leather_leggings",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "leather_leggings": 1
        }
    },
    {
        "group": "equipment",
        "task": "leather_boots",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "cow"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "leather_boots": 1
        }
    },
    {
        "group": "equipment",
        "task": "iron_helmet",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_helmet": 1
        }
    },
    {
        "group": "combat",
        "task": "wooden_sword",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "wooden_sword": 1
        }
    },
    {
        "group": "combat",
        "task": "stone_sword",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "stone_sword": 1
        }
    },
    {
        "group": "combat",
        "task": "golden_sword",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "golden_sword": 1
        }
    },
    {
        "group": "combat",
        "task": "iron_sword",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_sword": 1
        }
    },
    {
        "group": "combat",
        "task": "diamond_sword",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_sword": 1
        }
    },
    {
        "group": "decoration",
        "task": "chain",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "chain": 1
        }
    },
    {
        "group": "decoration",
        "task": "crafting_table",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "crafting_table": 1
        }
    },
    {
        "group": "decoration",
        "task": "chest",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "chest": 1
        }
    },
    {
        "group": "decoration",
        "task": "furnace",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "furnace": 1
        }
    },
    {
        "group": "decoration",
        "task": "iron_bars",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_bars": 1
        }
    },
    {
        "group": "decoration",
        "task": "ladder",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "ladder": 1
        }
    },
    {
        "group": "decoration",
        "task": "oak_fence",
        "env": {
            "biome": "oak_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "oak_fence": 1
        }
    },
    {
        "group": "decoration",
        "task": "birch_fence",
        "env": {
            "biome": "birch_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "birch_fence": 1
        }
    },
    # Add on 2023/09/18
    {
        "group": "equipment",
        "task": "diamond_helmet",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_helmet": 1
        }
    },
    {
        "group": "equipment",
        "task": "diamond_leggings",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_leggings": 1
        }
    },
    {
        "group": "equipment",
        "task": "diamond_chestplate",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_chestplate": 1
        }
    },
    {
        "group": "equipment",
        "task": "diamond_boots",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_boots": 1
        }
    },
    {
        "group": "tool",
        "task": "diamond_hoe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_hoe": 1
        }
    },
    {
        "group": "tool",
        "task": "diamond_axe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "diamond_axe": 1
        }
    },
    {
        "group": "iron",
        "task": "hopper",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "hopper": 1
        }
    },
    {
        "group": "iron",
        "task": "iron_nugget",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_nugget": 1
        }
    },
    {
        "group": "iron",
        "task": "iron_leggings",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_leggings": 1
        }
    },
    {
        "group": "iron",
        "task": "iron_chestplate",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_chestplate": 1
        }
    },
    {
        "group": "redstone",
        "task": "piston",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "piston": 1
        }
    },
    {
        "group": "iron",
        "task": "heavy_weighted_pressure_plate",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "heavy_weighted_pressure_plate": 1
        }
    },
    {
        "group": "iron",
        "task": "shears",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "shears": 1
        }
    },
    {
        "group": "redstone",
        "task": "activator_rail",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "activator_rail": 1
        }
    },
    {
        "group": "redstone",
        "task": "compass",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "compass": 1
        }
    },
    # {
    #     "group": "iron",
    #     "task": "stonecutter",
    #     "env": {
    #         "biome": "plains",
    #         "mobs": [],
    #         "init_inventory": {}
    #     },
    #     "task_obj": {
    #         "stonecutter": 1
    #     }
    # },
    # {
    #     "group": "redstone",
    #     "task": "detector_rail",
    #     "env": {
    #         "biome": "plains",
    #         "mobs": [],
    #         "init_inventory": {}
    #     },
    #     "task_obj": {
    #         "detector_rail": 1
    #     }
    # },
    {
        "group": "tool",
        "task": "iron_hoe",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_hoe": 1
        }
    },
    {
        "group": "tool",
        "task": "crossbow",
        "env": {
            "biome": "plains",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 10,
                    "mob_name": "spider"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "crossbow": 1
        }
    },
    {
        "group": "equipment",
        "task": "iron_boots",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "iron_boots": 1
        }
    },
    # Add the acacia groups
    {
        "group": "building",
        "task": "acacia_wood",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_wood": 1
        }
    },
    {
        "group": "building",
        "task": "acacia_slab",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_slab": 1
        }
    },
    {
        "group": "building",
        "task": "acacia_planks",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_planks": 1
        }
    },
    {
        "group": "building",
        "task": "acacia_log",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_log": 1
        }
    },
    {
        "group": "redstone",
        "task": "acacia_button",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_button": 1
        }
    },
    {
        "group": "redstone",
        "task": "acacia_door",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_door": 1
        }
    },
    {
        "group": "redstone",
        "task": "acacia_fence_gate",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_fence_gate": 1
        }
    },
    {
        "group": "redstone",
        "task": "acacia_trapdoor",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_trapdoor": 1
        }
    },
    {
        "group": "transportation",
        "task": "acacia_boat",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_boat": 1
        }
    },
    {
        "group": "decoration",
        "task": "acacia_fence",
        "env": {
            "biome": "savanna",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "acacia_fence": 1
        }
    },
    {
        "group": "building",
        "task": "jungle_wood",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_wood": 1
        }
    },
    {
        "group": "building",
        "task": "jungle_slab",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_slab": 1
        }
    },
    {
        "group": "building",
        "task": "jungle_planks",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_planks": 1
        }
    },
    {
        "group": "building",
        "task": "jungle_log",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_log": 1
        }
    },
    {
        "group": "redstone",
        "task": "jungle_button",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_button": 1
        }
    },
    {
        "group": "redstone",
        "task": "jungle_door",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_door": 1
        }
    },
    {
        "group": "redstone",
        "task": "jungle_fence_gate",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_fence_gate": 1
        }
    },
    {
        "group": "redstone",
        "task": "jungle_trapdoor",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_trapdoor": 1
        }
    },
    {
        "group": "transportation",
        "task": "jungle_boat",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_boat": 1
        }
    },
    {
        "group": "decoration",
        "task": "jungle_fence",
        "env": {
            "biome": "jungle",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "jungle_fence": 1
        }
    },
    {
        "group": "redstone",
        "task": "redstone",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "redstone": 1
        }
    },
    {
        "group": "redstone",
        "task": "dropper",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "dropper": 1
        }
    },
    {
        "group": "redstone",
        "task": "note_block",
        "env": {
            "biome": "plains",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "note_block": 1
        }
    },
    # Add 23/09/21 -> colorful tasks
    {
        "group": "colorful",
        "task": "yellow_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "yellow_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "red_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "red_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "magenta_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "magenta_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_gray_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "light_gray_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "pink_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "pink_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "orange_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "blue_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "blue_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "white_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "white_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_blue_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "light_blue_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "purple_dye",
        "env": {
            "biome": "flower_forest",
            "mobs": [],
            "init_inventory": {}
        },
        "task_obj": {
            "purple_dye": 1
        }
    },
    {
        "group": "colorful",
        "task": "yellow_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "yellow_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "red_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "red_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "magenta_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "magenta_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_gray_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_gray_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "pink_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "pink_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "orange_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "blue_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "blue_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_blue_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_blue_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "purple_wool",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "purple_wool": 1
        }
    },
    {
        "group": "colorful",
        "task": "yellow_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "yellow_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "red_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "red_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "magenta_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "magenta_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_gray_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_gray_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "pink_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "pink_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "orange_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "orange_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "blue_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "blue_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_blue_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_blue_bed": 1
        }
    },
    {
        "group": "colorful",
        "task": "purple_bed",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "purple_bed": 1
        }
    },
    {
        "group": "animals",
        "task": "white_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "white_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "yellow_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "yellow_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "red_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "red_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "magenta_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "magenta_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_gray_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_gray_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "pink_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "pink_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "orange_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "blue_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "blue_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_blue_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_blue_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "purple_carpet",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "purple_carpet": 1
        }
    },
    {
        "group": "colorful",
        "task": "yellow_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "yellow_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "red_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "red_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "magenta_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "magenta_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_gray_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_gray_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "pink_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "pink_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "orange_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "orange_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "blue_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "blue_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "light_blue_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "light_blue_banner": 1
        }
    },
    {
        "group": "colorful",
        "task": "purple_banner",
        "env": {
            "biome": "flower_forest",
            "mobs": [
                {
                    "range_x": [
                        -20,
                        20
                    ],
                    "range_y": [
                        5,
                        10
                    ],
                    "range_z": [
                        -20,
                        20
                    ],
                    "number": 20,
                    "mob_name": "sheep"
                }
            ],
            "init_inventory": {}
        },
        "task_obj": {
            "purple_banner": 1
        }
    }
]

import json
with open("/scratch/hekaichen/workspace/mc-textworld/mctextworld/jarvis_task.json", "w") as j:
    json.dump(jarvis_tasks, j)



# default_summon_config = {
#     'range_x': [-20, 20], 
#     'range_y': [5, 10], 
#     'range_z': [-20, 20], 
#     'number': 10
# }

# def build_env_config(task):
#     if 'env' in task.keys():
#         task_env_config = task['env']
#         if 'biome' in task_env_config.keys():
#             pass

# import json
# with open('../assets/tag_items.json', 'r') as f:
#     tag_items = json.load(f)

# with open('../assets/spawn.json', 'r') as f:
#     spawn = json.load(f)

# seeds = {}
# for s in spawn:
#     if s['biome'] not in seeds.keys():
#         seeds[s['biome']] = []
#     seeds[s['biome']].append(s['seed'])
        

# import yaml
# import random 

# def build_env_yaml(env_config):
#     with open('../global_configs/jarvis-1/env_base.yaml', 'r') as f:
#         env_yaml = yaml.load(f, Loader=yaml.FullLoader)
#     # biome -> seed: 12345, close_ended: True
#     if env_config["biome"]:
#         env_yaml['candidate_preferred_spawn_biome'] = [env_config["biome"]]
#         if env_config["biome"] in seeds.keys():
#             env_yaml['close_ended'] = True
#             env_yaml['seed'] = random.choice(seeds[env_config["biome"]])

#     # mobs -> summon_mobs
#     if env_config["mobs"]:
#         env_yaml['summon_mobs'] = env_config["mobs"]

#     # init_inventory -> init_inventory
#     if env_config["init_inventory"]:
#         for k,v in env_config["init_inventory"].items():
#             env_yaml['init_inventory'][k] = v

#     with open('../global_configs/envs/jarvis.yaml', 'w') as f:
#         yaml.dump(env_yaml, f, sort_keys=False)
    
#     return env_yaml

# # check two env yaml is same or not
# def check_env_change(env_1, env_2):
#     for key in env_1.keys():
#         if key == 'seed':
#             continue
#         if key not in env_2.keys():
#             return True
#         if env_1[key] != env_2[key]:
#             return True
#     return False

# if __name__ == '__main__':
#     # BUILD plans.json
#     # plans = {}
#     # for task in jarvis_tasks:
#     #     plans[task['task']] = task['plan']
#     # with open('../assets/plans.json', 'w') as f:
#     #     json.dump(plans, f, indent=4)
    
#     # TODO: ADD timeout params
#     # TODO: ADD Biome Support
#     # BUILD TASKS JSON
#     # for t in jarvis_tasks:
#     #     # if 'plan' in t.keys():
#     #     #     t.pop('plan')

#     #     # t['task_obj'] = {t["task"]: 1}
        
#     #     t['env'] = {
#     #         'biome': 'plains',
#     #         'mobs': [],
#     #         'init_inventory': {}
#     #     }

#     #     if t['task'] in sheep_task_set:
#     #         default_summon_config['mob_name'] = 'sheep'
#     #         t['env']['mobs'].append(default_summon_config.copy())
#     #     elif t['task'] in cow_task_set:
#     #         default_summon_config['mob_name'] = 'cow'
#     #         t['env']['mobs'].append(default_summon_config.copy())
#     #     elif t['task'] in chicken_task_set:
#     #         default_summon_config['mob_name'] = 'chicken'
#     #         t['env']['mobs'].append(default_summon_config.copy())
#     #     elif t['task'] in pig_task_set:
#     #         default_summon_config['mob_name'] = 'pig'
#     #         t['env']['mobs'].append(default_summon_config.copy())
#     #     elif t['task'] in spider_task_set:
#     #         default_summon_config['mob_name'] = 'spider'
#     #         t['env']['mobs'].append(default_summon_config.copy())

#     # import json
#     # with open('tasks.json', 'w') as f:
#     #     json.dump(jarvis_tasks, f, indent=4)

#     # BUILD ENV CONFIG to jarvis.yaml
#     # env_config = jarvis_tasks[0]['env']
#     # builded_yaml = build_env_yaml(env_config)
#     # print(builded_yaml)

#     for t in animals_task_set:
#         print(t)
