import gettext

t = gettext.translation('pskalah', 'locale', fallback=True)
_ = t.ugettext

AI_LIST = [
    {
        "index": 1,
        "name": "Maisy",
        "rank": "1",
        "strategy": "random",  # options: "random", "negamax"
        "tactics": "blind", # options: "blind", "standard"
        "lookahead": 0,  # 1 to 6
        "error_rate": 1.00,  # 0.0 to 1.0; odds of making mistake
        "fitness": "greed",
        "fitness_desc": _("simple"),
        "desc": _("This four-year-old likes to move seeds."),
        "tagline": _("Play is largely random. Very easy to win.")
    },
    {
        "index": 2,
        "name": "Billy",
        "rank": "2",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "blind",
        "lookahead": 0,  # 1 to 6
        "error_rate": 0.20,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("Billy just learned the rules of the game."),
        "tagline": _("Sometimes makes obviously bad moves. Still easy to win against.")
    },
    {
        "index": 3,
        "name": "Emily",
        "rank": "3",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 0,  # 1 to 6
        "error_rate": 0.00,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("Emily is still a novice, but has played multiple times."),
        "tagline": _("Blunt errors are rare, but still easy to win against.")
    },
    {
        "index": 4,
        "name": "Jacob",
        "rank": "4",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 1,  # 1 to 6
        "error_rate": 0.05,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("Jacob plays on occasion with friends."),
        "tagline": _("Jacob plays okay. Moderate difficulty.")
    },
    {
        "index": 5,
        "name": "Emma",
        "rank": "5",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 1,  # 1 to 6
        "error_rate": 0.00,  # 0.0 to 1.0; odds of making mistake
        "fitness_desc": _("greed"),
        "fitness": "greed",
        "desc": _("Emma is determined to win, even if she does not play much."),
        "tagline": _("Emma is a gambler trying to win big. Moderate difficulty.")
    },
    {
        "index": 6,
        "name": "Matthew",
        "rank": "6",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 2,  # 1 to 6
        "error_rate": 0.00,  # 0.0 to 1.0; odds of making mistake
        "fitness": "caution",
        "fitness_desc": _("caution"),
        "desc": _("Matthew plays with friends and family, but is embarrased if he loses by too much."),
        "tagline": _("Matthew is obsessed with keeping you from getting seeds, even if that makes the game long. Moderate difficulty.")
    },
    {
        "index": 7,
        "name": "Olivia",
        "rank": "7",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 2,  # 1 to 6
        "error_rate": 0.05,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("Olivia plays regularly but doesn't consider herself a gamer."),
        "tagline": _("A well-rounded player. Moderate difficulty.")
    },
    {
        "index": 8,
        "name": "William",
        "rank": "8",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 3,  # 1 to 6
        "error_rate": 0.03,  # 0.0 to 1.0; odds of making mistake
        "fitness": "greed",
        "fitness_desc": _("greed"),
        "desc": _("William loves to gamble and win big."),
        "tagline": _("Smart but concentrates on his own store too much. Moderate difficulty.")
    },
    {
        "index": 9,
        "name": "Sam",
        "rank": "9",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 3,  # 1 to 6
        "error_rate": 0.00,  # 0.0 to 1.0; odds of making mistake
        "fitness": "caution",
        "fitness_desc": _("caution"),
        "desc": _("Sam plays a good game and has played all his life."),
        "tagline": _("Too cautious, but a solid player. High difficulty.")
    },
    {
        "index": 10,
        "name": "Sandra",
        "rank": "10",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 4,  # 1 to 6
        "error_rate": 0.01,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("Sandra is very good. Plays regularly."),
        "tagline": _("High difficulty. Errors are very rare.")
    },
    {
        "index": 11,
        "name": "R3 UNIT",
        "rank": "11",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 5,  # 1 to 6
        "error_rate": 0.03,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("An arrogant artificial intelligence.\n\n[b]On some devices, R3 UNIT runs very slow.[/b]"),
        "tagline": _("R3 UNIT looks ahead 5 moves. High difficulty.")
    },
    {
        "index": 12,
        "name": "ThoughtNet",
        "rank": "12",
        "strategy": "negamax",  # options: "random", "negamax"
        "tactics": "standard",
        "lookahead": 5,  # 1 to 6
        "error_rate": 0.00,  # 0.0 to 1.0; odds of making mistake
        "fitness": "balance",
        "fitness_desc": _("balance"),
        "desc": _("A deep artificial intelligence. ThoughtNet finds interacting with humans pleasing.\n\n[b]On some devices, ThoughtNet runs very slow.[/b]"),
        "tagline": _("Very high difficulty. It is still possible to win if you go first.")
    },
]
