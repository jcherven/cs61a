# I'm going to work through Berkeley CS61a

## The Course

[cs61a.org](https://cs61a.org)

## The Book

[Composing Programs by John DeNero]( https://composingprograms.com )

## Using OK to do exercises and homework

[Using OK at cs61a.org]( https://cs61a.org/articles/using-ok.html )

### Quick Reference:

#### Run the OK autograder/tester with

`$ python3 ok`

#### Run OK with network submission to okpy.org disabled with the local flag:

`python3 ok --local`

Consider aliasing that to `ok` in your terminal environment since non-enrolled students can't use the upload features.

#### Run the test on a specific question

`python3 ok -q <name of the question>`

OK will test all quesitons by default if `-q` is omitted.

#### Displaying Tests

OK displays only failed tests by default. Display all tests with the `-v` flag.

`python3 ok -v`

#### Submitting assignments

Submitting will run the assignment's tests and try to upload the assignment to okpy.org. Not being a student and therefore not having an account, this won't work. Just run the test and don't worry about submitting.

Simply commit the completed assignment to the repo when you're satisfied with the result of the tests.

## A python3 execution visualizer

[pythontutor.com](http://pythontutor.com/composingprograms.html#mode=edit)

## A python3 interpreter that runs in the browser

[code.cs61a.org](https://code.cs61a.org/)
