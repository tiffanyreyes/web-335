/*
===========================================================================================
; Title: reyes-aggregate-queries.js
; Author: Tiffany Reyes
; Date: 1 July 2023
; Description: Aggregate queries
;==========================================================================================
*/

// A query to show a list of all documents in houses collection
db.houses.find({})

// A query to a list of all documents in students collection
db.students.find({})

// A query to add a document to the students collection
db.students.insertOne({
    firstName: "George",
    lastName: "Weasley",
    studentId: "s1019",
    houseId: "h1007"
})

// A query to find recently added document in collection
db.students.findOne({ "studentId": "s1019" })

// A query to delete a document in collection
db.students.deleteOne({ "studentId": "s1019" })

// A query to find recently deleted document in collection
db.students.findOne({ "studentId": "s1019" })

// A query to lookup students by house
db.houses.aggregate([
   { 
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    }
])

// A query to lookup students by Gryffindor house
db.houses.aggregate([
    { 
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
        $match: { 
            houseId: "h1007"
        }
    }
])

// A query to lookup students by Eagle mascot
db.houses.aggregate([
    { 
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    },
    {
        $match: { 
            mascot: "Eagle"
        }
    }
])

