# VAMSEC



This is a python tool that looks for specific code in Virtamate files (.cs files inside .var files, and other loose .cs files).

## DECEMBER 24
https://www.youtube.com/watch?v=FxJb7NYmbss

In December 2024 a security issue was reported and made public regarding the misuse of a certain function in Virtamate files. Since the security breach is public and many people know about it, I made this tool for my patreon supporters to be able to check vars to prevent having issues due to this security breach.

This script will look for that function and highlight the cases found where it's used. There are many plugins that use it legitimately, to open important links and they can be easily identified (links to patreon, github, youtube etc). If the tools finds something that doesn't fit that rule, in a var that's strange or with a link that is unclear where it leads, it's best to avoid using it until some fix is deployed by the virtamate team. As well as reported either here, or on my patreon https://patreon.com/spqr_aeternum , or on the vam discord to the people there, so that somebody can take a closer look at it and inform others in case there's a problem with that var.


## HOW TO USE
1. Download the [latest zip from the releases](https://github.com/5PQR/VAMSEC/archive/refs/tags/December24.zip)
2. Extract archive anywhere, but make sure the path DOESN'T have white spaces in it. Long story. "C:/New Folder" won't work, "C:/New_Folder" or C:/"NewFolder" will work.
3. Right click and Edit the **config.py**  file in any text editor. Put the path to your VAM folder like in the example with two "\\\\" between folders. You can also put any folder that you want to check. The script will look everywhere in that folder for vars and cs files.
4. Run  **VAMSec.December24.bat** and wait. Depending on your VAM size, it might take a long time! Maybe even hours for people with TB worth of mods

## RESULTS
Once finished, the script will generate a results.html file in the same folder. And it will also automatically open it in your default browser, like in the youtube video above.

There will be a table with all the results found. On the third column if you see links such as patreon, github, youtube, vamhub, then those should be ok. If you notice anything else that looks suspicious you might want to avoid using that and report it to somebody to check it closer.




