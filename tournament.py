#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def dbconnect():
    """Connect to the PostgreSQL database.  Returns a database connection
       and cursor."""

    try:
        conn = psycopg2.connect("dbname=tournament")
        cur = conn.cursor()
        return conn, cur

    except Exception, err:
        print('Data Base connection error. Description {0}'.
              format(err.message))
        return None, None


def selects(sql):
    """ Execute query statements. """

    conn, cur = dbconnect()

    if cur is not None:
        try:
            cur.execute(sql, ())
            """ conn.commit() """
            return cur.fetchall()

        except Exception, err:
            print('Query execution error. Description {0}'.format(err.message))

        finally:
            conn.close()


def commits(sql, param=None):
    """ Execute modification queries requiring commit. """

    conn, cur = dbconnect()

    if cur is not None:
        try:
            cur.execute(sql, param)
            conn.commit()

        except Exception, err:
            print('Query execution error. Description {0}'.format(err.message))

        finally:
            conn.close()


def deleteMatches():
    """Remove all the match records from the database."""

    result = commits("DELETE FROM matches")


def deletePlayers():
    """Remove all the player records from the database."""

    result = commits("DELETE FROM players")


def countPlayers():
    """Returns the number of players currently registered."""

    result = selects("SELECT COUNT(id) FROM players")

    if result is not None:
        return result[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    result = commits("INSERT INTO players (name) VALUES (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    result = selects("SELECT * FROM standings")
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    result = commits("INSERT INTO matches(player_id, opponent_id) \
                     VALUES(%s, %s)", (winner, loser, ))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    count = 0
    standing = playerStandings()
    pairs = len(standing)/2
    my_pairs = []

    for x in range(0, pairs):
        match = (standing[count][0], standing[count][1],
                 standing[count + 1][0], standing[count + 1][1],)
        my_pairs.append(match)
        count += 2

    return (my_pairs)
