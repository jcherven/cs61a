# I'm going to work through Berkeley CS61a
## The Course
https://cs61a.org

## The Book
https://composingprograms.com

## Using OK to do exercises and homework
https://cs61a.org/articles/using-ok.html

### Quick Reference:
#### Run the OK autograder/tester with
`$ python3 ok`

#### Run OK with network submission to Berkeley disabled with the local flag:
`python3 ok --local`

Consider aliasing that to `ok` in your terminal environment since non-enrolled students can't use the upload features.

#### Run the test a specific question

`pythong3 ok -q <name of the question>`

OK will test all quesitons by default if `-q` is omitted.

#### Displaying Tests

OK displays only failed tests by default. Display all tests with the `-v` flag.
`python3 ok -v`

#### Submitting assignments
Submitting will run the assignment's tests and try to upload the assignment to okpy.org. Not being a student and therefore not having an account, this won't work. Just run the test and don't worry about submitting.

Simply commit the completed assignment to the repo when you're satisfied with the result of the tests.

## A python3 interpreter that runs in the browser
https://code.cs61a.org/

