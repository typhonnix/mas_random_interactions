init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_random_love_you",
            category=["romance", "???"],
            prompt="Love you",
            pool=True,
            unlocked=True,
            random=True,
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label monika_random_love_you:
    $ ev = mas_getEV("monika_random_love_you")
    m 5eua "Hey [player]!"
    $ _history_list.pop()
    menu :
        "Yes, [m_name]?":
            m 5hublb "I love you~"
            return "love"
