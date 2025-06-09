# ReaL Reproduction

This repository contains the code and artifacts needed to reproduce the results of **Project ReaL** on EDA automation tasks.

---

## Overview

Our 7 B-parameter model was trained on two NVIDIA A100 GPUs using the ReaL training framework. We evaluated its ability to generate OpenROAD scripts across 27 distinct tasks.

---

## Model

* **Architecture:** 7 B parameters
* **Training hardware:** 2× NVIDIA A100 GPUs
* **Framework:** ReaL

---

## Inputs

* **Prompt file:** `prompt.json`
  Contains the 27 task specifications and corresponding prompt instructions.

---

## Outputs

* **`exported_scripts/`**
  A folder containing the model’s generated OpenROAD scripts.
  All scripts have been verified to run in the OpenROAD Docker environment (see ECE240 Lab 6).

---

## Notices

* You may see warnings when running OpenROAD scripts. These arise because we do not supply full chip‑ and process‑design files (our focus is on EDA functionality, not physical design).
* Our training corpus similarly omits full context; it emphasizes script functionality over complete design flows.

---

## Evaluation

1. **Functionality**

   * Tool: `detectoreval.py`
   * Result: 21/27 tasks passed → **77.7 % accuracy**
   * Detailed results are in `detect_results.json`.

2. **Quality**

   * Tool: `llm_judge_ability_test.py`
   * Result: 22/27 tasks passed → **81.5 % accuracy**
   * Raw judgments are in `llm_judge_result.txt`.

---

## Reproduction

To reproduce our results:

1. **Clone the repository**

   ```bash
   git clone https://github.com/Colin0vO/ReaL_reproduction.git
   cd ReaL_reproduction
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**
   Create a `.env` file in the project root with the following content:

   ```ini
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Run the full evaluation**

   ```bash
   bash run_all.sh
   ```

   This script will:

   * Generate OpenROAD scripts for all prompts
   * Execute `detectoreval.py` (outputs `detect_results.json`)
   * Execute `llm_judge_ability_test.py` (outputs `llm_judge_result.txt`)

After completion, inspect `detect_results.json` for functionality accuracy and `llm_judge_result.txt` for quality judgments.

---

## License & Contributions

Feel free to open issues or pull requests for questions, bug fixes, or feature improvements. All contributions are welcome!
