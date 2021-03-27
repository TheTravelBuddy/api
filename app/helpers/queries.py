GET_BLOG_DETAILS_QUERY = """
MATCH
    (blog:Blog {uid:$blog})-[:AUTHOR_OF]-(traveller:Traveller),
    (blog)-[:TAGGED_TOPIC]-(topic),
    (blog)-[:TAGGED_LOCATION]-(location)
OPTIONAL MATCH
    (blog)-[like:LIKES_BLOG]-()
RETURN
    blog.uid AS id,
    blog.title AS title,
    blog.content AS content,
    blog.published_on AS publishedOn,
    blog.photos AS photos,
    topic.name AS topic,
    location.name AS location,
    traveller.name AS authorName,
    traveller.profile_picture AS authorProfile,
    COUNT(like) AS likes,
    EXISTS ((blog)-[:LIKES_BLOG]-(:User {uid:$user})) as liked
"""

GET_BLOG_COMMENTS_QUERY = """
MATCH
    (:Blog {uid:$blog})-[comment:COMMENTED_ON]-(traveller:Traveller)
RETURN
    traveller.name AS name,
    comment.content AS comment,
    comment.datetime AS datetime
ORDER BY datetime DESC
LIMIT $n
"""

GET_TOP_LOCATION_BLOGS_QUERY = """
MATCH
    (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author),
    (blog:Blog)-[:TAGGED_LOCATION]-(location)
WITH blog, author, location, COUNT(like) AS likes
ORDER BY likes DESC
WITH
    COLLECT(blog)[0] AS blog,
    COLLECT(author)[0] AS author,
    COLLECT(likes)[0] AS likes,
    location
RETURN
    blog.uid AS id,
    blog.photos[0] as coverUri,
    blog.title AS title,
    blog.published_on AS publishedOn,
    LEFT(blog.content, 100) AS content,
    likes,
    author.profile_picture AS authorProfile,
    location.uid AS locationId,
    location.name AS locationName
LIMIT $n
"""

GET_TOP_BLOG_TOPICS_QUERY = """
MATCH
    (blog:Blog)-[:TAGGED_TOPIC]->(topic:Topic)
RETURN
    topic.uid as id,
    topic.name as name,
    COUNT(blog) as blogs
ORDER BY blogs DESC
LIMIT $n
"""

GET_TOP_BANNER_BLOGS_QUERY = """
MATCH
    (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author)
RETURN
    blog.uid AS id,
    blog.title AS title,
    left(blog.content, 150) AS content,
    COUNT(like) AS likes,
    author.profile_picture AS authorProfile,
    blog.photos[0] as coverUri,
    blog.published_on AS publishedOn
ORDER BY likes DESC
LIMIT $n;
"""

GET_TOP_PACKAGES_QUERY = """
MATCH (package:Package)-[review:REVIEWED_PACKAGE]-(user)
RETURN
    package.uid AS id,
    package.photos[0] AS coverUri,
    package.name AS name,
    AVG(review.rating) AS rating
ORDER BY rating DESC
LIMIT $n
"""

GET_TOP_DESTINATIONS_QUERY = """
MATCH (city:City)-[review:REVIEWED_CITY]-(user)
RETURN
    city.uid AS id,
    city.photos[0] AS coverUri,
    city.name AS name,
    AVG(review.rating) AS rating
ORDER BY rating DESC
LIMIT $n
"""

GET_TOP_HOTELS_QUERY = """
MATCH (city:City)-[:LOCATED_IN]-(hotel:Hotel)-[review:REVIEWED_HOTEL]-(user)
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    hotel.price AS price,
    AVG(review.rating) AS rating,
    hotel.locality AS locality,
    city.name AS city
ORDER BY rating DESC
LIMIT $n
"""

GET_TOP_BLOGS_QUERY = """
MATCH (blog:Blog)-[like:LIKES_BLOG]-(),
    (blog:Blog)-[:AUTHOR_OF]-(author)
RETURN
    blog.uid AS id,
    blog.title AS title,
    left(blog.content, 100) AS content,
    COUNT(like) AS likes,
    author.profile_picture as authorProfile
ORDER BY likes DESC LIMIT $n;
"""

GET_HOTEL_DETAILS_QUERY = """
MATCH
    (city:City)-[:LOCATED_IN]-(hotel:Hotel {uid:$hotel})
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
RETURN
    hotel.uid as id,
    hotel.photos as photos,
    hotel.name as name,
    city.name as city,
    hotel.locality as locality,
    hotel.address as address,
    hotel.postal_code as postalCode,
    AVG(review.rating) as rating,
    hotel.phone as phoneNumber,
    hotel.latitude as latitude,
    hotel.longitude as longitude,
    hotel.price as price,
    hotel.description as about,
    hotel.amenities as amenities,
    EXISTS ((hotel)-[:LIKES_HOTEL]-(:User {uid:$user})) as liked
"""

GET_HOTEL_REVIEWS_QUERY = """
MATCH
    (hotel:Hotel {uid:$hotel})-[review:REVIEWED_HOTEL]-(traveller:Traveller)
RETURN
    traveller.uid as id,
    review.rating as rating,
    left(review.review,150) as review,
    review.datetime as datetime,
    traveller.name as name
ORDER BY datetime DESC
LIMIT $n
"""

GET_OWNED_HOTELS = """
MATCH
    (hotel:Hotel)-[:LOCATED_IN]->(city:City),
    (hotel)-[:OWNS_HOTEL]-(hotelOwner:HotelOwner {uid:$hotelierId})
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    city.name AS city,
    AVG(review.rating) as rating,
    hotel.locality AS locality,
    hotel.price AS price
ORDER BY rating DESC
"""
