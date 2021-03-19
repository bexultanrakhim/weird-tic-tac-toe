#!/usr/bin/env python3
from simulator import World
from simulator import humanAgent
from simulator import genericAgent

def main():
    wr = World()
    wr.setAgent(genericAgent("X"))
    wr.setAgent(genericAgent("O"))
    while True:
        sp = wr.step()
        for i in wr.getMap():
            print(i)
        print("")
        if(not sp):
            break
    
    for i in wr.getMap():
        print(i)
    
    for agent in wr.players:
        print(agent.getHistory())
if __name__ == "__main__":
    main()