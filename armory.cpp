// armory.cpp : Defines the entry point for the DLL application.

// Some code copied from other default plugins ;)

/*
  BSD license

  Copyright (c) 2016 Kaadmy
  All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:

  1. Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer. 
  2. Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

  The views and conclusions contained in the software and documentation are those
  of the authors and should not be interpreted as representing official policies, 
  either expressed or implied, of the FreeBSD Project.
*/

#include <vector>
#include <map>
#include <math.h>
  
#include "bzfsAPI.h"
#include "plugin_utils.h"

enum {
  ATTACKERS = 0,
  DEFENDERS,
  TIE
};

// armorypoint class
class ArmoryPoint:public bz_CustomZoneObject
{
public:
  ArmoryPoint():bz_CustomZoneObject() {}

  std::string title;
  std::string name;
  std::string unlock;
};

// main armory class
class armory:public bz_Plugin, bz_CustomMapObjectHandler
{
public:
  virtual const char* Name (){return "Armory";}

  virtual bool MapObject (bz_ApiString object, bz_CustomMapObjectInfo *data);

  virtual bool EnoughPlayers(void);
  virtual bool NoPlayers(void);

  virtual void StartMatch(void);

  virtual void WinState (int team);

  virtual void Event (bz_EventData *eventData);

  virtual void Init (const char* config);
  virtual void Cleanup (void);
  
  std::vector<ArmoryPoint> armoryPoints;
  std::map<std::string, int> unlockedPoints; // list of unlocked points names
  
  float matchTime; // time for each round to be; this shouldn't change after init
  float matchEndTime; // what time the round ends at
  bool matchEnded; // if the match is ended or not enough players

  float nextTimeWarning; // when to show the next "time remaining" message

  bz_eTeamType attackTeamColor;
  bz_eTeamType defendTeamColor;

  int attackerWins;
  int attackerLosses;

  int defenderWins;
  int defenderLosses;

protected:
  typedef struct
  {
    int playerID;
    std::string callsign;
    bool hasKey;
    int team;
  } playerRecord;

  std::map<int, playerRecord> playerList;
};

BZ_PLUGIN(armory)

bool armory::NoPlayers() {
  if(bz_getTeamCount(attackTeamColor) == 0 && bz_getTeamCount(defendTeamColor) == 0)
    return true;
  return false;
}

bool armory::EnoughPlayers() {
  if(bz_getTeamCount(attackTeamColor) >= 1 && bz_getTeamCount(defendTeamColor) >= 1)
    return true;
  return false;
}

void armory::StartMatch (void) {
  if(!matchEnded)
    return;

  if(!EnoughPlayers())
    bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS,
		       "Not enough players, please wait for more players to join.");

  bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, "Round has begun!");

  matchEnded = false;
  matchEndTime = bz_getCurrentTime() + matchTime;

  nextTimeWarning = bz_getCurrentTime() + 3;

  // reset all the player scores
  for(unsigned int i = 0; i < playerList.size(); i++) {
    bz_resetPlayerScore(playerList[i].playerID);
  }
}

void armory::WinState (int team) {
  if(matchEnded)
    return;

  matchEnded = true;

  std::string teamString = "Attackers";

  if(team == ATTACKERS) {
    attackerWins ++;
    defenderLosses --;
    
    bz_setTeamWins(attackTeamColor, attackerWins);
    bz_setTeamLosses(defendTeamColor, defenderLosses);
  } else if(team == DEFENDERS) {
    defenderWins ++;
    attackerLosses --;
    
    bz_setTeamWins(defendTeamColor, defenderWins);
    bz_setTeamLosses(attackTeamColor, attackerLosses);

    teamString = "Defenders";
  } else if(team == TIE) {
    teamString = "Nobody";
  }
  
  if(strcmp(teamString.c_str(), "Nobody")) 
    bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, "Nobody won the round; It's a tie!");
  else
    bz_sendTextMessagef(BZ_SERVER, BZ_ALLUSERS, "The %s have won the round!", teamString.c_str());

  int highestRank = 0;
  int mvp = -1;

  //  bz_debugMessage(0, std::to_string(playerList.size()).c_str());
  for(unsigned int i = 0; i < playerList.size(); i++) {

    if(team != TIE) {
      int rank = bz_getPlayerRank(playerList[i].playerID);

      if(playerList[i].team == team && rank > highestRank) {
	highestRank = rank;
	mvp = i;
      }
    }

    // kill the player
    bz_killPlayer(playerList[i].playerID, false, BZ_SERVER);

    // and "fix" the player's score after killing them
    bz_setPlayerLosses(playerList[i].playerID, bz_getPlayerLosses(playerList[i].playerID) - 1);
  }

  if(mvp != -1)
    bz_sendTextMessagef(BZ_SERVER, BZ_ALLUSERS,
			"%s was the %s's MVP this round.", playerList[mvp].callsign.c_str(), teamString.c_str());
}

bool armory::MapObject (bz_ApiString object, bz_CustomMapObjectInfo *data) {
  if(object != "ARMORYPOINT" || !data)
    return false;

  ArmoryPoint zone;

  zone.handleDefaultOptions(data);

  zone.title = "UNKNOWN";
  zone.name = "";
  zone.unlock = "";

  for (unsigned int i = 0; i < data->data.size(); i++) {
    std::string line = data->data.get(i).c_str();
	
    bz_APIStringList *nubs = bz_newStringList();
    nubs->tokenize(line.c_str(), " ", 0, true);
	
    if (nubs->size() > 0) {
      std::string key = bz_toupper(nubs->get(0).c_str());
	    
      if (key == "TITLE" && nubs->size() > 1)
	zone.title = nubs->get(1).c_str();
      else if (key == "NAME" && nubs->size() > 1)
	zone.name = nubs->get(1).c_str();
      else if (key == "UNLOCK" && nubs->size() > 1)
	zone.unlock = nubs->get(1).c_str();
    }

    bz_deleteStringList(nubs);
  }

  armoryPoints.push_back(zone);

  return true;
}

void armory::Event (bz_EventData *eventData) {
  switch(eventData->eventType) {
  case bz_eTickEvent: {
    bz_TickEventData_V1* tick = (bz_TickEventData_V1*)eventData;

    if(!EnoughPlayers())
      return;

    float timeLeft = matchEndTime - bz_getCurrentTime(); // seconds remaining in the match

    if(timeLeft < 0.0) {
      WinState(DEFENDERS);
    }

    if(timeLeft > 0.0 && (float)tick->eventTime >= nextTimeWarning) {
      if(timeLeft < 10.0) {
	nextTimeWarning += 1.0; // every second less than 10 seconds

	std::string txt =  + " seconds remaining";
	bz_sendTextMessagef(BZ_SERVER, BZ_ALLUSERS, "%d seconds remaining",
			    (int)ceil(timeLeft));
      } else if(timeLeft < 30.0) {
	nextTimeWarning += 20.0; // from 10 seconds down

	bz_sendTextMessagef(BZ_SERVER, BZ_ALLUSERS, "%d seconds remaining",
			    (int)ceil(timeLeft));
      } else {
	int minutesLeft = ceil(timeLeft / 60);

	if(minutesLeft == 1)
	  nextTimeWarning += 30.0; // half minute
	else
	  nextTimeWarning += 60.0; // next minute

	bz_sendTextMessagef(BZ_SERVER, BZ_ALLUSERS, "%d minutes remaining", minutesLeft);
      }
    }
      
    break;
  }
    
  case bz_eTeamScoreChanged: {
    bz_TeamScoreChangeEventData_V1* event = (bz_TeamScoreChangeEventData_V1*)eventData;

    if(event->element == bz_eWins) {
      if(event->team == attackTeamColor && event->thisValue != attackerWins) {
	bz_setTeamWins(event->team, event->lastValue);
	event->thisValue = event->lastValue;
      } else if(event->team == defendTeamColor && event->thisValue != defenderWins) {
	bz_setTeamWins(event->team, event->lastValue);
	event->thisValue = event->lastValue;
      }
    } else if(event->element == bz_eLosses) {
      if(event->team == attackTeamColor && event->thisValue != attackerLosses) {
	bz_setTeamLosses(event->team, event->lastValue);
	event->thisValue = event->lastValue;
      } else if(event->team == defendTeamColor && event->thisValue != defenderLosses) {
	bz_setTeamLosses(event->team, event->lastValue);
	event->thisValue = event->lastValue;
      }
    }

    break;
  }

  case bz_ePlayerSpawnEvent:
    {
      if(!matchEnded)
	StartMatch();

      break;
    }

  case bz_ePlayerJoinEvent: {
    bz_PlayerJoinPartEventData_V1* event = (bz_PlayerJoinPartEventData_V1*)eventData;

    playerRecord record;

    record.playerID = event->playerID;
    record.callsign = event->record->callsign.c_str();
    record.hasKey = false;
    record.team = bz_getPlayerTeam(event->playerID);

    playerList[event->playerID] = record;

    break;
  }

  case bz_ePlayerPartEvent: {
    bz_PlayerJoinPartEventData_V1* event = (bz_PlayerJoinPartEventData_V1*)eventData;
    std::map<int, playerRecord>::iterator itr = playerList.find(event->playerID);
    if (itr != playerList.end())
      playerList.erase(itr);

    if(NoPlayers())
      WinState(TIE);
      
    break;
  }

  case bz_ePlayerUpdateEvent: {
    bz_PlayerUpdateEventData_V1* player = (bz_PlayerUpdateEventData_V1*)eventData;

    playerRecord &record = playerList.find(player->playerID)->second;

    if(record.hasKey) {
      for(unsigned int i = 0; i < armoryPoints.size(); i++) {
	if(armoryPoints[i].pointInZone(player->state.pos)) {
	  if(unlockedPoints.find(armoryPoints[i].name) != unlockedPoints.end())
	    continue;

	  bool unlocked = true;
	  
	  for(unsigned int j = 0; j < armoryPoints.size(); j++) {
	    if(armoryPoints[j].unlock == armoryPoints[i].name && unlockedPoints.find(armoryPoints[j].name) == unlockedPoints.end()) {
	      unlocked = false;
	      break;
	    }
	  }

	  if(!unlocked)
	    continue;

	  int flagID = bz_getPlayerFlagID(player->playerID);
	  bz_resetFlag(flagID);
	  
	  if(!EnoughPlayers()) {
	    bz_sendTextMessage(BZ_SERVER, player->playerID, "Not enough players, play fair!");
	    return;
	  }

	  std::string capStr;
	  if(armoryPoints[i].unlock != "") {
	    for(unsigned int j = 0; j < armoryPoints.size(); j++) {
	      if(armoryPoints[j].name == armoryPoints[i].unlock) {
		capStr = armoryPoints[j].title;
		capStr += " has been unlocked by ";
		capStr += record.callsign;
		capStr += "!";

		matchEndTime += 10; // increase time limit by 10 seconds		
		capStr += " +10 seconds!";
		break;
	      }
	    }
	  } else {
	    capStr = record.callsign;
	    capStr += " has captured ";
	    capStr += armoryPoints[i].title;
	    capStr += "!";
	    WinState(ATTACKERS);
	  }

	  bz_incrementPlayerWins(player->playerID, 10);

	  bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, (capStr).c_str());

	  unlockedPoints.insert(std::pair<std::string, int>(armoryPoints[i].name, 0));

	  record.hasKey = false;

	  break;
	}
      }
    }

    break;
  }

  case bz_eFlagGrabbedEvent: {
    bz_FlagGrabbedEventData_V1* event = (bz_FlagGrabbedEventData_V1*)eventData;

    if(strcmp(event->flagType, "KY") == 0) {    
      playerRecord &record = playerList.find(event->playerID)->second;

      if(bz_getPlayerTeam(event->playerID) == attackTeamColor) {
	if(!EnoughPlayers()) {
	  bz_sendTextMessage(BZ_SERVER, event->playerID, "Not enough players, play fair!");

	  int flagID = bz_getPlayerFlagID(event->playerID);
	  bz_resetFlag(flagID);
	  
	  return;
	}

	record.hasKey = true;

	bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, (record.callsign + " has picked up the Key!").c_str());
      } else {
	int flagID = bz_getPlayerFlagID(event->playerID);
	bz_resetFlag(flagID);

	bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, (record.callsign + " has returned the Key!").c_str());
      }
    }

    break;
  }
    
  case bz_eFlagDroppedEvent: {
    bz_FlagDroppedEventData_V1* event = (bz_FlagDroppedEventData_V1*)eventData;

    if(strcmp(event->flagType, "KY") == 0) {    
      playerRecord &record = playerList.find(event->playerID)->second;

      if(record.hasKey) {
	bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, "The Key has been dropped!");
	record.hasKey = false;
      }
    }

    break;
  }
    
  case bz_eFlagTransferredEvent: {
    bz_FlagTransferredEventData_V1* event = (bz_FlagTransferredEventData_V1*)eventData;

    if(strcmp(event->flagType, "KY") == 0) {    
      playerRecord &fromRecord = playerList.find(event->fromPlayerID)->second;
      playerRecord &toRecord = playerList.find(event->toPlayerID)->second;

      fromRecord.hasKey = false;
      toRecord.hasKey = true;

      bz_sendTextMessage(BZ_SERVER, BZ_ALLUSERS, (toRecord.callsign + " has taken the key!").c_str());
    }

    break;
  }
    
  default: {
    break;
  }
  }
}

void armory::Init (const char* commandLine) {
  matchTime = 2 * 60; // default 2 minutes
  matchEndTime = -1;
  matchEnded = true;

  nextTimeWarning = -1;

  attackTeamColor = eRedTeam; // hardcode for now, maybe changeable later
  defendTeamColor = eGreenTeam; // hardcode for now, maybe changeable later

  attackerWins = 0;
  attackerLosses = 0;

  defenderWins = 0;
  defenderLosses = 0;

  std::string param = commandLine;

  int time = atoi(param.c_str());
  if(time > 0) matchTime = (float)(time * 60);

  matchTime += 3; // extra 3 seconds for preparation/spawning

  Register(bz_eTickEvent);

  Register(bz_eTeamScoreChanged);

  Register(bz_ePlayerUpdateEvent);
  Register(bz_ePlayerSpawnEvent);
  Register(bz_ePlayerPartEvent);
  Register(bz_ePlayerJoinEvent);

  Register(bz_eFlagGrabbedEvent);
  Register(bz_eFlagDroppedEvent);
  Register(bz_eFlagTransferredEvent);

  bz_RegisterCustomFlag("KY", "Key", "Take the key through armory points to unlock the armory!", 0, eGoodFlag);

  bz_registerCustomMapObject("armorypoint", this);

  MaxWaitTime = 0.1;
}

void armory::Cleanup (void) {
  Flush();

  bz_removeCustomMapObject("armorypoint");
}
