This is a repo of Our Project ReaL on EDA's result.

Our Model is trained on 2 piece of Nvidia A100 using ReaL training framework. 

We run experiment on 27 tasks, 
The corresponding prompt is prompt.json file.

exported_scripts is folder of our 7b model scripts output. They have been verified runnable under OpenRoad Docker (see ECE260 Lab 0). 
But as we lack Process and Chip setting(not our main objective in project, we focusing on functionality of EDA desgin), we cannot verify correctness manually, we using llm_judge_ability_test.py to judge abilities. 
You might see warnings when executing them this is because we can't desgin chips and process for each prompt.

