GET_BLOG_DETAILS_QUERY = """
MATCH
    (blog:Blog {uid:$blog})-[:AUTHOR_OF]-(traveller:Traveller)
OPTIONAL MATCH
    (blog)-[like:LIKES_BLOG]-()
WITH
    COUNT(like) AS likes, blog, traveller
OPTIONAL MATCH (blog)-[:TAGGED_LOCATION]-(location)
OPTIONAL MATCH (blog)-[:TAGGED_TOPIC]-(topic)
RETURN
    blog.uid AS id,
    blog.title AS title,
    blog.content AS content,
    blog.published_on AS publishedOn,
    blog.photos AS photos,
    likes,
    topic.name AS topic,
    location.name AS location,
    traveller.name AS authorName,
    traveller.profile_picture AS authorProfile,
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

GET_RECOMMENDED_PACKAGES_QUERY = """
MATCH (package:Package)-[review:REVIEWED_PACKAGE]-(user)
WITH
    package.uid AS id,
    package.photos[0] AS coverUri,
    package.name AS name,
    AVG(review.rating) AS R,
    COUNT(review.rating) AS v,
    1 AS m
CALL {
    MATCH (:Package)-[review:REVIEWED_PACKAGE]-()
    RETURN
        AVG(review.rating) AS C
}
RETURN
    id, coverUri, name, R AS rating,
    (R*v + C*m)/(v + m) AS score
ORDER BY score DESC
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

GET_NEARBY_HOTELS_QUERY = """
MATCH (city:City)-[:LOCATED_IN]-(hotel:Hotel)-[review:REVIEWED_HOTEL]-(user)
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    hotel.price AS price,
    AVG(review.rating) AS rating,
    hotel.locality AS locality,
    city.name AS city,
    round(distance(
        point({latitude: hotel.latitude, longitude: hotel.longitude}),
        point({latitude: $latitude, longitude: $longitude})
    ) / 1000) AS distance
ORDER BY distance
LIMIT $n
"""

GET_BUDGET_HOTELS_QUERY = """
MATCH (city:City)-[:LOCATED_IN]-(hotel:Hotel)-[review:REVIEWED_HOTEL]-(user)
RETURN
    hotel.uid AS id,
    hotel.photos[0] AS coverUri,
    hotel.name AS name,
    hotel.price AS price,
    AVG(review.rating) AS rating,
    hotel.locality AS locality,
    city.name AS city
ORDER BY price
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

GET_ALL_TOPICS_QUERY = """
MATCH (topic:Topic)
RETURN
    topic.uid AS id,
    topic.name AS name
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

GET_PACKAGE_DETAILS_QUERY = """
MATCH
    (package:Package {uid:$package})
CALL {
    WITH package
    MATCH
        (package)-[dayRel:HAS_DAY]-(packageDay:PackageDay)
    WITH
        dayRel.day AS day,
        packageDay
    ORDER BY day
    RETURN
        COLLECT({
            day: day,
            title: packageDay.title,
            description: packageDay.description
        }) AS days
}
CALL {
    WITH package
    OPTIONAL MATCH
        (package)-[review:REVIEWED_PACKAGE]-()
    RETURN AVG(review.rating) AS rating
}
CALL {
    WITH package
    MATCH
        (package)-[:OFFERS_PACKAGE]-(agency:Agency)
    OPTIONAL MATCH
        (agency)-[:OFFERS_PACKAGE]-(:Package)-[review:REVIEWED_PACKAGE]-()
    RETURN
        {
            name: agency.name,
            description: agency.description,
            latitude: agency.latitude,
            longitude: agency.longitude,
            address: agency.address,
            phone: agency.phone,
            rating: AVG(review.rating)
        } AS agency
}
RETURN
    package.uid AS id,
    package.photos AS photos,
    package.name AS name,
    package.price AS price,
    package.description AS description,
    rating,
    package.amenities AS amenities,
    days,
    agency,
    EXISTS ((package)-[:LIKES_PACKAGE]-(:User {uid:$user})) AS liked,
    EXISTS ((package)-[:TAKEN_PACKAGE]-(:User {uid:$user})) AS visited
"""

GET_PACKAGE_REVIEWS_QUERY = """
MATCH
    (package:Package {uid:$package})-[review:REVIEWED_PACKAGE]-(traveller:Traveller)
RETURN
    traveller.uid AS id,
    review.rating AS rating,
    review.review AS review,
    review.datetime AS publishedOn,
    traveller.name AS name
ORDER BY publishedOn DESC
LIMIT $n
"""

GET_PACKAGE_REVIEWS_ALL_QUERY = """
MATCH (package:Package {uid:$package})<-[review:REVIEWED_PACKAGE]-(user)
RETURN
    ID(review) AS id,
    user.name AS name,
    user.profile_picture AS profileUri,
    review.rating AS rating,
    review.review AS review,
    review.datetime AS publishedOn
ORDER BY publishedOn DESC
"""

PACKAGE_SEARCH_QUERY = """
MATCH
    (package:Package)-[:HAS_DAY]->(:PackageDay)-[:VISITS_CITY]-(:City {uid:$cityId})
OPTIONAL MATCH
    (package)-[review:REVIEWED_PACKAGE]-()
WITH package, AVG(review.rating) as rating
WHERE
    toLower(package.name) CONTAINS $query
    AND package.price >= $budgetMin
    AND package.price <= $budgetMax
MATCH
    (package:Package)-[:HAS_DAY]->(day:PackageDay)
RETURN
    package.uid AS id,
    package.photos[0] AS coverUri,
    package.name AS name,
    rating,
    COUNT(day) AS days,
    package.price AS price
ORDER BY rating DESC
"""

GET_PACKAGE_BOOKING_DETAILS_QUERY = """
MATCH
    (:User)-[:HAS_BOOKING]->(booking:PackageBooking {uid:$packageBooking}),
    (booking)-[:FOR_PACKAGE]->(package:Package)
OPTIONAL MATCH
    (package)-[review:REVIEWED_PACKAGE]-()
WITH package, booking, AVG(review.rating) AS rating
CALL {
    WITH package
    MATCH
        (package:Package)-[:HAS_DAY]->(day:PackageDay)
    RETURN COUNT(day) AS days
}
CALL {
    WITH package
    MATCH
        (package)-[:OFFERS_PACKAGE]-(agency:Agency)
    OPTIONAL MATCH
        (agency)-[:OFFERS_PACKAGE]-(:Package)-[review:REVIEWED_PACKAGE]-()
    RETURN
        {
            name: agency.name,
            description: agency.description,
            latitude: agency.latitude,
            longitude: agency.longitude,
            address: agency.address,
            phone: agency.phone,
            rating: AVG(review.rating)
        } AS agency
}
RETURN
    {
        id: package.uid,
        name: package.name,
        coverUri: package.photos[0],
        rating: rating,
        price: package.price,
        days: days
    } AS package,
    {
        people: booking.people,
        date: booking.booking_date
    } AS booking,
    agency
"""

GET_USER_BOOKINGS_QUERY = """
MATCH (user:User {uid: $user})
CALL {
    WITH user
    MATCH
        (user)-[:HAS_BOOKING]->(booking:HotelBooking),
        (booking)-[:FOR_HOTEL]->(hotel:Hotel)-[:LOCATED_IN]->(city:City)
    OPTIONAL MATCH
        (hotel)-[review:REVIEWED_HOTEL]-()
    RETURN
        booking.uid AS id,
        booking.booked_at AS bookedAt,
        {
            id: hotel.uid,
            name: hotel.name,
            locality: hotel.locality,
            coverUri: hotel.photos[0],
            city: city.name,
            rating: AVG(review.rating),
            phone: hotel.phone,
            price: hotel.price
        } AS details,
        {
            adults: booking.adults,
            children: booking.children,
            rooms: booking.rooms,
            days: booking.days,
            date: booking.booking_date
        } AS booking,
        "HOTEL" AS type
    UNION ALL
    WITH user
    MATCH
        (user)-[:HAS_BOOKING]->(booking:PackageBooking),
        (booking)-[:FOR_PACKAGE]->(package:Package)
    OPTIONAL MATCH
        (package)-[review:REVIEWED_PACKAGE]-()
    WITH package, booking, AVG(review.rating) AS rating
    CALL {
        WITH package
        MATCH
            (package:Package)-[:HAS_DAY]->(day:PackageDay)
        RETURN COUNT(day) AS days
    }
    RETURN
        booking.uid AS id,
        booking.booked_at AS bookedAt,
        {
            id: package.uid,
            name: package.name,
            coverUri: package.photos[0],
            rating: rating,
            price: package.price,
            days: days
        } AS details,
        {
            people: booking.people,
            date: booking.booking_date
        } AS booking,
        "PACKAGE" AS type
}
RETURN id, bookedAt, details, booking, type
ORDER BY bookedAt DESC
"""

GET_USER_BLOGS_QUERY = """
MATCH
    (blog)-[:AUTHOR_OF]-(user:User {uid: $user})
OPTIONAL MATCH
    (blog)-[:TAGGED_LOCATION]-(location:Location)
CALL {
    WITH blog
    OPTIONAL MATCH
        (blog:Blog)-[like:LIKES_BLOG]-()
    RETURN
        COUNT(like) AS likes
}
RETURN
    blog.uid AS id,
    blog.title AS title,
    blog.content AS content,
    blog.published_on AS publishedOn,
    likes,
    user.name AS username,
    location.name AS location
ORDER BY likes DESC
"""

GET_FAVORITE_CITIES = """
MATCH
    (user:User {uid:$user})-[:LIKES_CITY]-(city:City)
OPTIONAL MATCH
    (city)-[review:REVIEWED_CITY]-()
RETURN
    city.uid AS id,
    city.photos[0] AS coverUri,
    city.name AS name,
    AVG(review.rating) AS rating
"""

GET_CITY_DETAILS_QUERY = """
MATCH
    (city:City {uid:$city})
OPTIONAL MATCH
    (city)-[review:REVIEWED_CITY]-()
WITH
    AVG(review.rating) AS rating,
    city
CALL {
    WITH city
    MATCH
        (city)-[review:REVIEWED_CITY]-(user)
    WITH
        {
            id: ID(review),
            name: user.name,
            profileUri: user.profile_picture,
            rating: review.rating,
            review: review.review,
            publishedOn: review.datetime
        } AS review
    ORDER BY review.publishedOn DESC
    LIMIT 3
    RETURN COLLECT(review) AS reviews
}
CALL {
    WITH city
    MATCH
        (city)-[:LOCATED_IN]-(attraction:Attraction)
    OPTIONAL MATCH
        (attraction)-[review:REVIEWED_ATTRACTION]-()
    WITH
        attraction,
        city,
        AVG(review.rating) AS rating
    ORDER BY rating DESC
    LIMIT 5
    RETURN
        COLLECT({
            id: attraction.uid,
            coverUri: attraction.photos[0],
            name: attraction.name,
            rating: rating
        }) AS topAttractions
}
CALL {
    WITH city
    MATCH
        (package:Package)-[:HAS_DAY]->(:PackageDay)-[:VISITS_CITY]-(city)
    OPTIONAL MATCH
        (package)-[review:REVIEWED_PACKAGE]-()
    WITH
        package,
        AVG(review.rating) AS rating
    ORDER BY rating DESC
    LIMIT 5
    MATCH
        (package:Package)-[:HAS_DAY]->(day:PackageDay)
    WITH
        package,
        COUNT(day) AS days,
        rating
    RETURN
        COLLECT({
            id: package.uid,
            coverUri: package.photos[0],
            name: package.name,
            price: package.price,
            days: days,
            rating: rating
        }) AS topPackages
}
CALL {
    WITH city
    MATCH
        (hotel:Hotel)-[:LOCATED_IN]->(city)
    OPTIONAL MATCH
        (hotel)-[review:REVIEWED_HOTEL]-()
    WITH hotel, city, AVG(review.rating) as rating
    ORDER BY rating DESC
    LIMIT 5
    RETURN
        COLLECT({
            id: hotel.uid,
            coverUri: hotel.photos[0],
            name: hotel.name,
            city: city.name,
            locality: hotel.locality,
            price: hotel.price,
            rating: rating
        }) AS topHotels
}
CALL {
    WITH city
    MATCH
        (blog:Blog)-[like:LIKES_BLOG]-(),
        (blog:Blog)-[:AUTHOR_OF]-(author),
        (blog:Blog)-[:TAGGED_LOCATION]-(city)
    WITH blog, author, city, COUNT(like) AS likes
    ORDER BY likes DESC
    LIMIT 5
    RETURN
        COLLECT({
            id: blog.uid,
            title: blog.title,
            content: LEFT(blog.content, 100),
            likes: likes,
            authorProfile: author.profile_picture
        }) AS topBlogs
}
RETURN
    city.uid AS id,
    city.photos AS photos,
    city.name AS name,
    city.description AS about,
    city.latitude AS latitude,
    city.longitude AS longitude,
    rating,
    EXISTS ((city)-[:LIKES_CITY]-(:User {uid:$user})) AS liked,
    EXISTS ((city)-[:VISITED_CITY]-(:User {uid:$user})) AS visited,
    reviews,
    topAttractions,
    topPackages,
    topHotels,
    topBlogs
"""

GET_EXPLORE_DATA_QUERY = """
MATCH
    (city:City {uid:$city})
CALL {
    WITH city
    MATCH
        (city)-[:LOCATED_IN]-(attraction:Attraction)
    OPTIONAL MATCH
        (attraction)-[review:REVIEWED_ATTRACTION]-()
    WITH
        attraction,
        city,
        AVG(review.rating) AS rating,
        round(distance(
            point({latitude: attraction.latitude, longitude: attraction.longitude}),
            point({latitude: $latitude, longitude: $longitude})
        ) / 1000) AS distance
    ORDER BY distance
    LIMIT 5
    RETURN
        COLLECT({
            id: attraction.uid,
            coverUri: attraction.photos[0],
            name: attraction.name,
            rating: rating,
            distance: distance
        }) AS nearbyAttractions
}
RETURN
    nearbyAttractions
"""
