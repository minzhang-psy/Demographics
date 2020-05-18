# **Demographics**
Collect Demographics Information. 
Information are based on NIH demographic report needed. 


## **Motivation**
In the past, our lab let participant fill out dempgraphic information by paper and assign RA manually enterd those information. Creating this this demographic collection survey mainly because our lab has cumputers disconnect from internet on purpous, so we are not able to use online survey. Ultimately, this program will significantly reduce human work and error. 

## **Information collected** 
|Header                     |Features  |
|---------------------------|----------|
|Time                       |Time of completed this survey |
|Study                      |Which study was participed, Selected from experiment folder's name|
|ID                         |Participant ID for current study|
|Hand                       |Which hand is participant's dominated one|
|Gender                     |Female, Male, other|
|Race                       |American Indian or Alaska Native, Asian, Black or African American, Native Hawaiian or other Pacific Islander, White, More than one race, Other, Prefer not to answer|
|Ethnicity                  |Hispanic or Latino, Not Hispanic or Latino, Prefer not to answer|
|School Year                |If Enrolled in College\nFreshman, Sophomore, Junior, Senior, Super Senior, Other|
|School Year explanation if choose other|If choose other in school year, type in..|
|School Year for not current student  |Some high school, High school, Some college, College, Some/all post-graduate|
|Sleep                      |Sleep time last night|
|Health                     |Current physical health compared to other people with same age on 5-point scale)

---

All information need to be selected inorder to submit answer. However, for Gender, Race, Ethnicity there are "Prefer not to answer option. 

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


