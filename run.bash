chmod +x detector_input_jsonal_helper.py
./detector_input_jsonal_helper.py exported_scripts/ -o responses.json

python detectoreval.py 
python merge_json.py prompt.json responses.json paired.json
python llm_judged_ability_test.py paired.json > llm_judge_result.txt