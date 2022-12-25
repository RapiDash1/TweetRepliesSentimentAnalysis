db.createUser(
    {
        user: "twitteradmin",
        pwd: "adminpassword",
        roles: [
            {
                role: "readWrite",
                db: "tweetanalysis"
            }
        ]
    }
);