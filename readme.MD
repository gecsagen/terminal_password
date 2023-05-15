# Console password generator  
### Install  
**1. Clone the repository:**  
`git clone https://github.com/gecsagen/terminal_password.git`  

**2. Creating a virtual environment**  
```bash  
    cd terminal_password  
    python3 -m venv .venv  

```  
**3. Activate the virtual environment**  

`source .venv/bin/activate  `  

**4. Installing dependencies**  

`pip install -r requirements.txt`  

**5. Launching the application**  

`python3 main.py --long 14 --quantity 5 --no-numbers`  

*This example will generate 5 passwords of 14 characters each without using numbers.  
Here is a complete reference on the possible arguments:*
**[-h]** - reference  
**[--long LONG]**- password length  
**[--quantity QUANTITY]** - number of passwords  
**[--lowercase | --no-lowercase]** - use / do not use lowercase letters  
**[--capital | --no-capital]** - use / do not use capital letters  
**[--numbers | --no-numbers] **- use / do not use numbers  
**[--special | --no-special]** - use / do not use special characters  
**[--buffer | --no-buffer]**  - copy generated passwords to clipboard  
**[--config CONFIG]** - Use config with generation settings  

Here is an example config file:  
```bash
[settings]
long = 15
quantity = 10
lowercase = True
capital_letters = True
numbers = True
special_characters = True
buffer = False
```
**Note:**
> *If you specified a config file, the program will ignore other flags and all settings will be taken from the config file. If the config file does not exist or it is not a valid bcdct use the default settings*

