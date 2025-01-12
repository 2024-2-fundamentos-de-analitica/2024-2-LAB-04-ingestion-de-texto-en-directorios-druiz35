# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import pandas as pd
from pathlib import Path
import os

# Path files
train = Path(__file__).resolve().parents[1].joinpath("./files/input/train")
test = Path(__file__).resolve().parents[1].joinpath("./files/input/test")


def create_csv_from_dataset(path, output_filename):
    # Create csv
    output_dir_path = Path(__file__).resolve().parents[1].joinpath("./files/output")
    output_file_path = output_dir_path.joinpath(f"./{output_filename}.csv")
    
    # Create output directory
    try:
        os.mkdir(output_dir_path)
    except:
        pass
    with open(output_file_path, "w") as f:
        f.write("phrase,target\n")

    # Feed csv
    for dir_name in os.listdir(path):
        files_path = path.joinpath(dir_name)
        files = os.listdir(files_path)
        for file in files:
            current_txt_file_path = files_path.joinpath(file)
            with open(current_txt_file_path, "r") as f:
                line = f.readlines()[0]
            
            with open(output_file_path, "a") as f:
                f.write(f"\"{line}\",\"{dir_name}\"\n")


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```
    """
    create_csv_from_dataset(train, "train_dataset")
    create_csv_from_dataset(test, "test_dataset")

pregunta_01()