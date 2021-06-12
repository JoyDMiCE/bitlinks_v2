# 1. What's the program?
   ### This program make bitlink, can count clicks of **_BITLINKS_**

## 2. Environment.
   Environment requirements can be found in requirements.txt, if you can't find file *.env* - it's normal because he's hidden from you(there save a token for a program) *requests* - need to make a _bitlinks_

## 3. How to start? 
   To start a program you need to write `python main.py "link"` in console (terminal).

### 4. Examples.
   Example: `python main.py https://dvmn.org/modules` - This command will give a bitlink(in the command can ALL links).
   
   Taking: `bit.ly/3bKvkyD`.
   
   (_You can check this link_).
   
   Example 2: `python main.py bit.ly/3bKvkyD` - Count clicks of BITLINK, which you made upper.

   Taking: `bit.ly/3bKvkyD
   1`.
   
   ### 5 Bitly token.

   If you don't like reading, here's a video guide - https://www.youtube.com/watch?v=oxXgIN4wvSA .
   

   To get a bitly token (which you need).
   
   go to the site https://bitly.com/ .

   after which, register.

   find your icon (it is on the top right) and click on it.
   
   | --- Profile Settings ----- GENERIC ACCESS TOKEN and enter your password there.
   
   now press the orange button "GENERIC TOKEN".
   
   you were given a token that you copy and paste (example: sd7f87hhjd9ffj454jjef8884s3).
   
   go to the project folder (bitlinks_v2).

   and create a .env file.

   go through it with any editor you are comfortable with.

   *AND WRITE EXACTLY AS WRITTEN HERE*.
   
   BITLY_TOKEN = sd7f87hhjd9ffj454jjef8884s3 (the token you have).
   
   Congratulations, now everything is working for you.