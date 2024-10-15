import random

# Step 1: Define some basic tables based on Carbon 2185 and Ultramodern5 for randomization.

# Character backgrounds (simplified)
careers = ['Corporate Drone', 'Criminal', 'Military', 'Hacker', 'Street Samurai', 'Bounty Hunter', 'Solo', 'Netrunner', 'Techie', 'Fixer']
vices = ['Addiction', 'Greed', 'Revenge', 'Violence', 'Lust for Power', 'Loyalty to a Fault']

# Mission types (Carbon 2185 focused)
missions = ['Bounty Hunt', 'Corporate Espionage', 'Heist', 'Assassination', 'Protection Detail', 'Sabotage', 'Tech Recovery', 'Gang Fight']

# Factions and locations (blending both books)
factions = ['Megacorp Execs', 'Underground Gang', 'Cyberpunk Hackers', 'Military Contractor', 'Rebel Faction', 'Netrunner Collective']
locations = ['Megacity Slums', 'Corporate Tower', 'Wasteland Ruins', 'High-Tech District', 'Gang Territory', 'Seedy Bar', 'Tech Market', 'Warehouse District']

# Event/Complication Generator
complications = ['Time-Limited', 'Double-Cross', 'Unforeseen Obstacle', 'AI Malfunction', 'Cyberpsychosis Breakdown', 'Law Enforcement Raid']

# Cyberware and gear (simplified)
cyberware = ['Cybernetic Arm', 'Augmented Eyes', 'Smartgun Link', 'Reflex Enhancers', 'Cyberlegs', 'Nano Tattoos']

# Step 2: Function to generate a random character
def generate_character():
    career = random.choice(careers)
    vice = random.choice(vices)
    return f"Career: {career}, Vice: {vice}"

# Step 3: Function to generate a random mission
def generate_mission():
    mission = random.choice(missions)
    faction = random.choice(factions)
    location = random.choice(locations)
    complication = random.choice(complications)
    return f"Mission Type: {mission}, Faction Involved: {faction}, Location: {location}, Complication: {complication}"

# Step 4: Function to generate random loot/cyberware
def generate_loot():
    return random.choice(cyberware)

# Step 5: Combine everything into one function for the campaign generator
def generate_campaign():
    character = generate_character()
    mission = generate_mission()
    loot = generate_loot()
    
    return {
        "Character": character,
        "Mission": mission,
        "Loot": loot
    }

# Step 6: Generate a sample campaign to test
campaign = generate_campaign()
campaign
