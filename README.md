# **FREYR**: A **F**ramework for **R**ecognizing and **E**xecuting **Y**our **R**equests

This repository contains the code for "FREYR: A Framework for Recognizing and Executing Your Requests".

## Setting it up
Clone this repository locally:
```bash
git clone https://github.com/gallorob/freyr.git && cd freyr
```
Install requirements with pip:
```bash
pip install -r requirements.txt
```

Install [Ollama](https://ollama.com/) on your machine then run `get_llms.sh` to make sure you have all the models required to replicate our results.

And you're ready to go 😄
## Using FREYR
You can replicate the results from our paper by running the different configurations available in `run_experiments.sh`. You can then use the different notebooks (`.ipynb`) to analyze the results.

## Citing
If you find this work useful, consider citing it as:
* The arXiv preprint:
```bibtex
@article{gallotta2025freyr,
	title        = {{FREYR}: A {F}ramework for {R}ecognizing and {E}xectuing {Y}our {R}equests},
	author       = {Gallotta, Roberto and Liapis, Antonios and Yannakakis, Georgios N.},
	year         = 2025,
	journal      = {arXiv preprint arXiv:2501.2501.12423}
}
```
* Or this Github repository:
```bibtex
@misc{freyr,
  title = {FREYR: A Framework for Recognizing and Executing Your Requests Without Tools},
  author = {Roberto Gallotta, Antonios Liapis, Georgios N. Yannakakis},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/gallorob/freyr}},
  year={2024}
}
``` 
