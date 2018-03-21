# PROJECT: Tournament Planner

In this project, you’ll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

## Quick Start
### Software Requirements
1. Python Version 2.7 - Refer to the [Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Download) for installation instructions
2. pip Package Manager - Refer to this [installation guide](https://pip.pypa.io/en/stable/installing/)
3. PostgreSQL object-relational database management system - Refer to the [installation guide](https://wiki.postgresql.org/wiki/Detailed_installation_guides)
4. Psycopg2 wrapper for the libpq - Refer to the [installation guide](http://initd.org/psycopg/docs/install.html)

### What is included

Within the download you'll find the following files:

* tournament.sql - set up the database schema
* tournament.py - provides access to the database via a library of functions which can add, delete or query data in the database to a client program
* tournament_test.py - client program which will use the functions written in the tournament.py module
* README.md - this readme file

### How to run the tournament

Clone the repo from github by running
``` sh
git clone https://github.com/wo984c/tournament
```

To build and access the database, run
```sh
psql
\i tournament.sql
\q
```

To run the client program, run
```sh
python tournament_test.py
```

You should be able to see the following output once all your tests have passed:
``` sh
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After one match, players with one win are paired.
Success!  All tests pass!
```
