def seed_blog_relations(travellers, blogs):
    travellers["Jenovah"].author_of.connect(blogs["blog1"])
    travellers["Ester"].author_of.connect(blogs["blog2"])
    travellers["Ester"].author_of.connect(blogs["blog3"])
    travellers["Jenovah"].author_of.connect(blogs["blog4"])
    travellers["Ester"].author_of.connect(blogs["blog5"])
    travellers["Lucifer"].author_of.connect(blogs["blog6"])

    travellers["Justin"].likes_blog.connect(blogs["blog1"])
    travellers["Justin"].likes_blog.connect(blogs["blog3"])
    travellers["Justin"].likes_blog.connect(blogs["blog5"])
    travellers["Justin"].likes_blog.connect(blogs["blog6"])

    travellers["Selena"].likes_blog.connect(blogs["blog2"])
    travellers["Selena"].likes_blog.connect(blogs["blog3"])
    travellers["Selena"].likes_blog.connect(blogs["blog4"])
