from collections import namedtuple

ID_to_name = {
    1: 'annie',
    2: 'olaf',
    3: 'galio',
    4: 'twistedfate',
    5: 'xinzhao',
    6: 'urgot',
    7: 'leblanc',
    8: 'vladimir',
    9: 'fiddlesticks',
    266: 'aatrox',
    11: 'masteryi',
    12: 'alistar',
    13: 'ryze',
    14: 'sion',
    15: 'sivir',
    16: 'soraka',
    17: 'teemo',
    18: 'tristana',
    19: 'warwick',
    20: 'nunu',
    21: 'missfortune',
    22: 'ashe',
    23: 'tryndamere',
    24: 'jax',
    25: 'morgana',
    26: 'zilean',
    27: 'singed',
    28: 'evelynn',
    29: 'twitch',
    30: 'karthus',
    31: 'chogath',
    32: 'amumu',
    33: 'rammus',
    34: 'anivia',
    35: 'shaco',
    36: 'drmundo',
    37: 'sona',
    38: 'kassadin',
    39: 'irelia',
    40: 'janna',
    41: 'gangplank',
    42: 'corki',
    43: 'karma',
    44: 'taric',
    45: 'veigar',
    48: 'trundle',
    50: 'swain',
    51: 'caitlyn',
    53: 'blitzcrank',
    54: 'malphite',
    55: 'katarina',
    56: 'nocturne',
    57: 'maokai',
    58: 'renekton',
    59: 'jarvaniv',
    60: 'elise',
    61: 'orianna',
    62: 'monkeyking',
    63: 'brand',
    64: 'leesin',
    67: 'vayne',
    68: 'rumble',
    69: 'cassiopeia',
    72: 'skarner',
    268: 'azir',
    74: 'heimerdinger',
    75: 'nasus',
    76: 'nidalee',
    77: 'udyr',
    78: 'poppy',
    79: 'gragas',
    80: 'pantheon',
    81: 'ezreal',
    82: 'mordekaiser',
    83: 'yorick',
    84: 'akali',
    85: 'kennen',
    86: 'garen',
    267: 'nami',
    89: 'leona',
    90: 'malzahar',
    91: 'talon',
    92: 'riven',
    96: 'kogmaw',
    98: 'shen',
    99: 'lux',
    101: 'xerath',
    102: 'shyvana',
    103: 'ahri',
    104: 'graves',
    105: 'fizz',
    106: 'volibear',
    107: 'rengar',
    110: 'varus',
    111: 'nautilus',
    112: 'viktor',
    113: 'sejuani',
    114: 'fiora',
    115: 'ziggs',
    117: 'lulu',
    119: 'draven',
    120: 'hecarim',
    121: 'khazix',
    122: 'darius',
    126: 'jayce',
    127: 'lissandra',
    131: 'diana',
    133: 'quinn',
    134: 'syndra',
    136: 'aurelionsol',
    143: 'zyra',
    150: 'gnar',
    154: 'zac',
    412: 'thresh',
    157: 'yasuo',
    161: 'velkoz',
    420: 'illaoi',
    421: 'reksai',
    429: 'kalista',
    432: 'bard',
    201: 'braum',
    202: 'jhin',
    203: 'kindred',
    222: 'jinx',
    223: 'tahmkench',
    236: 'lucian',
    238: 'zed',
    245: 'ekko',
    10: 'kayle',
    254: 'vi',

}

name_to_ID = {champ: ID for ID, champ in ID_to_name.items()}


ID_to_item = {
    1039: "Hunter's Talisman",
    3101: "Stinger",
    3143: "Randuin's Omen",
    3113: "Aether Wisp",
    3028: "Chalice of Harmony",
    1301: "Enchantment: Alacrity",
    2051: "Guardian's Horn",
    3084: "Overlord's Bloodmail",
    3674: "Enchantment: Devourer",
    2003: "Health Potion",
    1036: "Long Sword",
    3715: "Skirmisher's Sabre",
    3303: "Spellthief's Edge",
    3083: "Warmog's Armor",
    3362: "Greater Vision Totem (Trinket)",
    3285: "Luden's Echo",
    3302: "Relic Shield",
    3116: "Rylai's Crystal Scepter",
    2015: "Kircheis Shard",
    3363: "Farsight Alteration",
    3812: "Death's Dance",
    3152: "Will of the Ancients",
    3117: "Boots of Mobility",
    3599: "The Black Spear",
    1004: "Faerie Charm",
    3174: "Athene's Unholy Grail",
    3156: "Maw of Malmortius",
    3211: "Spectre's Cowl",
    1042: "Dagger",
    3092: "Frost Queen's Claim",
    3672: "Enchantment: Cinderhulk",
    3009: "Boots of Swiftness",
    3240: "Enchantment: Furor",
    3065: "Spirit Visage",
    3144: "Bilgewater Cutlass",
    1332: "Enchantment: Captain",
    3108: "Fiendish Codex",
    3187: "Hextech Sweeper",
    1055: "Doran's Blade",
    3191: "Seeker's Armguard",
    3048: "Seraph's Embrace",
    3004: "Manamune",
    3060: "Banner of Command",
    1318: "Enchantment: Distortion",
    1327: "Enchantment: Captain",
    1308: "Enchantment: Distortion",
    3801: "Crystalline Bracer",
    3340: "Warding Totem (Trinket)",
    2033: "Corrupting Potion",
    3042: "Muramana",
    3047: "Ninja Tabi",
    1306: "Enchantment: Alacrity",
    3139: "Mercurial Scimitar",
    3142: "Youmuu's Ghostblade",
    3020: "Sorcerer's Shoes",
    3114: "Forbidden Idol",
    1325: "Enchantment: Furor",
    3022: "Frozen Mallet",
    3197: "The Hex Core mk-2",
    3673: "Enchantment: Runic Echoes",
    3033: "Mortal Reminder",
    3190: "Locket of the Iron Solari",
    1051: "Brawler's Gloves",
    3056: "Ohmwrecker",
    3751: "Bami's Cinder",
    1413: "Enchantment: Cinderhulk",
    3504: "Ardent Censer",
    3041: "Mejai's Soulstealer",
    1043: "Recurve Bow",
    3089: "Rabadon's Deathcap",
    1403: "Enchantment: Devourer",
    3046: "Phantom Dancer",
    3748: "Titanic Hydra",
    3165: "Morellonomicon",
    1400: "Enchantment: Warrior",
    3902: "Death's Daughter",
    3903: "Raise Morale",
    1300: "Enchantment: Furor",
    3035: "Last Whisper",
    3082: "Warden's Mail",
    3085: "Runaan's Hurricane",
    2050: "Explorer's Ward",
    2049: "Sightstone",
    3053: "Sterak's Gage",
    1316: "Enchantment: Alacrity",
    3145: "Hextech Revolver",
    3096: "Nomad's Medallion",
    3361: "Greater Stealth Totem (Trinket)",
    1321: "Enchantment: Alacrity",
    1052: "Amplifying Tome",
    1401: "Enchantment: Cinderhulk",
    3136: "Haunting Guise",
    3170: "Moonflair Spellblade",
    3078: "Trinity Force",
    3932: "Enchantment: Sated Devourer",
    3706: "Stalker's Blade",
    3115: "Nashor's Tooth",
    3157: "Zhonya's Hourglass",
    3007: "Archangel's Staff (Crystal Scar)",
    2303: "Eye of the Equinox",
    3341: "Sweeping Lens (Trinket)",
    3671: "Enchantment: Warrior",
    1001: "Boots of Speed",
    3094: "Rapid Firecannon",
    3460: "Golden Transcendence",
    3200: "Prototype Hex Core",
    3930: "Enchantment: Sated Devourer",
    3071: "The Black Cleaver",
    1331: "Enchantment: Alacrity",
    3027: "Rod of Ages",
    3185: "The Lightbringer",
    3110: "Frozen Heart",
    3069: "Talisman of Ascension",
    1029: "Cloth Armor",
    3124: "Guinsoo's Rageblade",
    1402: "Enchantment: Runic Echoes",
    3050: "Zeke's Harbinger",
    3073: "Tear of the Goddess (Crystal Scar)",
    3222: "Mikael's Crucible",
    3901: "Fire at Will",
    1415: "Enchantment: Devourer",
    2031: "Refillable Potion",
    1058: "Needlessly Large Rod",
    3072: "The Bloodthirster",
    1328: "Enchantment: Distortion",
    3043: "Muramana",
    1311: "Enchantment: Alacrity",
    3800: "Righteous Glory",
    1026: "Blasting Wand",
    1083: "Cull",
    3098: "Frostfang",
    1305: "Enchantment: Furor",
    1410: "Enchantment: Runic Echoes",
    3508: "Essence Reaver",
    1307: "Enchantment: Captain",
    1302: "Enchantment: Captain",
    3102: "Banshee's Veil",
    1315: "Enchantment: Furor",
    3052: "Jaurim's Fist",
    3040: "Seraph's Embrace",
    1313: "Enchantment: Distortion",
    3057: "Sheen",
    3123: "Executioner's Calling",
    3001: "Abyssal Scepter",
    1033: "Null-Magic Mantle",
    1310: "Enchantment: Furor",
    1333: "Enchantment: Distortion",
    1011: "Giant's Belt",
    2140: "Elixir of Wrath",
    3068: "Sunfire Cape",
    3135: "Void Staff",
    3158: "Ionian Boots of Lucidity",
    3931: "Enchantment: Sated Devourer",
    3301: "Ancient Coin",
    3036: "Lord Dominik's Regards",
    3034: "Giant Slayer",
    3184: "Entropy",
    2052: "Poro-Snax",
    1056: "Doran's Ring",
    1041: "Hunter's Machete",
    1057: "Negatron Cloak",
    3134: "Serrated Dirk",
    1409: "Enchantment: Cinderhulk",
    2032: "Hunter's Potion",
    3025: "Iceborn Gauntlet",
    3097: "Targon's Brace",
    1037: "Pickaxe",
    2301: "Eye of the Watchers",
    1054: "Doran's Shield",
    3242: "Enchantment: Captain",
    1317: "Enchantment: Captain",
    3401: "Face of the Mountain",
    3461: "Golden Transcendence (Disabled)",
    1018: "Cloak of Agility",
    3006: "Berserker's Greaves",
    2302: "Eye of the Oasis",
    3077: "Tiamat",
    1006: "Rejuvenation Bead",
    3090: "Wooglet's Witchcap",
    3010: "Catalyst the Protector",
    3111: "Mercury's Treads",
    3091: "Wit's End",
    3241: "Enchantment: Alacrity",
    3153: "Blade of the Ruined King",
    1322: "Enchantment: Captain",
    3133: "Caulfield's Warhammer",
    3112: "Orb of Winter",
    3512: "Zz'Rot Portal",
    3067: "Kindlegem",
    1411: "Enchantment: Devourer",
    3196: "The Hex Core mk-1",
    3029: "Rod of Ages (Crystal Scar)",
    2045: "Ruby Sightstone",
    3075: "Thornmail",
    1326: "Enchantment: Alacrity",
    1414: "Enchantment: Runic Echoes",
    3100: "Lich Bane",
    1408: "Enchantment: Warrior",
    3105: "Aegis of the Legion",
    3122: "Wicked Hatchet",
    3181: "Sanguine Blade",
    2047: "Oracle's Extract",
    3008: "Manamune (Crystal Scar)",
    3024: "Glacial Shroud",
    1027: "Sapphire Crystal",
    3104: "Lord Van Damm's Pillager",
    3348: "Hextech Sweeper",
    1038: "B. F. Sword",
    3031: "Infinity Edge",
    3044: "Phage",
    3140: "Quicksilver Sash",
    3364: "Oracle Alteration",
    1312: "Enchantment: Captain",
    3026: "Guardian Angel",
    2010: "Total Biscuit of Rejuvenation",
    3155: "Hexdrinker",
    1028: "Ruby Crystal",
    1082: "The Dark Seal",
    2053: "Raptor Cloak",
    3074: "Ravenous Hydra",
    3742: "Dead Man's Plate",
    3146: "Hextech Gunblade",
    3151: "Liandry's Torment",
    3086: "Zeal",
    3087: "Statikk Shiv",
    2139: "Elixir of Sorcery",
    1031: "Chain Vest",
    2054: "Diet Poro-Snax",
    1323: "Enchantment: Distortion",
    1330: "Enchantment: Furor",
    3003: "Archangel's Staff",
    3345: "Soul Anchor (Trinket)",
    3198: "Perfect Hex Core",
    2009: "Total Biscuit of Rejuvenation",
    3070: "Tear of the Goddess",
    2043: "Vision Ward",
    1320: "Enchantment: Furor",
    1303: "Enchantment: Distortion",
    3147: "Duskblade of Draktharr",
    3243: "Enchantment: Distortion",
    3137: "Dervish Blade",
    2138: "Elixir of Iron",
    3711: "Tracker's Knife",
    1053: "Vampiric Scepter",
    1412: "Enchantment: Warrior",
}