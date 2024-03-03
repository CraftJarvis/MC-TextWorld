# 🌏 MC-TextWorld: Plan in Minecraft TextWorld with free vision and action

### 📖 Introduction

This is the repository for the Minecraft TextWorld environment, which is a text-based game environment based on Minecraft game rules. 
We also test the planning performance of various agents based on Language Models in this environment.

### 📦 Installation
```
pip install -e mctextworld
```

### 📝 Usage

Run
```
cd mctextworld
python run_gui.py
```
to enter the mctextworld interface. The task name is default to "diamond_pickaxe". You can also choose a task by introduce the argument`--task_name`, the argument should be in a key in tasks.json and be defined in corresponding value.

Introduce the argument `--use_plan` to run the task by plan automaticly. If you enable this argument, the argument ```--task_name``` should be a key in plans.json and the plan should be defined in corresponding value.

### 📚 Data Source

The rules are based on the Minecraft game rules, and the data is collected from the Minecraft game. You can check the data source in the `data` folder. 

This is the recipe of `minecraft:cake`:
```json
{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "AAA",
    "BEB",
    "CCC"
  ],
  "key": {
    "A": {
      "item": "minecraft:milk_bucket"
    },
    "B": {
      "item": "minecraft:sugar"
    },
    "C": {
      "item": "minecraft:wheat"
    },
    "E": {
      "item": "minecraft:egg"
    }
  },
  "result": {
    "item": "minecraft:cake"
  }
}
```
We also check the plan according to the recipe.

### Terms of use
By using this service, users are required to agree to the following terms: The service is a research preview intended for non-commercial use only. It only provides limited safety measures and may generate offensive content. It must not be used for any illegal, harmful, violent, racist, or sexual purposes. **The service collects user dialogue data for future research.**
