from datetime import datetime

from ..models.database import Blog


def seed_blog():
    return dict(
        blog1=Blog(
            title="Masti in mumbai",
            content="Firstly I took a train to Mumbai from my home city Hyd. You don't know what type of people you are going to meet ,but my co-passengers were good because I didn't loose any of my items from my bag.",
            published_on=datetime(2017, 1, 1),
            photos=[],
        ).save(),
        blog2=Blog(
            title="Playful pleasure of Pune",
            content="The Food here is amazing, One must visit & eat S.P Biryani if visiting Pune, Have Sujata Mastani, Have a goti soda, Jumbo Wadapav, Faluda in Camp is so nice you will love it, Misal pav, Ban maska of Cafe Goodluck is famous since decades, Shegaon Kachori.",
            published_on=datetime(2017, 2, 10),
            photos=[],
        ).save(),
        blog3=Blog(
            title="Peaceful hills in pune",
            content="There are a number of popular hill stations located near Pune. They are so close that if you are rich and have loads of money, you can plan a trip to these fabulous places every weekend and have a gala time with friends and family.",
            published_on=datetime(2017, 2, 3),
            photos=[],
        ).save(),
        blog4=Blog(
            title="Mystic Mumbai",
            content="Once you have landed, it's a long walk till you reach the airport exit gate. It was one of those days when you are raring to go. And even though I did put one foot in front of the other, I just couldn't contain my heart. I took an auto to reach my friend's place. The meter said 27 so I paid 30 rupees and got out of the auto. I heard the driver call out to me, confused I turned around, only to find out he was returning my 3 rupees change. Love at first ride. Is that a phrase? Well it should be, because I did fall in love with this city.",
            published_on=datetime(2019, 12, 10),
            photos=[],
        ).save(),
        blog5=Blog(
            title="Delhi wali dastan",
            content="I think Delhi is a glorious city. As well as being my home-away-from-home, I also find it inspiring and endlessly fascinating. Like Rome, Delhi is an eternal city. Not only is it the capital of modern India, it has been the capital of at least seven previous civilizations, and each have left behind a trail of monuments.",
            published_on=datetime(2020, 3, 2),
            photos=[],
        ).save(),
        blog6=Blog(
            title="Diligent Dilli",
            content=" I prefer to stay where I am treated as something more than a walking wallet. My top Delhi tip is to stay away from the hustle and bustle, and avoid the sharks. Stay instead in the leafy, upscale neighbourhoods of central New Delhi, South Delhi, or Mehrauli. In South Delhi, I rarely get ripped off, because this is not a tourist area: when I get in an auto, I get charged the same price as my neighbours, the locals.",
            published_on=datetime(2020, 1, 10),
            photos=[],
        ).save(),
    )
