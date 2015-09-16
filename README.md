
# Your assignment is to write a small text adventure game.

* The game world consists of 5 rooms with the following paths between them:
E
| A­B || D­C
* The player starts in room A
* The path between A and E is blocked by a locked door
* In room C lies the key the enables the player to pass the locked door
* The game should respond to the following commands:
* look
* go [direction], where direction is one of the compass directions n, e, s, w
* get [item]
* The game ends when the player manages to reach room E

Implementation pointers:
* Don’t use any non­standard libraries
* Express your coding style in the design of the implementation
* Make your implementation elegant; as simple as possible, but not trival
* Make it extensible where you think it matters
* Think about ownership and dependencies
* Make sure the player gets reasonable feedback on actions, both failed and successful
* Feel free to give your own description of rooms and objects
glhf!

Here’s a play­through of an example implementation:
A cold room
<pre>>> go n</pre>
a strong iron door is blocking the way in that direction.
<pre>>> go e</pre>
A dusky room >> go s
A hot room
I can also see the following:
a shining key
<pre>>> get key</pre>
You pick up a shining key.
<pre>>> go w</pre>
A bright room
<pre>>> go n</pre>
A cold room
<pre>>> go n</pre>

You use a shining key to unlock a strong iron door.
A nice garden
Congratulations you've escaped!
