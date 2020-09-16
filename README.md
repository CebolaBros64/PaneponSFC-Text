Resources meant for modifying the text in the SFC/SNES games *Panel de Pon* and *Tetris Attack*.

## Status

### Panel de Pon
 * Panel de Pon [Zuqkeo].tbl (Fan-translation)
   * Some characters identified.
### Tetris Attack
(should also apply to Yoshi no Panepon)
 * Tetris Attack [En].tbl
   * All characters identified. Probably missing a few control codes.
 * Tetris Attack [Ja].tbl
   * Broken and unuseable as of now. The Japanese script switches between two character tables on the fly, and Cartographer does not support that.

## TO-DO
* Figure out the pointer tables for both games.
* Figure out abcde and Atlas.
* Japanese character tables for both games.
* Update "Usage" section of this README.

## Usage
 * Clone this repository
 * Download [Cartographer](https://www.romhacking.net/utilities/647/), and save the executable to the same folder where you cloned the repo
 * Place an unheadered, american ROM for Tetris Attack in the same folder; and rename it to "Tetris Attack (USA) (En,Ja).sfc"
 * Optionally, check out out the readme to learn how Cartographer works
 * Run *dump.cmd*, it should create a file called *output.txt* with the game's text