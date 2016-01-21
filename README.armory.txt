================================================================================
  BZFlag Server Plugin :: armory
================================================================================

Adds a gamemode similar to Team Fortress 2's "payload" gamemode.

To run with the default map bundled with this plugin, run bzfs with:
  -conf armory.conf
Change vthe .conf file as needed for the file paths.

Attackers(Red team):
  Break into the other team's armory.

  Grab the Key(KY) flag and capture the armory points in order.
  When a point is captured, the flag is returned back to your base.

  Capturing points increases the timelimit by 10 seconds.

  You win by capturing the armory at the end.

Defenders(Green team):
  Prevent the Attackers from breaking into your armory.

  The default match duration, if unspecified, is 2 minutes.

  You win by holding the Attackers back for the duration of the match.

---------------------------------------
  Loading The Plugin
---------------------------------------

To load the plugin with default settings, use:
  -loadplugin armory

To load the plugin with parameters use the format:
  -loadplugin armory,<matchtime in minutes>
For example:
  -loadplugin armory,2

---------------------------------------
  Custom Map Objects
---------------------------------------

armorypoint # Start of the armorypoint

  # Define the position of the armorypoint
  pos <x> <y> <z>

  # Size of the armorypoint
  size 10 10 10

  # Rotation of the armorypoint
  rot 45

  # The name of the armorypoint that's referenced by other points
  # The final armorypoint HAS to be "armory"
  name armorypoint

  # The visible name of the armorypoint
  title Armory Point

  # What becomes unlocked when this point is captured
  unlock armory

end # End of the armorypoint definition
