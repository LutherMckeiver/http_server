# http-server
    - [X] `GET /` - returns a valid HTML formatted response with a project description and an anchor tag which references a new request to `GET /cow`.
    - [X] `GET /cow?msg=text` - returns a cowpy response which correctly displays a default cow object including the `text` from your query string.
     - [X]`POST /cow msg=text` - returns a cowpy response with a JSON body `{"content": "<cowsay cow>"}`
    - [X] Both `GET` and `POST` should handle any paths that are not defined by you, and return with the appropriate `404 Not Found` response and headers.
    - [X] Ensure that each of your valid routes are also able to handle a malformed request, which should return a `400 Bad Request` response and headers. For example, a request to `GET /cow` which does not include a query string message is not properly formatted for your API, and should respond properly.
### Testing
        - [X] `GET /`: `200 OK <HTML Response>`
        - [X]`!GET /`: `400 Bad Request`

        - [X]`GET /cow?msg=text`: `200 OK <Text Response>`
        - [X]`GET /cow`: `400 Bad Request`
        - `GET /cow?who=dat&wat=do`: `400 Bad Request`
        - [X]`!GET /cow?msg=text`: `405 Invalid Method`

        - [X]`POST /cow msg=text`: `201 Created <JSON Response>`
        - [X] `POST /cow`: `400 Bad Request`
        - [X]`POST /cow who=this how=why`: `400 Bad Request`
        - [X]`!POST /cow msg=text`: `405 Invalid Method`

        - [X]`ANY /does_not_exist`: `404 Not Found`

**Your test suite should have 80% or better test coverage.**
