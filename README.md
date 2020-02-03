# Exploratory-Data-Analysis-on-Dota-2-Matches

### R Notebook
The R notebook version of this project can be found [here](https://leyaof.github.io/Notebooks/dota%20analysis.nb.html)

## Introduction

#### What is Dota 2
Dota 2 is a popular online multiplayer team strategy game released in 2013 by Valve. Each match consists of ten players, randomly assigned into Dire or Radiant team with five players on each team. The objective is to work together as a team to destroy the opposing side’s base while defending their own. In each match, players will play as one of the many heroes in the selection pool with unique abilities to help them win the game. Throughout the match, players accumulate ‘kills’ and ‘assists’ when they defeat an enemy player or help a team member defeat an enemy player. They will also accumulate ‘deaths’ when they are defeated by players on the enemy team. When players get kills or assists, they are granted some amount of gold and which can be used to buy items for their hero and they also gain exp(experience points for their hero) in order to get stronger and be more useful. When players die, they lose some amount of gold and are temporarily timed out and unable to do anything during that window of time.    

#### Objective of this analysis
I will analyze the relationship between the combat variables (kills, deaths, etc.) and the outcome of the matches (win/lose). I will use the 7 years worth of game data my friend Jeff left behind in this analysis. Jeff started playing Dota 2 in December 2012, and quit cold turkey in September 2019. Jeff is sober now after his favourite hero got nerfed (the power of the hero got reduced by the game developers).   

#### Dataset
All data used in this analysis are collected from the open source platform, [OpenDota](https://www.opendota.com/). The dataset and code used can be found [here](https://github.com/leyaof/Exploratory-Data-Analysis-on-Dota-2-matches). The dataset consists of all the matches that Jeff has ever played between 2012 - 2019. Each row represents information of each match and each column represents different feature of a match.
