## ETL Process (mvp)


### Description
***
In this project I performed the automation of extraction, transformation and load weekly of sales data from Tienda Nube using Python.
  


### Use
***
To use this resource you will need define the following environment variables:

* "**USER**" *(Tienda Nube user)*
* "**TN_PASSWORD**" *(user password)*
* "**ORIGIN_DIR**" *(it will be the csv file path that will download on your pc)*
* "**DESTINY_DIR_PROJECT**" *(it will be the directory of choice to save the csv)*
* "**FILE_OUTPUT**" *(it will be the file path on the directory selected)*

and run the command:
~~~ 
pip install -r requirements.txt 
~~~

to install all necessary to run the project. In addition to importing the Python **shutil** and **os** modules.

I hope it serves you!