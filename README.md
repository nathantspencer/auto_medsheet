# auto_medsheet
auto_medsheet is a tool for nursing students and others who need to quickly grab information for name brand drugs from a drug reference such as PDR.net (which is the source of information used for this tool).

Using auto medsheet is simple. Call the script with the name of the file you'd like to create as the first argument, and the name brand drugs you'd like to grab information on as subsequent arguments. Call the line below...

`$ python auto_medsheet.py fileToWrite xanax abilify ablivar`

And the a document like this will be created in your auto_medsheet directory!

![alt text](https://github.com/nathantspencer/auto_medsheet/blob/master/example.png?raw=true "Viola!")

## Additional Info
All of the dependencies for auto_medsheet can be `pip install`ed on Unix-based systems. The table setup for output is specific to the needs of nursing students local to me, but can be changed easily within the script.

If you'd like to use the tool but are unsure of how to adapt it your purposes, feel free to contact me at nathantspencer@gmail.com and I can help you get started.
