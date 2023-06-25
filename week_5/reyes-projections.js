/*
===========================================================================================
; Title: reyes-projections.js
; Author: Tiffany Reyes
; Date: 25 June 2023
; Description: Projections
;==========================================================================================
*/


// A query to add a new user to user collection
db.users.insertOne({
    firstName: "George",
    lastName: "Handel",
    employeeId: "1013",
    email: "gfhandel@me.com",
    dateCreated: new Date()
})

// A query to update user's email in the collection
db.users.updateOne(
    { lastName: "Mozart" },
    { $set: { email: "mozart@me.com" } }
)

// A query to display specified fields in the user collection
db.users.aggregate( [ { $project : { _id : 0 , firstName : 1 , lastName : 1 , email : 1 } } ] )