# Home Finder

## About
This is a WIP project which is building a flask application in Python that allows a user to find a suitable address 
that is within their commute time. The idea is that a user can specify their office location and get back a map of london
that is shaded to show the living area based on the commute time specified by the user.

## Design ideas
- Use the google maps api to get travel time 
- Use ONS postcode data to test multiple postcodes to get those that fit the commute time
- Let the user specify which area of london to reduce the number of requests to the API as a cost saving measure


## MVP 
### User Story:
```
As a user
I can input two postcodes and get the travel time between locations
``` 