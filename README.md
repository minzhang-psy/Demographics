# **Demographics**
Collect Demographics Information. 


## **Motivation**
In the past, our lab let participant fill out dempgraphic information by paper and assign RA manually enterd those information. Creating this this demographic collection survey mainly because our lab has cumputers disconnect from internet on purpous, so we are not able to use online survey. Ultimately, this program will significantly reduce human work and error. 

## **Information collected** 
|Header                     |Features  |
|---------------------------|----------|
|Time                       |Time of completed this survey |
|Study                      |Which study was participed, Selected from experiment folder's name|
|ID                         |Participant ID for current study|
|Hand                       |Which hand is participant's dominated one|
|Gender                     ||
|Race                       ||
|Ethnicity                  |      |
|School Year                | If Enrolled in College|
|School Year explanation if choose other|If choose other in school year|
|School Year for not current student    ||
|Sleep                      |Sleep time last night|
|Health                     ||
---

# Stand Alone Application

If a stand alone application is needed (without open python), run folloing code in terminal. This will create a folder with all the needed moudle, so that the script could be run without openning python editor. Or you can simply download the [Demographic](Demographics) folder. In the new folder created by this code, there is a [application with exec icon](Demographics/Demographics) which is the stand Alone Application you will be use.


### To convert the PY file to stand alone application 

Open Terminal, install auto-py-exe if you don't have this
```
pip install auto-py-to-exe
# Set up the working directory (add directory after cd 
cd
```
convert .py file to a stand alone file
```
auto-py-to-exe
```
In open window select script need to be convert. In Icon drop down menu add picture for icon (optional) 
Press CONVERT .PY TO .EXE at bottom. Output file is in the working directory 

#### If the Demographics EXE file can't open  
Go to get info for this file set default open through Terminal 
In terminal, type in code, with a space at the end, then type in file path  
```
		chmod +x 
```
Now you should be able to open this app! 


