# Never forget to congratulate your friends and family on their birthday!!!

## DESCRIPTION
This is a simple script that automatically posts "HAPPY BIRTHDAY"-like phrase on your facebook friends wall on the day of their birthday.

## WHY
people having a lot of facebook friends and having not enough time and memory to manage birthday's mess.

## HOW
- you provide token
- on every launch it requests you friends list using your access_token
- builds today birthday candidates 
- post contgrat phrase to the wall (there are more that 30 messages in different languages)

## WHAT IT DOESN'T:
- it doesn't persist ANY data to ANY database

## DEPLOY
0. before using you should get you access_token 
(see https://developers.facebook.com/docs/authentication/)
1. run main.py once or use cron for automatic daily launch

## OPEN ISSUES
token should be updated every x days as fb got rid of offline_access
