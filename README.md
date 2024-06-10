# create_app_from_website
This is a depository that helps you create an application from almost any website that exists.

## Installation

You need to install these libraries for the code to work.

```sh
pip install PyQt5
pip install PyQtWebEngine
pip install python-dotenv
pip install pyinstaller
```

## usage

Copy the ```sample.env``` file and rename it to ```.env```. Then put the url to the website you want to make to an application in the WEBSITE_URL variable. after that you can run the ```main.py``` file and you should have an application of your website.

## Createn an exe

After you test if everything works by runing the ```main.py``` file you can run the ```create_exe.bat``` file in your terminal and it will automatically create your exe in the ```dist``` folder.

> Note: For some reason the exe only works inside the dist folder or some other folder you create in the root folder. So to be able to create multiple application i would recommend creating an apps folder where you put all your exe's inside. 