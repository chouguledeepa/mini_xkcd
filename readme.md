# Package 
packages are use to group or packages multiple module
that work together to solve problem.

## http verbs(aka methods)
- resources (data)

    - HTTP verbs / HTTP methods
        - GET (200-success)
        - POST 
        - PATCH
        - PUT
        - DELETE
        - # Resource (data)
- Singular resource: /api/planets/1/
- Plural resource: /api/planets
# built-in variable called `__name__`

- __name__ variable represents current module
- variable `__name__` is set to value `__main__` by default when running current module.
- `if __name__ == "__main__":` used to represent entrypoint
# Convention to use import statement

- import statements should always go on top


Absolute URL: home url + relative url (Example - https://swapi.dev/api/planets/1/)

# Project structure
### swapi-sample 
- swapitask1.py (entrypoint)
- utils (package containing utility functions)
  - randomnum (produces random numbers between given range)