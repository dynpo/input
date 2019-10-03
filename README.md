# dynpoinput

This project provides a dynamic input package, you can define a object with the parameters that you need and even pass custom validation to it. Default basic valitation for datatype is already in place.

## Installation

Install from source:

```
$ git clone git@github.com:dynpo/input.git
$ cd input
$ pip .
```

## Example

By default, the rbkcli will attempt to read the the Rubrik Cluster credentials from the following environment variables:

```python
from dynpoinput import MyInput

inputer = MyInput()
name = inputer.get_input(msg='Please provide the name: ',
                         required=True,
                         data_type='string')
print(name)
```


## Documentation

Here are some resources to get you started! If you find any challenges from this project are not properly documented or are unclear, please raise an issue and let us know!

* [Documentation Summary](docs/SUMMARY.md)

## How You Can Help

We glady welcome contributions from the community. From updating the documentation to adding more functions for Python, all ideas are welcome.

* [Contributing Guide](CONTRIBUTING.md)
* [Code of Conduct](CODE_OF_CONDUCT.md)

## License

* [MIT License](LICENSE)

## About Dynpo

It is a group of libraries to facilitate Python Automation, seeks to empower dynamic coding and decrease the time to maintain and write new code.
