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
    EXISTS ((blog)-[:LIKES_BLOG]-(:User {uid:$user})) AS liked
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
    blog.photos[0] AS coverUri,
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
    topic.uid AS id,
    topic.name AS name,
    COUNT(blog) AS blogs
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
    blog.photos[0] AS coverUri,
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
    author.profile_picture AS authorProfile
ORDER BY likes DESC LIMIT $n;
"""

GET_HOTEL_DETAILS_QUERY = """
MATCH
    (city:City)-[:LOCATED_IN]-(hotel:Hotel {uid:$hotel})
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
RETURN
    hotel.uid AS id,
    hotel.photos AS photos,
    hotel.name AS name,
    city.name AS city,
    hotel.locality AS locality,
    hotel.address AS address,
    hotel.postal_code AS postalCode,
    AVG(review.rating) AS rating,
    hotel.phone AS phoneNumber,
    hotel.latitude AS latitude,
    hotel.longitude AS longitude,
    hotel.price AS price,
    hotel.description AS about,
    hotel.amenities AS amenities,
    EXISTS ((hotel)-[:LIKES_HOTEL]-(:User {uid:$user})) AS liked,
    EXISTS ((hotel)-[:VISITED_HOTEL]-(:User {uid:$user})) AS visited
"""

GET_HOTEL_REVIEWS_QUERY = """
MATCH
    (hotel:Hotel {uid:$hotel})-[review:REVIEWED_HOTEL]-(traveller:Traveller)
RETURN
    traveller.uid AS id,
    review.rating AS rating,
    review.review AS review,
    review.datetime AS publishedOn,
    traveller.name AS name
ORDER BY publishedOn DESC
LIMIT $n
"""

GET_ALL_CITIES_QUERY = """
MATCH (city:City)
RETURN
    city.uid AS id,
    city.name AS name,
    city.latitude AS latitude,
    city.longitude AS longitude
"""

HOTEL_SEARCH_QUERY = """
MATCH
    (hotel:Hotel)-[:LOCATED_IN]->(city:City {uid:$cityId})
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
WITH hotel, city, AVG(review.rating) as rating
WHERE
    toLower(hotel.name) CONTAINS $query
    AND hotel.price >= $budgetMin
    AND hotel.price <= $budgetMax
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    city.name AS city,
    rating,
    hotel.locality AS locality,
    round(distance(
        point({latitude: hotel.latitude, longitude: hotel.longitude}),
        point({latitude: city.latitude, longitude: city.longitude})
    ) / 1000) AS distance,
    hotel.price AS price
ORDER BY rating DESC
"""


GET_HOTEL_REVIEWS_ALL_QUERY = """
MATCH (hotel:Hotel {uid:$hotelId})<-[review:REVIEWED_HOTEL]-(user)
RETURN
    ID(review) AS id,
    user.name AS name,
    user.profile_picture AS profileUri,
    review.rating AS rating,
    review.review AS review,
    review.datetime AS publishedOn
ORDER BY publishedOn DESC
"""

GET_HOTEL_BOOKING_DETAILS_QUERY = """
MATCH
    (:User)-[:HAS_BOOKING]->(booking:HotelBooking {uid:$hotelBooking}),
    (booking)-[:FOR_HOTEL]->(hotel:Hotel)-[:LOCATED_IN]->(city:City)
OPTIONAL MATCH
    (hotel)-[review:REVIEWED_HOTEL]-()
RETURN
    {
        id: hotel.uid,
        name: hotel.name,
        locality: hotel.locality,
        coverUri: hotel.photos[0],
        city: city.name,
        rating: AVG(review.rating),
        phone: hotel.phone,
        price: hotel.price,
        latitude: hotel.latitude,
        longitude: hotel.longitude
    } AS hotel,
    {
        adults: booking.adults,
        children: booking.children,
        rooms: booking.rooms,
        days: booking.days,
        date: booking.booking_date
    } AS booking
"""
