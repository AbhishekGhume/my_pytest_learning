@transaction
Feature: Bank Transaction
    Tests pretaining to banking transactions like withdrawal, deposit

    Background: 
        Bank account is active

    Scenario: Withrawal of money
        Given the account balance is 100
        When the account holder withdraws 30
        Then the account balance should be 70