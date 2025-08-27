@calculator
Feature: Basic Calculator

    Test cases for the basic Calculator operations like addition, subtraction, multiplication and division

    Scenario: Addition of 2 numbers
        Given calculator is open
        When user enters numbers 2 and 3 with + sign between them
        Then the result should be 5

    Scenario: Subtraction of 2 numbers
        Given calculator is open
        And user enters 10
        When user subtracts 5 from it
        Then the result should be 5