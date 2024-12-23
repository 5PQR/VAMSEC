# VAMSEC

This is a python tool that looks for specific code in Virtamate files (.cs files inside .var files, and other loose .cs files).

It can be used as a general tool to scan for specific things in virtamate mods code, in any folder. Both the folder and the searched for string can be modified in the config file. 

For .dll files, you'll have to manually decompile them first like with [ILSpy](https://github.com/icsharpcode/ILSpy). You can drag a DLL in ILSpy, right-click on the dll in it and click Save Code. Then you can run the tool on the folder that has that code.

***For other devs, feel free to fork, reuse or repurpose this script.***


## DECEMBER 24 v2
[YOUTUBE DEMO](https://www.youtube.com/watch?v=SDddjyxhLPY)![](https://i.imgur.com/PGzGGjU.jpeg)


[DOWNLOAD](https://github.com/5PQR/VAMSEC/releases/download/December24v2/SPQR.VAMSEC.December24v2.zip)

Tool updated for better results formatting and to speed it up. 

Tool now also has a list of whitelisted strings which when found close to the searched text will get highlighted as green.

Each result line will be marked as red or green depending if any whitelisted terms are found. This makes reading the results a little easier.


## DECEMBER 24 v1

In December 2024 a security issue was reported and made public regarding the misuse of a certain function in Virtamate files. Since the security breach is public and many people know about it, I made this tool for my patreon supporters to be able to check vars to prevent having issues due to this security breach.

This script will look for that function and highlight the cases found where it's used. There are many plugins that use it legitimately, to open important links and they can be easily identified (links to patreon, github, youtube etc). If you notice results that don't fit in this category (links you recognize), or they're in a var that's strange to you, it's best to avoid using it until some fix is deployed by the virtamate team. You can also report it either here, or on my patreon https://patreon.com/spqr_aeternum , or on the vam discord to the people there, so that somebody can take a closer look at it and inform others in case there's a problem with that var.


## HOW TO USE
1. Download the version you want, recommended the most recent
2. Extract archive anywhere, but make sure the path DOESN'T have white spaces in it. Long story. "C:/New Folder" won't work, "C:/New_Folder" or C:/"NewFolder" will work.
3. Right click and Edit the **config.py**  file in any text editor. Put the path to your VAM folder like in the example with two "\\\\" between folders. You can also put any folder that you want to check. The script will look everywhere in that folder for vars and cs files.
4. Run  **VAMSec.December24.bat** and wait. Depending on your VAM size, it might take a long time! Maybe even hours for people with TB worth of mods

## RESULTS
Once finished, the script will generate a results.html file in the same folder. And it will also automatically open it in your default browser, like in the youtube video above.

There will be a table with all the results found. On the third column if you see links such as patreon, github, youtube, vamhub, then those should be ok. If you notice anything else that looks suspicious you might want to avoid using that and report it to somebody to check it closer.




