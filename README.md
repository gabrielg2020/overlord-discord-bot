# Discord Bot
This bot was made to be funny for my friends discord server

## v1.3
- Refined 'HOTS' detection
- Save user timeouts when ran on a container
## v1.2
- Added the `/clearto [@user]` to clear timeouts
## v1.1
- Added `fuzzywuzzy` to replace regular expressions
## v1.0
- If you say 'hots' or 'heroes of the storm' or any variation with capitals, spaces or special characters, you will get timed out.
- The time outs works on an exponential backoff system. The more you get timed out -> the longer you will get timed out for.
- Number of times you have been timed out for is saved in a .json file, so even if the bot goes out, it will remember...
