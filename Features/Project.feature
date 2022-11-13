
Feature: Test Login page

  Scenario: correct Email and Password
    Given user at login page
     When user insert correct emil and password
     And  user Click login button
     Then use should be in home page
