# Trivia API

## API Documentation

### Categories

<details>
  <summary>Get Categories</summary>
    get all categories available as a list

  - **method**: `GET`
  - **location**: `/api/v1/categories`
  - **body**: `None`
  - **example request**:

    ```sh
    curl --location --request GET 'localhost:5000/api/v1/categories'
    ```
  - **example response**:

    ```json
    [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        ...
    ]
    ```

</details>

### Questions

<details>
  <summary>Get Questions</summary>
    get all questions available as a list (paginated)

  - **method**: `GET`
  - **location**: `api/v1/questions`
  - **params**: `page: int`
  - **body**: `None`
  - **example request**:

    ```sh
    curl --location --request GET 'http://localhost:5000/api/v1/questions?page=1'
    ```
  - **example response**:

    ```json
    {
        "categories": [
            {
                "id": 1,
                "type": "Science"
            },
            {
                "id": 2,
                "type": "Art"
            },
            {
                "id": 3,
                "type": "Geography"
            },
            {
                "id": 4,
                "type": "History"
            },
            {
                "id": 5,
                "type": "Entertainment"
            },
            {
                "id": 6,
                "type": "Sports"
            }
        ],
        "current_category": null,
        "questions": [
            {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
            },
            {
                "answer": "Apollo 13",
                "category": 5,
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
                "answer": "Tom Cruise",
                "category": 5,
                "difficulty": 4,
                "id": 4,
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
                "answer": "Edward Scissorhands",
                "category": 5,
                "difficulty": 3,
                "id": 6,
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
                "answer": "Brazil",
                "category": 6,
                "difficulty": 3,
                "id": 10,
                "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
                "answer": "Uruguay",
                "category": 6,
                "difficulty": 4,
                "id": 11,
                "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
                "answer": "George Washington Carver",
                "category": 4,
                "difficulty": 2,
                "id": 12,
                "question": "Who invented Peanut Butter?"
            },
            {
                "answer": "Lake Victoria",
                "category": 3,
                "difficulty": 2,
                "id": 13,
                "question": "What is the largest lake in Africa?"
            },
            {
                "answer": "The Palace of Versailles",
                "category": 3,
                "difficulty": 3,
                "id": 14,
                "question": "In which royal palace would you find the Hall of Mirrors?"
            },
            {
                "answer": "Agra",
                "category": 3,
                "difficulty": 2,
                "id": 15,
                "question": "The Taj Mahal is located in which Indian city?"
            }
        ],
        "total_questions": 19
    }
    ```

</details>

<details>
  <summary>Get Questions - by Category</summary>
    get all questions belonging to a category as a list (paginated)

  - **method**: `GET`
  - **location**: `/api/v1/categories/<category_id>/questions`
  - **params**: `page: int`
  - **body**: `None`
  - **example request**:

    ```sh
    curl --location --request GET 'localhost:5000/api/v1/categories/1/questions'
    ```

  - **example response**:

    ```json
    {
        "categories": [
            {
                "id": 1,
                "type": "Science"
            },
            {
                "id": 2,
                "type": "Art"
            },
            {
                "id": 3,
                "type": "Geography"
            },
            {
                "id": 4,
                "type": "History"
            },
            {
                "id": 5,
                "type": "Entertainment"
            },
            {
                "id": 6,
                "type": "Sports"
            }
        ],
        "current_category": null,
        "questions": [
            {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
            },
            {
                "answer": "Apollo 13",
                "category": 5,
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
                "answer": "Tom Cruise",
                "category": 5,
                "difficulty": 4,
                "id": 4,
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
                "answer": "Edward Scissorhands",
                "category": 5,
                "difficulty": 3,
                "id": 6,
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
                "answer": "Brazil",
                "category": 6,
                "difficulty": 3,
                "id": 10,
                "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
                "answer": "Uruguay",
                "category": 6,
                "difficulty": 4,
                "id": 11,
                "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
                "answer": "George Washington Carver",
                "category": 4,
                "difficulty": 2,
                "id": 12,
                "question": "Who invented Peanut Butter?"
            },
            {
                "answer": "Lake Victoria",
                "category": 3,
                "difficulty": 2,
                "id": 13,
                "question": "What is the largest lake in Africa?"
            },
            {
                "answer": "The Palace of Versailles",
                "category": 3,
                "difficulty": 3,
                "id": 14,
                "question": "In which royal palace would you find the Hall of Mirrors?"
            },
            {
                "answer": "Agra",
                "category": 3,
                "difficulty": 2,
                "id": 15,
                "question": "The Taj Mahal is located in which Indian city?"
            }
        ],
        "total_questions": 19
    }
    ```
</details>

<details>
  <summary>Get Questions - by Category (alternative)</summary>
    get all questions belonging to a category as a list

  - **method**: `PSOT`
  - **location**: `/api/v1/questions/by-category`
  - **body**:

    ```json
    {
        "category_id": 2
    }
    ```

  - **example request**:

    ```sh
    curl --location --request POST 'localhost:5000/api/v1/questions/by-category' \
    --data-raw '{
        "category_id": 2
    }'
    ```

  - **example response**:

    ```json
    {
        "categories": [
            {
                "id": 1,
                "type": "Science"
            },
            {
                "id": 2,
                "type": "Art"
            },
            {
                "id": 3,
                "type": "Geography"
            },
            {
                "id": 4,
                "type": "History"
            },
            {
                "id": 5,
                "type": "Entertainment"
            },
            {
                "id": 6,
                "type": "Sports"
            }
        ],
        "current_category": null,
        "questions": [
            {
                "answer": "Muhammad Ali",
                "category": 4,
                "difficulty": 1,
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
            },
            {
                "answer": "Apollo 13",
                "category": 5,
                "difficulty": 4,
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
                "answer": "Tom Cruise",
                "category": 5,
                "difficulty": 4,
                "id": 4,
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
                "answer": "Edward Scissorhands",
                "category": 5,
                "difficulty": 3,
                "id": 6,
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
                "answer": "Brazil",
                "category": 6,
                "difficulty": 3,
                "id": 10,
                "question": "Which is the only team to play in every soccer World Cup tournament?"
            },
            {
                "answer": "Uruguay",
                "category": 6,
                "difficulty": 4,
                "id": 11,
                "question": "Which country won the first ever soccer World Cup in 1930?"
            },
            {
                "answer": "George Washington Carver",
                "category": 4,
                "difficulty": 2,
                "id": 12,
                "question": "Who invented Peanut Butter?"
            },
            {
                "answer": "Lake Victoria",
                "category": 3,
                "difficulty": 2,
                "id": 13,
                "question": "What is the largest lake in Africa?"
            },
            {
                "answer": "The Palace of Versailles",
                "category": 3,
                "difficulty": 3,
                "id": 14,
                "question": "In which royal palace would you find the Hall of Mirrors?"
            },
            {
                "answer": "Agra",
                "category": 3,
                "difficulty": 2,
                "id": 15,
                "question": "The Taj Mahal is located in which Indian city?"
            }
        ],
        "total_questions": 19
    }
    ```

</details>

<details>
  <summary>Search Questions</summary>
    search for question by text matching

  - **method**: `POST`
  - **location**: `localhost:5000/api/v1/questions/search`
  - **body**:

    ```json
    {
        "query": "<query: string>"
    }
    ```

  - **example request**:

    ```sh
    curl --location --request POST 'localhost:5000/api/v1/questions/search' \
    --data-raw '{
        "query": "what"
    }'
    ```

  - **example response**:

    ```json
    {
        "question_count": 8,
        "questions": [
            {
                "id": 9,
                "question": "What boxer's original name is Cassius Clay?"
            },
            {
                "id": 2,
                "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
            },
            {
                "id": 4,
                "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
            },
            {
                "id": 6,
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
            },
            {
                "id": 13,
                "question": "What is the largest lake in Africa?"
            },
            {
                "id": 17,
                "question": "La Giaconda is better known as what?"
            },
            {
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
            },
            {
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            }
        ],
        "success": true
    }
    ```
</details>

<details>
  <summary>Create Question</summary>
    create a question given its text, answer, category and difficulty

  - **method**: `POST`
  - **location**: `/api/v1/questions`
  - **body**:

    ```json
    {
        "answer": "<answer: string>",
        "difficulty": "<difficulty: int>",
        "question": "<question: string>",
        "category_id": "<category id: int>"
    }
    ```

  - **example request**:

    ```sh
    curl --location --request POST 'localhost:5000/api/v1/questions' \
    --data-raw '{
        "answer":"1",
        "difficulty":"5",
        "question":"hi",
        "category_id":5
    }'
    ```

  - **example response**:

    ```json
    {
        "question": {
            "answer": "1",
            "category_id": 5,
            "difficulty": 5,
            "id": 29,
            "question": "hi"
        },
        "success": true
    }
    ```

</details>

<details>
  <summary>Delete Question</summary>
    delete a question by id

  - **method**: `DELETE`
  - **location**: `localhost:5000/api/v1/questions/<question_id>`
  - **body**: `None`
  - **example request**:

    ```sh
    curl --location --request DELETE 'localhost:5000/api/v1/questions/21'
    ```

  - **example response**:

    ```json
    {
        "question_id": "21",
        "success": true
    }
    ```

</details>

### Quiz

<details>
  <summary>Play a turn</summary>
  simulates a trivia game turn, send the current category and previous questions, ends when sending back an empty question

  - **method**: `POST`
  - **location**: `/api/v1/quizzes/play`
  - **body**:

    ```json
    {
        "previous_questions": "<array of question ids>",
        "category_id": "<category id: int>"
    }
    ```

  - **example request**:

    ```sh
    curl --location --request POST 'localhost:5000/api/v1/quizzes/play' \
    --data-raw '{
        "previous_questions": [1, 2],
        "category_id":1
    }'
    ```

  - **example response**:

    ```json
    {
        "question": {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        }
    }
    ```

</details>
