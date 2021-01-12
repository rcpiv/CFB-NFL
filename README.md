# CFB-NFL
## Creating a app of win history with the feature to look at last time two teams won the same weekend
### Current Progress
- 12/17/2020: Obtained data from sports-reference.com and api.collegefootballdata.com. Cleaned CFB and NFL data to be prepped for import into Tableau
- 12/31/2020: Cleaned data further to add consistent 'WeekId' to link the NFL and CFB schedule together. Began dashboarding. This is going to be more difficult than I thought. May try something simpler.
- 1/4/2021: Realized that a dashboard/Tableau is not the best way to present this. I am pivoting the project to be done in Python and plan on using Flask or Docker. I currently am working on making sure the program works and returns the correct values before I try to make it interactive via Flask/Docker or something else
- 1/11/2021: Added functionality to present all 4 different win/loss combinations between teams (Team A win/Team B win, Team A win/Team B lose,...)
- 1/12/2021: Cleaned up some code and added error handling for user input

### Potential Features
- (ADDED: Week begins on wednesday) Actions to check the history of two teams playing on the same weekend/same week (we love MACtion)
- Check for correlations between 2 teams
- Possibly expand to more than 2 teams
- If successful, include other leagues (NBA, NCAAB, MLB, EPL, etc.)
