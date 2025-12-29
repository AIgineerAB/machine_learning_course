# Exercise 3 - pydantic

In this exercise, you get to work with data validation using Pydantic v2. Pydantic is foundational building block for FastAPI.

## 0. Field validation

Define a model Registration with the following fields:

- username (str, min length 3)
- password (str, min length 8)

Try passing invalid values and observe validation errors.

## 1. User data

This exercise will give you a feel of the pydantic library for data validation.

a) Create a BaseModel for a User. It should have a required id (integer) and a required name (string). Instantiate the model with valid data and then with invalid data (e.g., a string for id) to see the ValidationError.

b) Create a BaseModel for a Person with the fields name, age, email, favourite pet. Add appropriate validation in each fields. Tips: you can use built-in EmailStr type in pydantic for validating email. Try out your Person class by instantiating it with different types of values for the fields to see proper validations.

c) Use normal python class to replicate what you have created in b), i.e. create a Person class with proper input validation.

## 2. Validate data from API using Pydantic

Use this code snippet to get a random dad joke

```py
import requests

headers = {"Accept": "application/json"}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)

print(response.json())
```

a) Create a Pydantic model with name Joke with the following fields

- id with type integer
- joke with type string

b) Validate the data from the API using the Joke model. Test out your Joke instance to see that you can access the joke and id fields.

c) Now create a new Joke Pydantic model that also have the field words_in_joke. This is a computed field and a property so you will need to decorate your method like this

```py
    @computed_field
    @property
    def words_in_joke(self) -> int:
        """returns number of words in the joke"""
```

Note that computed_field is imported from pydantic. Validate a random joke with your new Joke model.

d) Request 10 jokes from the api and validate them into many Jokes instances that you store into a list. Make sure to use sleep for 5 seconds to not request from the API too much.


## 3. Theory questions

a) Explain the primary purpose of Pydantic. What core problems does it solve for developers?

b) In Pydantic, what is the key difference between using model_validate() and model_validate_json()? When would you use each one?

c) How can you define a field in a Pydantic model that has a specific value constraint, such as a minimum or maximum number? Give an example.

d) Describe how Pydantic's data validation can improve the robustness and reliability of an application that processes data from an external API.

e) What is a computed field in Pydantic?


## 4. Glossary

| Glossary        | Description |
| --------------- | ----------- |
| BaseModel       |             |
| Field           |             |
| model_fields    |             |
| computed_field  |             |
| model_validate  |             |
| model_dump      |             |
| type hinting    |             |
| serialization   |             |
| deserialization |             |
