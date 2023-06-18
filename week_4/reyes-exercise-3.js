/*
===========================================================================================
; Title: reyes-exercise-3.js
; Author: Tiffany Reyes
; Date: 17 June 2023
; Description: An introduction to mongosh. Below are queries used for exercise 4.3
;==========================================================================================
*/

// This query is to find all documents in the users collection
db.users.find()

// This query is to find any document in the users collection with specified email
db.users.find({email: 'jbach@me.com'})

// This query is to find any document in the users collection with specified lastName
db.users.find({lastName: 'Mozart'})

// This query is to find any document in the users collection with specified firstName
db.users.find({firstName: 'Richard'})

// This query is to find any document in the users collection with specified employeeId
db.users.find({employeeId: '1010'})