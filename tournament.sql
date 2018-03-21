
-- Removes the catalog entries for the database and deletes the directory containing the data.
-- Do not throw an error if the database does not exist.

DROP DATABASE IF EXISTS tournament;

-- Creates the Data Base tournament.

CREATE DATABASE tournament;

-- Connects to tournament.

\c tournament;

-- Creates Players table.

CREATE TABLE IF NOT EXISTS players (
    id serial PRIMARY KEY,
    name text NOT NULL
);

-- Creates Matches Table.

CREATE TABLE IF NOT EXISTS matches (
    id serial PRIMARY KEY,
    player_id integer REFERENCES players (id) ON DELETE CASCADE,
    opponent_id integer REFERENCES players (id) ON DELETE CASCADE
);

-- View number of wins per player.

CREATE VIEW results
    AS SELECT players.id as pid, count(matches.player_id) as wins
    FROM players LEFT JOIN matches
    ON players.id = matches.player_id
    GROUP BY players.id
    ORDER BY wins DESC;

-- View matches per player.

CREATE VIEW played
    AS select players.id pid, count(matches) as games
    FROM players LEFT JOIN matches
    ON players.id = matches.player_id
    OR players.id = matches.opponent_id
    GROUP BY players.id;

-- View list of (id, name, wins, matches)
-- for each player, sorted by the number of wins each player has.

CREATE VIEW standings
    AS SELECT players.id, players.name, results.wins, played.games
    FROM players, results, played
    WHERE results.pid = players.id
    AND played.pid = players.id
    ORDER BY results.wins DESC;

-- Table definitions for the tournament project.
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


