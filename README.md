# gdp (Grundlagen der Programmierung) Wintersemester 2025/26

This repository contains Jupyter notebooks and example data for my
course *Grundlagen der Programmierung* at Graz University. All notebooks are 
in German.

The number of notebooks will grow during the semester. So run `git pull` before each class.

## Usage

To use the notebooks make sure you have these programs installed:

  * Python version 3. 
  * Jupyter. Install it via pip or conda (`pip install --user jupyter` or 
    `conda install jupyter` if you use Conda/Anaconda)
  * I suggest to also install jupyterlab, which is a more modern version of 
    `jupyter notebook` (which was installed automatically with `jupyter`): 
    `pip install --user jupyterlab` or `conda install jupyterlab`.

Clone the repository from GitHub:

```bash
git clone https://github.com/gvasold/gdp25.git
```

Then change into `gdp25` directory and start the Jupyter server:

```bash
cd gdp
jupyter-lab
```


or, if you prefer jupyter notebook:

```bash
jupyter notebook
```

This will bring up your browser and will show you the contents of the `gdp` 
directory.

All notebooks have numbers (like `01_datentypen.ipynb`). I suggest to use the 
notebooks in this order. Notebooks are organized by topics. Each topic has i
its own folder. Start with folder `grundlagen`.

## License

All notebooks are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0).
 
